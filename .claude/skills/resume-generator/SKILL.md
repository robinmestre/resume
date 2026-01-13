---
name: resume-generator
description: Generate tailored, ATS-optimized resumes from job descriptions. Use when the user asks to create a resume, tailor a resume for a job, apply to a position, update their CV, or generate application materials. Triggers include phrases like "tailor my resume for", "I'm applying to", "generate resume for this JD", "update my resume", or "help me apply to". Produces Markdown output rendered as an artifact for easy copy/paste, with keyword optimization, quantified achievements, and format appropriate to target role level (executive, technical, or hybrid).
---

# Resume Generator

Generate tailored, ATS-optimized resumes by matching achievements to job requirements.

## Workflow Overview

```
1. PARSE JOB DESCRIPTION
   └─ Extract: keywords, requirements, culture signals, seniority indicators

2. RETRIEVE CANDIDATE DATA
   └─ Load: career-profile.xml with STAR-formatted activities from experience/

3. MATCH & PRIORITIZE
   └─ Score activities using multi-level tags; rank by relevance

4. GENERATE TAILORED CONTENT
   └─ Convert STAR→CAR for bullets; optimize for ATS; format for role level

5. PRODUCE OUTPUT
   └─ Save to resumes/{company-job-title-slug}/; render artifact

6. LOG APPLICATION
   └─ Update job_applications.xml; capture URL if present in source
```

## Input Requirements

**Required:**
- Job description (pasted text, URL, or attached file)

**From Project Knowledge (experience/ directory):**
- `experience/career-profile.xml` — Full career with STAR-formatted activities, multi-level skill tags, and keywords
- `experience/career-summary.xml` — Condensed version for quick reference and initial JD matching
- `experience/career-positions.xml` — Position-focused extraction for deep activity matching

**XML Structure:**
```xml
<activity id="google-2018-pipeline" type="strategic">
  <situation>Context that created the need...</situation>
  <task>Specific responsibility assigned...</task>
  <action>What was done (power verbs)...</action>
  <result>Quantified outcome with metrics inline...</result>
  <tags>
    <domain ref="value-engineering">
      <skill>TCO analysis</skill>
      <technology>Stratozone</technology>
    </domain>
  </tags>
</activity>
```

**Optional:**
- Target format preference (executive, technical, hybrid)
- Specific activities to emphasize or exclude
- Length constraints

## Step 1: Parse Job Description

Extract and categorize:

| Category | What to Extract |
|----------|-----------------|
| **Hard requirements** | Required skills, certifications, years of experience |
| **Soft requirements** | Preferred qualifications, nice-to-haves |
| **Keywords** | Technical terms, tools, methodologies, frameworks |
| **Culture signals** | Values language, team descriptors, work style indicators |
| **Seniority markers** | Scope indicators, leadership expectations, strategic vs. tactical |
| **Success metrics** | How performance will be measured in role |

Create keyword frequency map for ATS optimization targeting.

## Step 2: Match Activities

For each JD requirement, scan activities in career-profile.xml using multi-level tags:

**XML Tag Hierarchy for Matching:**
```
<tags>
  <domain ref="ai-ml">           ← Match against domain IDs in <expertise> section
    <skill>AI platform...</skill> ← Match specific skill names
    <technology>Gemini</technology> ← Match technology keywords
  </domain>
</tags>
```

**Scoring Criteria:**
- **Direct match (3 points):** JD keyword matches `<technology>` or `<skill>` tag exactly
- **Adjacent match (2 points):** JD keyword matches a related skill in same `<domain>`
- **Contextual match (1 point):** JD keyword matches domain ID or parent expertise tier

**Matching Workflow:**
1. Extract keywords from JD
2. Query activities using XPath-like patterns:
   - `//activity/tags/domain[@ref='ai-ml']` → All AI/ML activities
   - `//activity/tags//skill[contains(.,'platform')]` → Activities with "platform" skill
   - `//activity/result[contains(.,'$')]` → Activities with dollar metrics
3. Score each activity by summing tag matches
4. Use `<keywords>` section in career-profile.xml for keyword synonyms

**Prioritization Rules:**
1. Lead with highest-scored matches
2. Ensure coverage of ALL hard requirements
3. Include soft requirement matches if space permits
4. Balance recency with relevance (prefer recent, but strong older achievements can rank higher)
5. Reference position IDs (e.g., `mcd-2024`, `google-2018`) for grouping by role

## Step 3: Generate Tailored Content

### STAR to CAR Conversion

Activities in career-profile.xml use STAR format. Convert to CAR for resume bullets:

| STAR Element | CAR Mapping | Usage |
|--------------|-------------|-------|
| `<situation>` | **Challenge** (context) | Provides background; rarely appears verbatim in bullet |
| `<task>` | **Challenge** (responsibility) | Combined with situation for context |
| `<action>` | **Action** | Use directly; ensure power verbs |
| `<result>` | **Result** | Use directly; contains inline metrics |

**Bullet Format:**
```
[Action verb] [what was done] to [address challenge], resulting in [quantified result]
```

**Example Conversion:**
```xml
<!-- Source STAR -->
<action>Built comprehensive Global Assessment and Planning Program by consolidating
Stratozone, CloudPhysics, and Velostrata into end-to-end solution...</action>
<result>Generated $1.5B in pipeline within 9 months representing 10X growth from
$150M baseline...</result>
```
```
→ CAR Bullet: Built global assessment program consolidating three migration tools
into unified solution, generating $1.5B pipeline in 9 months (10X growth)
```

