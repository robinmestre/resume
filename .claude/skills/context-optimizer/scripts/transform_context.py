#!/usr/bin/env python3
"""
Transform data files into Claude-optimized context format.

Supports: JSON, CSV, YAML, plain text → XML-wrapped context
"""

import argparse
import json
import csv
import sys
import os
from datetime import datetime
from pathlib import Path

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


def escape_xml(text: str) -> str:
    """Escape special XML characters."""
    if not isinstance(text, str):
        text = str(text)
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))


def read_json(filepath: str) -> dict:
    """Read JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_csv(filepath: str) -> list:
    """Read CSV file as list of dicts."""
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_yaml(filepath: str) -> dict:
    """Read YAML file."""
    if not YAML_AVAILABLE:
        raise ImportError("PyYAML not installed. Run: pip install pyyaml")
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def read_text(filepath: str) -> str:
    """Read plain text file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def detect_format(filepath: str) -> str:
    """Detect file format from extension."""
    ext = Path(filepath).suffix.lower()
    format_map = {
        '.json': 'json',
        '.csv': 'csv',
        '.tsv': 'csv',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.txt': 'text',
        '.md': 'text',
        '.xml': 'text',
    }
    return format_map.get(ext, 'text')


def json_to_xml(data: dict, root_tag: str = "data") -> str:
    """Convert JSON/dict to XML string."""
    
    def convert_value(value, indent=2):
        spaces = " " * indent
        if isinstance(value, dict):
            lines = []
            for k, v in value.items():
                # Sanitize key for XML tag
                tag = str(k).replace(" ", "_").replace("-", "_")
                if isinstance(v, (dict, list)):
                    inner = convert_value(v, indent + 2)
                    lines.append(f"{spaces}<{tag}>\n{inner}\n{spaces}</{tag}>")
                else:
                    escaped = escape_xml(v)
                    lines.append(f"{spaces}<{tag}>{escaped}</{tag}>")
            return "\n".join(lines)
        elif isinstance(value, list):
            lines = []
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    inner = convert_value(item, indent + 2)
                    lines.append(f"{spaces}<item index=\"{i}\">\n{inner}\n{spaces}</item>")
                else:
                    escaped = escape_xml(item)
                    lines.append(f"{spaces}<item index=\"{i}\">{escaped}</item>")
            return "\n".join(lines)
        else:
            return f"{spaces}{escape_xml(value)}"
    
    content = convert_value(data)
    return f"<{root_tag}>\n{content}\n</{root_tag}>"


def csv_to_xml(data: list, source: str = None) -> str:
    """Convert CSV data (list of dicts) to XML."""
    lines = ["<records>"]
    
    for i, row in enumerate(data):
        lines.append(f'  <record index="{i}">')
        for key, value in row.items():
            tag = str(key).replace(" ", "_").replace("-", "_")
            escaped = escape_xml(value)
            lines.append(f"    <{tag}>{escaped}</{tag}>")
        lines.append("  </record>")
    
    lines.append("</records>")
    return "\n".join(lines)


def wrap_document(content: str, source: str, doc_type: str = None, 
                  index: int = 1, priority: str = "primary") -> str:
    """Wrap content in document tags with metadata."""
    
    doc_type_attr = f'\n    <type>{escape_xml(doc_type)}</type>' if doc_type else ''
    
    return f'''<document index="{index}" priority="{priority}">
    <source>{escape_xml(source)}</source>{doc_type_attr}
    <date>{datetime.now().strftime("%Y-%m-%d")}</date>
    <content>
{content}
    </content>
  </document>'''


def create_optimized_context(documents: list, instructions: str = None, 
                              query: str = None) -> str:
    """Create full optimized context structure."""
    
    parts = []
    
    # Documents at top
    if documents:
        parts.append("<documents>")
        for doc in documents:
            parts.append(f"  {doc}")
        parts.append("</documents>")
    
    # Instructions in middle
    if instructions:
        parts.append(f"\n<instructions>\n{instructions}\n</instructions>")
    
    # Query at end
    if query:
        parts.append(f"\n<query>{escape_xml(query)}</query>")
    
    return "\n".join(parts)


def transform_file(filepath: str, output_format: str = "xml", 
                   add_metadata: bool = True, doc_type: str = None) -> str:
    """Transform a single file to optimized format."""
    
    input_format = detect_format(filepath)
    source = Path(filepath).name
    
    # Read and convert based on format
    if input_format == 'json':
        data = read_json(filepath)
        if output_format == 'xml':
            content = json_to_xml(data)
        else:
            content = json.dumps(data, indent=2)
            
    elif input_format == 'csv':
        data = read_csv(filepath)
        if output_format == 'xml':
            content = csv_to_xml(data, source)
        else:
            content = json.dumps(data, indent=2)
            
    elif input_format == 'yaml':
        data = read_yaml(filepath)
        if output_format == 'xml':
            content = json_to_xml(data)
        else:
            content = json.dumps(data, indent=2)
            
    else:  # text
        content = read_text(filepath)
    
    # Wrap with metadata if requested
    if add_metadata and output_format == 'xml':
        inferred_type = doc_type or input_format
        return wrap_document(content, source, inferred_type)
    
    return content


def main():
    parser = argparse.ArgumentParser(
        description="Transform data files for optimal Claude context",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert JSON to XML with metadata
  %(prog)s data.json --format xml --output optimized.xml
  
  # Convert CSV to XML document
  %(prog)s metrics.csv --format xml --type financial_data
  
  # Combine multiple files into context
  %(prog)s doc1.json doc2.csv --combine --output context.xml
  
  # Add instructions and query
  %(prog)s data.json --instructions "Analyze trends" --query "What changed?"
        """
    )
    
    parser.add_argument('files', nargs='+', help='Input file(s) to transform')
    parser.add_argument('--format', '-f', choices=['xml', 'json'], 
                        default='xml', help='Output format (default: xml)')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--add-metadata', action='store_true', default=True,
                        help='Add document metadata wrapper (default: true)')
    parser.add_argument('--no-metadata', action='store_true',
                        help='Skip document metadata wrapper')
    parser.add_argument('--type', '-t', help='Document type for metadata')
    parser.add_argument('--combine', '-c', action='store_true',
                        help='Combine multiple files into single context')
    parser.add_argument('--instructions', '-i', 
                        help='Add instructions section')
    parser.add_argument('--query', '-q', help='Add query section at end')
    
    args = parser.parse_args()
    
    add_metadata = not args.no_metadata
    
    try:
        if args.combine and len(args.files) > 1:
            # Combine multiple files
            documents = []
            for i, filepath in enumerate(args.files, 1):
                doc = transform_file(filepath, args.format, add_metadata, args.type)
                # Re-wrap with correct index
                if add_metadata:
                    content_start = doc.find("<content>")
                    content_end = doc.rfind("</content>")
                    if content_start > -1 and content_end > -1:
                        inner = doc[content_start:content_end + len("</content>")]
                        source = Path(filepath).name
                        doc = wrap_document(
                            inner.replace("<content>\n", "").replace("\n    </content>", ""),
                            source, args.type or detect_format(filepath),
                            index=i, priority="primary" if i == 1 else "supporting"
                        )
                documents.append(doc)
            
            output = create_optimized_context(
                documents, args.instructions, args.query
            )
        else:
            # Single file
            output = transform_file(
                args.files[0], args.format, add_metadata, args.type
            )
            
            if args.instructions or args.query:
                output = create_optimized_context(
                    [output] if add_metadata else [],
                    args.instructions, args.query
                )
        
        # Write output
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"✅ Output written to {args.output}", file=sys.stderr)
        else:
            print(output)
            
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
