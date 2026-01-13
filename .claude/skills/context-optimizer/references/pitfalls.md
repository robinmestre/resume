# Common Pitfalls & Mitigations

Detailed guide to avoiding context optimization failures.

## Attention & Positioning Pitfalls

### Lost in the Middle

**Problem:** Information in the middle of long contexts receives less attention than content at the start or end.

**Symptoms:**
- Claude ignores or misses details from middle sections
- Responses favor information from document boundaries
- Inconsistent retrieval from long corpora

**Mitigation:**
1. Put critical information at START (reference docs) or END (queries)
2. For unavoidable middle content, add explicit retrieval instructions:
   ```
   Before answering, find and quote the relevant passage from 
   document index="3" regarding [SPECIFIC_TOPIC].
   ```
3. Use progressive summarization for very long contexts:
   - Summarize middle sections
   - Keep full text only for boundary sections

### Instructions Buried in Data

**Problem:** Instructions surrounded by large data blocks get attention-diluted.

**Symptoms:**
- Claude ignores or partially follows instructions
- Responses drift from specified format
- Missing required output components

**Mitigation:**
1. Always place instructions AFTER data
2. Place the actual query/task at the END
3. If instructions must appear early, repeat key constraints at end:
   ```xml
   <data>{{LARGE_DATA_BLOCK}}</data>
   
   <instructions>
   Remember: Output must be JSON. Include confidence scores.
   [Full instructions here]
   </instructions>
   
   <query>{{QUESTION}} (Output: JSON with confidence scores)</query>
   ```

## Reference & Attribution Pitfalls

### Ambiguous Document References

**Problem:** Using "this document" or "the passage" when multiple documents exist.

**Symptoms:**
- Claude references wrong document
- Confusion about which source supports claims
- Inconsistent citation patterns

**Mitigation:**
1. Always use explicit index references:
   - ❌ "What does this document say about..."
   - ✅ "What does document index='3' say about..."
2. Include unique identifiers in document wrappers:
   ```xml
   <document index="1" id="annual-report-2023">
   ```
3. In instructions, reference by both index and type:
   ```
   Using the financial_report (document index="1"), extract...
   ```

### Missing Source Attribution

**Problem:** Documents without source metadata can't be properly cited.

**Symptoms:**
- Claude can't trace claims to sources
- No way to verify accuracy
- Responses lack credibility markers

**Mitigation:**
Always include in document wrappers:
```xml
<document index="1">
  <source>annual_report_2023.pdf</source>
  <type>financial_report</type>
  <date>2023-12-31</date>
  <author>CFO Office</author>
  <content>...</content>
</document>
```

## Context Window Pitfalls

### Context Overflow

**Problem:** Total tokens exceed model limits; content silently truncated.

**Symptoms:**
- Later documents missing from responses
- Incomplete analysis
- Unexpected summarization

**Mitigation:**
1. Pre-calculate token counts before submission
2. Budget allocation:
   - Documents: ~70% of limit
   - Instructions: ~10%
   - Output buffer: ~20%
3. For large corpora, use chunking with overlap:
   ```
   Chunk 1: Pages 1-50 (with 5-page overlap at end)
   Chunk 2: Pages 46-100 (overlaps 46-50)
   ```
4. Progressive summarization for supporting documents

### Token Estimation Errors

**Problem:** Actual tokens differ from estimates; unexpected truncation.

**Symptoms:**
- Requests fail with length errors
- Responses cut off mid-sentence

**Mitigation:**
1. Use Anthropic's token counting API for accurate counts
2. Apply 10% safety buffer
3. For mixed content (text + images), overestimate image tokens

## Structural Pitfalls

### Inconsistent Tag Names

**Problem:** Using different names for same concept reduces pattern matching.

**Symptoms:**
- Inconsistent output structure
- Claude misses connections between related sections
- Format drift over conversation

**Mitigation:**
1. Define tag vocabulary upfront:
   ```xml
   <!-- Schema comment: Using <findings>, <evidence>, <recommendations> -->
   ```
2. Reference tags by name in instructions:
   ```
   Place your key findings in <findings> tags, with supporting 
   evidence from the documents in <evidence> tags.
   ```

### Over-Structured Simple Data

**Problem:** Excessive nesting creates parsing overhead for simple content.

**Symptoms:**
- Responses include unnecessary structural artifacts
- Slower processing
- Verbose outputs

**Mitigation:**
Match structure complexity to content complexity:
- Simple list → Plain text or markdown list
- Key-value pairs → JSON or YAML
- Hierarchical with metadata → XML
- Tabular → CSV or markdown table

### Under-Structured Complex Data

**Problem:** Complex data without structure leads to misinterpretation.

**Symptoms:**
- Claude conflates separate concepts
- Inconsistent handling of multi-part data
- Lost relationships between elements

**Mitigation:**
Add structure when data has:
- Multiple sources requiring attribution
- Hierarchical relationships
- Metadata affecting interpretation
- Elements that must remain distinct

## Format-Specific Pitfalls

### JSON in Long Contexts

**Problem:** Large JSON blobs are harder to navigate than equivalent XML.

**Mitigation:**
- Use XML for long documents requiring navigation
- Reserve JSON for state tracking and output schemas
- If JSON required, add section comments:
  ```json
  {
    "// section": "financial_data",
    "revenue": 1000000,
    ...
  }
  ```

### CSV Without Headers

**Problem:** Headerless CSV leads to column misinterpretation.

**Mitigation:**
Always include headers, even if obvious:
```csv
metric,q1,q2,q3,q4
revenue,100,120,115,140
```

### Nested XML Too Deep

**Problem:** Deep nesting (>3 levels) reduces readability and increases errors.

**Mitigation:**
- Keep nesting to 3 levels max
- Flatten where possible using attributes:
  ```xml
  <!-- Instead of: -->
  <document><metadata><source>file.pdf</source></metadata></document>
  
  <!-- Use: -->
  <document source="file.pdf">...</document>
  ```

## Retrieval & Grounding Pitfalls

### No Grounding Instructions

**Problem:** Claude generates answers without citing evidence.

**Symptoms:**
- Responses lack source references
- Can't verify accuracy
- Potential hallucination

**Mitigation:**
Always include grounding instruction for document analysis:
```
Before answering, find and quote the specific passages that support 
your response. Place quotes in <evidence> tags with document index.
```

### Overly Broad Queries

**Problem:** Vague queries lead to unfocused responses.

**Mitigation:**
Structure queries with specificity:
```
❌ "Summarize the document"
✅ "Summarize the key financial metrics from document index='1', 
    specifically: revenue, profit margin, and YoY growth"
```

## Debugging Checklist

When context optimization fails, check:

- [ ] Are documents positioned BEFORE instructions?
- [ ] Is the query at the END?
- [ ] Do all documents have explicit index numbers?
- [ ] Are tag names consistent throughout?
- [ ] Is total token count within limits (with buffer)?
- [ ] Are grounding instructions included for analysis tasks?
- [ ] Do document references use index numbers (not "this document")?
- [ ] Is structure complexity appropriate for content complexity?