See `references/achievement-frameworks.md` for verb lists and quantification patterns.

### ATS Optimization

Apply rules from `references/ats-optimization.md`:
- Mirror exact keyword phrasing from JD
- Place critical keywords in first third of resume
- Use standard section headers
- Avoid tables, graphics, headers/footers
- Maintain 2-4% keyword density for top terms

### Format Selection

| Role Level | Format | Characteristics |
|------------|--------|-----------------|
| **Executive** | Strategic emphasis | Board exposure, P&L, transformation leadership, vision |
| **Technical** | Skills-forward | Tech stack prominence, architecture decisions, scale metrics |
| **Hybrid** | Balanced | Technical depth + business impact + leadership |

## Step 4: Generate Output

**Produce Markdown file rendered as artifact:**

Create the resume as a `.md` file saved to an organized subfolder and provide a rendered artifact for easy copy/paste.

**Output Folder Structure:**

Create a subfolder under `resumes/` using a slug format:
- Folder path: `resumes/{company-job-title-slug}/`
- Slug format: lowercase, hyphens replace spaces and special characters
- Remove apostrophes, consecutive hyphens, leading/trailing hyphens
- Example: "McDonald's" + "AI Strategy Lead" → `resumes/mcdonalds-ai-strategy-lead/`

**Files to Create:**
- `resume.md` — The tailored resume
- `cover-letter.md` — Cover letter (if requested)

**Markdown Formatting:**
- Use `#` for name (H1), `##` for section headers
- Use `**bold**` for company names and job titles
- Use bullet lists (`-`) for achievement bullets
- Use horizontal rules (`---`) between major sections
- Keep formatting clean and portable

**Structure:**
```markdown
# [Full Name]
[Email] | [Phone] | [Location] | [LinkedIn URL]

---

## Professional Summary
[3-5 line summary with top keywords]

---

## Professional Experience

**[Job Title]** | [Company Name] | [Location]
*[Start Date] – [End Date]*

- [Achievement bullet 1]
- [Achievement bullet 2]
- [Achievement bullet 3]

---

## Skills
**[Category 1]:** [Skill 1], [Skill 2], [Skill 3]
**[Category 2]:** [Skill 1], [Skill 2], [Skill 3]

---

## Education
**[Degree]** | [Institution] | [Year]
```

**Artifact Requirements:**
1. Create subfolder `resumes/{company-job-title-slug}/`
2. Save resume as `resume.md` in the subfolder
3. Render as Markdown artifact in conversation for immediate preview
4. User can copy directly from artifact or download file

**Include tailoring summary (in conversation, not in resume):**
- Keywords incorporated and their frequency
- JD requirements matched (with achievement citations)
- Coverage gaps identified (requirements without strong matches)
- Recommendations for strengthening candidacy

## Step 5: Log Application

Track each job application in `job_applications.xml` at the repository root.

**URL Extraction:**

If the job description came from a file in `jobs/`, scan the first 5 and last 5 lines for URLs:
- Look for patterns starting with `https://` or `http://`
- Common job board domains: linkedin.com, indeed.com, greenhouse.io, lever.co, workday.com
- Capture the first valid URL found

**XML Log Structure:**

Create or update `job_applications.xml` in the repository root:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<job_applications>
  <application>
    <company>Google</company>
    <job_title>Senior Software Engineer</job_title>
    <applied_at>2026-01-13T14:30:00Z</applied_at>
    <url>https://careers.google.com/jobs/12345</url>
    <resume_path>resumes/google-senior-software-engineer/resume.md</resume_path>
  </application>
</job_applications>
```

**Log Entry Fields:**
- `company` — Company name (as extracted from JD)
- `job_title` — Job title (as extracted from JD)
- `applied_at` — ISO 8601 timestamp when resume was generated
- `url` — Job posting URL (if found in source file, otherwise omit tag)
- `resume_path` — Relative path to the generated resume

**Logging Behavior:**
1. If `job_applications.xml` doesn't exist, create it with XML declaration and root element
2. If it exists, append new `<application>` entry before closing `</job_applications>`
3. Use current timestamp in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)

## Quality Checklist

Before delivering, verify:

- [ ] All hard requirements addressed with specific activities from career-profile.xml
- [ ] Top 10 JD keywords appear in resume (with natural placement)
- [ ] Every bullet follows CAR framework (converted from STAR) with quantified result
- [ ] No orphan bullets (single bullets under a role)
- [ ] Consistent date formatting throughout
- [ ] No first-person pronouns
- [ ] Action verbs vary (no verb used more than twice)
- [ ] Contact information complete (from `<identity>` section in career-profile.xml)
- [ ] Markdown renders cleanly (no broken formatting)
- [ ] Resume saved to `resumes/{company-job-title-slug}/resume.md`
- [ ] Application logged in `job_applications.xml`
- [ ] Artifact rendered in conversation for easy copy/paste

## Reference Files

**Career Data (experience/ directory):**
- `experience/career-profile.xml` — Full career with STAR activities, expertise taxonomy, credentials
- `experience/career-summary.xml` — Condensed version for quick reference
- `experience/career-positions.xml` — Position-focused extraction

**Skill References:**
- `references/ats-optimization.md` — ATS rules, formatting requirements, keyword strategies
- `references/achievement-frameworks.md` — CAR/STAR frameworks, power verbs, quantification patterns

Load career data from experience/ and reference files when generating resume content for detailed guidance.
