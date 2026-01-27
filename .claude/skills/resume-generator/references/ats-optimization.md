# ATS Optimization Reference

Rules for Applicant Tracking System compatibility, human reviewer psychology, and cross-platform consistency.

## Dual-Audience Reality

Resume must pass TWO distinct evaluations:

| Audience | Evaluation Mode | Optimization Focus |
|----------|-----------------|-------------------|
| **ATS** | Keyword matching, parsing | Exact terms, standard format |
| **Human** | 7-second scan, pattern matching | Placement, authenticity, excitement |

Optimize for both. Sacrificing one for the other fails.

---

## Critical Formatting Rules

### Document Structure (ATS-Critical)
- Single-column layout ONLY
- Standard section headers (see below)
- No tables, graphics, text boxes
- No headers/footers with critical info
- Clean Markdown hierarchy

### Standard Section Headers
**Use these exact headers** (ATS recognition):
- Professional Summary / Summary
- Experience / Professional Experience / Work Experience
- Skills / Technical Skills / Core Competencies
- Education
- Certifications

**Never use:**
- "Where I've Made Impact" → use "Experience"
- "What I Bring" → use "Summary"
- "My Toolkit" → use "Skills"

### Parsing-Safe Formatting
| Element | Safe | Risky |
|---------|------|-------|
| Layout | Single column | Two columns, sidebars |
| Lists | Simple bullets | Nested lists, tables |
| Dates | MM/YYYY - MM/YYYY | Quarters, seasons, "to present" |
| Characters | Standard ASCII | Smart quotes, em-dashes, symbols |

---

## Keyword Optimization

### Extraction Strategy
1. Identify repeated terms in JD (frequency = importance)
2. Note EXACT phrasing (match precisely)
3. Capture acronyms AND spelled-out versions
4. Distinguish required vs. preferred

### Placement Priority
1. **Summary section**: Top 3-5 keywords
2. **Skills section**: Technical keywords verbatim
3. **Experience bullets**: Keywords in context
4. **Job titles**: Add equivalent if your title differs

### Keyword Density
- Top keywords: 2-4% (appears 2-4 times per 100 words)
- Supporting keywords: 1-2%
- Avoid stuffing (unnatural repetition backfires with humans)

### Matching Rules
**Exact match required:**
- Technical tools (Kubernetes, not "container orchestration")
- Certifications (AWS Solutions Architect, not "cloud certified")
- Methodologies (Agile, Scrum, SAFe—specific terms)

**Semantic matching acceptable:**
- Soft skills (led teams ≈ leadership ≈ team management)
- Business outcomes (revenue growth ≈ increased sales)

---

## Above-the-Fold Placement (Human-Critical)

### The 7-Second Scan Reality
Recruiters spend 6-7 seconds on initial scan. 80% of viewing time on:
- Name
- Current title/company
- Previous title/company  
- Dates
- Education (for early-career)

### High-Attention Zones
```
┌─────────────────────────────────────────┐
│ ████████████ HIGH ATTENTION ███████████│ ← Name, title
│ ██████████ HIGH ATTENTION ██████████   │ ← Summary, current role
│ ██████ MEDIUM ██████                   │ ← Recent achievements
│ ████ LOW ████                          │ ← Older roles
│ ██ MINIMAL ██                          │ ← Bottom content
└─────────────────────────────────────────┘
```

### Placement Rules
- Strongest achievement → First bullet of current role
- Top keywords → Summary section
- Critical qualifications → Visible without scrolling
- If best achievements are old → Promote to summary highlights

---

## LinkedIn Consistency Check

### Why This Matters
Recruiters routinely cross-check resume against LinkedIn. Discrepancies trigger:
- Investigation (best case)
- Immediate rejection (common case)
- Credibility damage for interview (worst case)

### Must Match Exactly
| Element | Requirement |
|---------|-------------|
| Job titles | Identical or explained |
| Company names | Identical spelling |
| Employment dates | Same month/year |
| Education | Same credentials |

### Acceptable Variation
- Resume MORE detailed than LinkedIn (more bullets)
- Resume MORE tailored (role-specific keywords)
- Summary can differ (LinkedIn general, resume targeted)

### Red Flags to Avoid
- Different titles for same role
- Dates that don't align (even by 1-2 months)
- Companies on one but not other
- Degree claims that differ

