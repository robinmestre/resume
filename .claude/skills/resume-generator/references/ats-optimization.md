# ATS Optimization Reference

Rules and best practices for Applicant Tracking System compatibility.

## Markdown to ATS Pipeline

Markdown resumes work well with ATS because:
1. Clean conversion to plain text (most ATS parse plain text)
2. No formatting artifacts that corrupt parsing
3. Easy copy/paste into application forms
4. Converts cleanly to DOCX/PDF via Pandoc if needed

**User workflow:** Copy from artifact → Paste into application OR convert to DOCX/PDF for upload

## Critical Formatting Rules

### Document Structure
- Single-column layout only
- Standard section ordering
- No tables or complex layouts
- Clean hierarchy via Markdown headers

### Section Headers
Use these exact standard headers (ATS looks for them):
- Professional Summary / Summary
- Experience / Work Experience / Professional Experience
- Skills / Technical Skills / Core Competencies
- Education
- Certifications (if applicable)

Do NOT use creative headers like:
- "Where I've Made Impact" (use "Experience")
- "What I Bring" (use "Summary")
- "My Toolkit" (use "Skills")

## Keyword Optimization

### Extraction Strategy
1. Copy JD into text analyzer
2. Identify repeated terms (frequency = importance)
3. Note exact phrasing (match precisely)
4. Capture acronyms AND spelled-out versions

### Placement Priority
1. **Summary section** — Top 3-5 keywords
2. **Skills section** — Technical keywords verbatim
3. **Experience bullets** — Contextual keyword usage
4. **Job titles** — If your actual title differs, add equivalent in parentheses

### Keyword Density
- Top keywords: 2-4% density (appears 2-4 times per 100 words)
- Supporting keywords: 1-2% density
- Avoid keyword stuffing (unnatural repetition)

### Matching Strategies

**Exact match required for:**
- Technical tools (Kubernetes, not "container orchestration")
- Certifications (AWS Solutions Architect, not "cloud certified")
- Methodologies (Agile, Scrum, SAFe — specific terms)

**Semantic matching acceptable for:**
- Soft skills (led teams = leadership = team management)
- Business outcomes (revenue growth = increased sales = business development)

## Common ATS Failures

### Content Failures
| Issue | Problem | Solution |
|-------|---------|----------|
| Creative titles | "Revenue Ninja" not matched to "Sales Manager" | Use standard titles |
| Acronyms only | "PM" may not match "Project Manager" | Include both forms |
| Passive voice | Weaker keyword association | Use active verbs |
| Vague metrics | "Improved sales" scores lower | Quantify: "Increased sales 47%" |

### Conversion Failures (when converting Markdown to DOCX/PDF)
| Issue | Problem | Solution |
|-------|---------|----------|
| Complex Markdown | Nested lists may not convert cleanly | Keep structure flat |
| Special characters | May corrupt in some parsers | Use standard ASCII |
| Long lines | May wrap poorly | Keep bullets concise |

## Section-Specific Guidance

### Professional Summary (3-5 lines)
- Lead with years of experience + primary domain
- Include top 3-5 keywords from JD
- State value proposition aligned to role
- Mention target role type explicitly

**Template:**
```
[Title] with [X] years of experience in [domain/industry]. 
Expertise in [keyword 1], [keyword 2], and [keyword 3]. 
Proven track record of [quantified achievement aligned to JD]. 
Seeking to leverage [specific skill] to [value proposition for target role].
```

### Experience Section
- Reverse chronological order
- Include: Company, Title, Location, Dates (MM/YYYY - MM/YYYY)
- 3-6 bullets per role (more for recent, fewer for older)
- Start each bullet with action verb
- End each bullet with quantified result

### Skills Section
- Group by category (Technical, Leadership, Domain)
- List keywords exactly as they appear in JD
- Include both acronyms and full terms
- Order by relevance to target role

### Education Section
- Degree, Major, Institution, Year
- Include GPA only if >3.5 and within 5 years
- Relevant coursework only if entry-level
- Certifications can be separate section or here

## Pre-Submission Checklist

1. [ ] Verify keyword match rate >70% against JD
2. [ ] Check Markdown renders correctly in artifact
3. [ ] Confirm clean copy/paste into plain text
4. [ ] Test conversion to DOCX/PDF if needed (Pandoc or online converter)
5. [ ] Verify no formatting artifacts after conversion
