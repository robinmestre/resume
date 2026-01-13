# Format Patterns Reference

Complete templates for structuring data optimally for Claude.

## XML Patterns

### Multi-Document Corpus (Analysis Tasks)

```xml
<context>
  <purpose>{{WHAT_CLAUDE_SHOULD_DO}}</purpose>
  <success_criteria>
    <criterion>{{CRITERION_1}}</criterion>
    <criterion>{{CRITERION_2}}</criterion>
  </success_criteria>
</context>

<documents>
  <document index="1" priority="primary">
    <source>{{FILENAME}}</source>
    <type>{{DOCUMENT_TYPE}}</type>
    <date>{{DOCUMENT_DATE}}</date>
    <content>
{{DOCUMENT_CONTENT}}
    </content>
  </document>
  <document index="2" priority="supporting">
    <source>{{FILENAME_2}}</source>
    <type>{{DOCUMENT_TYPE_2}}</type>
    <content>
{{DOCUMENT_CONTENT_2}}
    </content>
  </document>
</documents>

<instructions>
First, identify relevant passages from the documents and cite them.
Then, perform the analysis following these steps:
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}
</instructions>

<output_format>
  <quotes>Relevant passages with document index references</quotes>
  <analysis>Structured analysis following the steps above</analysis>
  <confidence>Assessment of certainty levels</confidence>
</output_format>

<query>{{SPECIFIC_QUESTION}}</query>
```

### Data Extraction Tasks

```xml
<schema>
  <entity name="{{ENTITY_TYPE}}">
    <field name="field1" type="string" required="true"/>
    <field name="field2" type="number" required="false"/>
    <field name="field3" type="date" format="YYYY-MM-DD"/>
  </entity>
</schema>

<source_data format="{{FORMAT}}">
{{RAW_DATA}}
</source_data>

<extraction_rules>
  <rule>Extract all instances of {{ENTITY_TYPE}}</rule>
  <rule>If ambiguous, prefer {{PREFERENCE}}</rule>
  <rule>Mark confidence level for each extraction</rule>
</extraction_rules>

<output_format>JSON array conforming to schema above</output_format>
```

### Chain-of-Thought Integration

```xml
<task>
  <instructions>{{TASK_DESCRIPTION}}</instructions>
  <data>{{INPUT_DATA}}</data>
  <output_structure>
    <thinking>Step-by-step reasoning (show work)</thinking>
    <answer>Final response</answer>
    <confidence>0-100 scale</confidence>
  </output_structure>
</task>
```

### Few-Shot Examples

```xml
<examples>
  <example index="1">
    <input>{{EXAMPLE_INPUT_1}}</input>
    <output>{{EXAMPLE_OUTPUT_1}}</output>
  </example>
  <example index="2">
    <input>{{EXAMPLE_INPUT_2}}</input>
    <output>{{EXAMPLE_OUTPUT_2}}</output>
  </example>
</examples>

<task>
  <input>{{ACTUAL_INPUT}}</input>
  <instructions>Follow the pattern shown in the examples above.</instructions>
</task>
```

## JSON Patterns

### State Tracking

```json
{
  "session": {
    "id": "{{SESSION_ID}}",
    "started": "{{ISO_TIMESTAMP}}",
    "status": "in_progress"
  },
  "tasks": [
    {
      "id": 1,
      "description": "{{TASK_1}}",
      "status": "complete",
      "result": "{{RESULT_1}}"
    },
    {
      "id": 2,
      "description": "{{TASK_2}}",
      "status": "pending",
      "dependencies": [1]
    }
  ],
  "context": {
    "files_processed": ["file1.pdf", "file2.csv"],
    "key_findings": []
  }
}
```

### Structured Output Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["summary", "findings", "recommendations"],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Executive summary in 2-3 sentences"
    },
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["finding", "evidence", "confidence"],
        "properties": {
          "finding": { "type": "string" },
          "evidence": { "type": "string" },
          "confidence": { "type": "number", "minimum": 0, "maximum": 100 }
        }
      }
    },
    "recommendations": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

## YAML Patterns

### Configuration/Parameters

```yaml
analysis_config:
  mode: comprehensive  # Options: quick, comprehensive, deep
  focus_areas:
    - financial_metrics
    - risk_factors
    - competitive_position
  
  output:
    format: markdown
    include_citations: true
    confidence_threshold: 0.7
  
  constraints:
    max_length: 2000  # tokens
    time_range: "2023-01-01 to 2024-12-31"
```

### Hierarchical Metadata

```yaml
document_set:
  name: Q4 Analysis Package
  created: 2024-01-15
  version: 2.1
  
  documents:
    - index: 1
      source: annual_report.pdf
      type: financial_report
      priority: primary
      pages: 1-50
      
    - index: 2
      source: market_research.xlsx
      type: market_analysis
      priority: supporting
      
  processing_notes:
    - "Document 1 contains audited financials"
    - "Document 2 covers North American market only"
```

## Markdown Table Patterns

### Comparison Tables

```markdown
| Criterion | Option A | Option B | Option C | Weight |
|-----------|----------|----------|----------|--------|
| Cost | $10,000 | $15,000 | $8,000 | 0.3 |
| Quality | High | Medium | High | 0.4 |
| Timeline | 4 weeks | 2 weeks | 6 weeks | 0.3 |
| **Score** | **7.8** | **6.5** | **7.2** | — |
```

### Data Summary Tables

```markdown
| Metric | Q1 | Q2 | Q3 | Q4 | YoY Change |
|--------|-----|-----|-----|-----|------------|
| Revenue | $1.2M | $1.4M | $1.3M | $1.8M | +15% |
| Users | 10,000 | 12,500 | 14,000 | 18,000 | +80% |
| NPS | 42 | 45 | 48 | 52 | +10 pts |
```

## Combined Patterns

### Full Analysis Package

```xml
<analysis_package>
  <metadata format="yaml">
created: 2024-01-15
version: 2.1
scope: Q4 performance review
analyst: Claude
  </metadata>
  
  <primary_data>
    <financial_metrics format="csv">
metric,q3,q4,change
revenue,1300000,1800000,38.5%
expenses,900000,1100000,22.2%
profit,400000,700000,75.0%
    </financial_metrics>
  </primary_data>
  
  <supporting_context>
    <market_conditions>
      {{NARRATIVE_TEXT}}
    </market_conditions>
  </supporting_context>
</analysis_package>

<instructions>
Analyze the Q4 performance data and provide:
1. Key performance highlights
2. Areas of concern
3. Recommendations for Q1
</instructions>

<query>What drove the 75% profit increase, and is it sustainable?</query>
```

## Tag Naming Conventions

| Domain | Recommended Tags |
|--------|-----------------|
| Documents | `<documents>`, `<document>`, `<source>`, `<content>` |
| Analysis | `<findings>`, `<evidence>`, `<recommendations>` |
| Reasoning | `<thinking>`, `<answer>`, `<confidence>` |
| Examples | `<examples>`, `<example>`, `<input>`, `<output>` |
| Metadata | `<metadata>`, `<context>`, `<purpose>` |
| Data | `<data>`, `<schema>`, `<records>` |

Use semantic names that describe content. Reference tags explicitly in instructions:
- ✅ "Using the data in `<financial_metrics>`, calculate..."
- ❌ "Using the data above, calculate..."