### Post-Tailoring Alert
After heavy tailoring, verify:
```
⚠️ LinkedIn Consistency Check Required:
Before applying, ensure LinkedIn reflects:
- [Title used in resume]
- [Date range used]
- [Any promoted achievements now featured]
```

---

## Employment Gap Handling

### Gap Duration Thresholds
| Gap Length | Action |
|------------|--------|
| <6 months | No action needed—within normal range |
| 6-12 months | Optional brief explanation in cover letter |
| >12 months | Required proactive framing |

### Framing Strategies for Extended Gaps

**Consulting/Freelance Positioning:**
```
Independent Consultant | [Dates]
- [Specific project or client work]
- [Skill maintained or developed]
```

**Skill Development Narrative:**
```
Professional Development | [Dates]
- Completed [certification] in [domain]
- [Course/training] through [institution]
```

**Life Transition (brief, forward-looking):**
```
Career Transition | [Dates]
- [Brief context: caregiving, relocation, health—one line]
- Maintained [skills] through [activity]
```

### What NOT to Do
- Leave extended gap unexplained (recruiter assumes worst)
- Over-explain or apologize
- Use functional resume format (signals hiding something)

---

## Career Transition Handling

### Transferable Skills Mapping
1. Identify JD requirements
2. Map to non-obvious prior experience
3. Make connection EXPLICIT (don't force recruiter to figure it out)

### Transition Framing Patterns
```
"Leveraged [prior skill] to [new application]"
"Applied [domain expertise] to [new context]"
"Translated [previous function] experience into [target function]"
```

### Example: Sales → Product Management
```
❌ Vague: "5 years of sales experience"

✓ Mapped: "5 years gathering customer requirements and translating pain points 
into solution recommendations—now applying to product roadmap decisions"
```

### Format Warning
**Functional resumes signal "hiding something."**
Use reverse-chronological but front-load transferable achievements in summary and top bullets.

---

## Parsing Verification Protocol

### Pre-Submission Checks

**Markdown to Plain Text:**
1. Copy Markdown output to plain text editor
2. Verify no formatting artifacts
3. Verify logical reading order
4. Verify all dates extractable

**If Converting to DOCX/PDF:**
1. Test conversion (Pandoc or online)
2. Verify bullet points render
3. Check bold/italic preserved
4. Confirm headers recognized
5. Verify no orphaned text

### Parsing Confidence Levels

**HIGH Confidence:**
- Single column, standard headers
- MM/YYYY dates, standard bullets
- No tables or graphics

**MEDIUM Confidence:**
- Minor formatting complexity
- Non-standard but clear date formats
- Simple nested structure

**LOW Confidence (Re-format):**
- Multi-column layout
- Tables for content
- Graphics with text
- Dates in headers/footers

---

## Section-Specific Guidance

### Professional Summary (3-5 lines)
```
[Specific identity + scope] + [Top quantified achievement] + 
[Second achievement or expertise] + [Value proposition for THIS role]
```

**Include:**
- Top 3-5 JD keywords (natural placement)
- At least one specific metric
- Connection to target role

**Avoid:**
- Generic templates that could apply to anyone
- "Seeking opportunity to..." (assumed)
- Listing skills without context

### Experience Section
- Reverse chronological
- Format: Company | Title | Location | MM/YYYY - MM/YYYY
- 3-6 bullets per role (more for recent, fewer for old)
- Every bullet: Action verb → Specific contribution → Quantified result

### Skills Section
- Group by category relevant to JD
- List keywords exactly as in JD
- Include both acronyms and full terms
- Order by relevance to target role

### Education Section
- Degree, Major, Institution, Year
- GPA only if >3.5 AND within 5 years
- Coursework only if entry-level
- Certifications: separate section or here

---

## Pre-Submission Checklist

### ATS Compatibility
- [ ] Single-column layout
- [ ] Standard section headers
- [ ] No tables, graphics, text boxes
- [ ] Dates in MM/YYYY format
- [ ] Top 10 JD keywords present

### Human Psychology
- [ ] Strongest achievement visible in 7-second scan
- [ ] Top keywords in summary section
- [ ] No round numbers without at least one precise metric
- [ ] Varied sentence structures

### Cross-Platform Consistency
- [ ] Job titles match LinkedIn
- [ ] Dates match LinkedIn
- [ ] Education matches LinkedIn
- [ ] No claims that contradict public profile

### Parsing Verification
- [ ] Clean copy/paste to plain text
- [ ] Conversion tested if needed
- [ ] Parsing confidence: HIGH
