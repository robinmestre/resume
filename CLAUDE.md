# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Personal career data repository for Robin Mestre containing structured career history, achievements, and three Claude Code skills:
- **resume-generator**: Generates ATS-optimized resumes tailored to job descriptions
- **update-experience**: Adds or updates career experience in XML files with STAR format enforcement
- **context-optimizer**: Formats data files for optimal Claude reasoning and extraction

## Repository Structure

```
resume/
├── experience/           # XML-formatted career data (optimized for Claude)
│   ├── career-profile.xml    # Full career with positions, achievements, keywords
│   ├── career-summary.xml    # Condensed version for quick reference
│   └── career-positions.xml  # Position-focused extraction
├── jobs/                 # Job opportunities (text format)
│   └── *.txt                 # Job descriptions to apply for
├── resumes/              # Generated application materials
│   └── {company-job-title}/  # Subfolder per job (slug format)
│       ├── resume.md             # Tailored resume in Markdown
│       └── cover-letter.md       # Cover letter in Markdown
├── job_applications.xml  # Application log (auto-generated)
└── .claude/skills/       # Claude Code skills
    ├── resume-generator/     # Resume tailoring skill
    ├── update-experience/    # Career data management skill
    └── context-optimizer/    # Context formatting skill
```

## Career Data Format

Career data in `experience/` uses XML optimized for Claude's attention patterns:
- Identity and contact info at TOP (high attention zone)
- Expertise taxonomy with tiered domains (Tier 1: 10+ years, Tier 2: 5-10 years, Tier 3: 2-5 years)
- Quantified key metrics for quick scanning
- Chronological positions with nested initiatives and STAR-formatted activities
- Keywords at END (high attention zone)

**STAR Activity Format:**
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

Reference positions by `id` attribute (e.g., `mcd-2024`, `google-2016`, `microsoft-2006`).

**Three XML Files:**
- `career-profile.xml` (~93KB, ~28K tokens) - Full career data for resume generation
- `career-summary.xml` (~9KB, ~3K tokens) - Quick reference for initial matching
- `career-positions.xml` (~31KB, ~9K tokens) - Position-focused extraction

## Using the Skills

### Resume Generator

Triggered by phrases like "tailor my resume for", "generate resume for this JD", or "help me apply to".

Workflow:
1. Parse job description for keywords, requirements, seniority markers
2. Load career data from `experience/career-profile.xml`
3. Match STAR activities using multi-level tags (direct=3, adjacent=2, contextual=1)
4. Convert STAR→CAR for resume bullets (Situation+Task→Challenge, Action→Action, Result→Result)
5. Generate Markdown resume optimized for ATS
6. Save to `resumes/{company-job-title-slug}/resume.md`
7. Log application to `job_applications.xml` with timestamp and URL (if present)

Output organization:
- Subfolder naming: company + job title as lowercase slug (e.g., `google-senior-engineer`)
- URL capture: If job description file contains a URL at start/end, it's logged automatically

Key references:
- `.claude/skills/resume-generator/references/ats-optimization.md` - ATS formatting rules
- `.claude/skills/resume-generator/references/achievement-frameworks.md` - Power verbs, quantification

### Update Experience

Triggered by phrases like "add experience", "update my career", "I did X at company", or any career data modification request.

Workflow:
1. Parse input to identify update type (new position, activity, credential, etc.)
2. Extract STAR elements from provided text
3. Ask clarifying questions for missing STAR components
4. Generate properly formatted XML with domain tags
5. Update `experience/career-profile.xml`

STAR enforcement:
- **Situation**: Business context or problem
- **Task**: Your specific responsibility
- **Action**: Steps taken (power verbs)
- **Result**: Quantified outcome with metrics

Handles unstructured input by extracting what it can and asking targeted questions to complete STAR requirements.

Key reference:
- `.claude/skills/update-experience/references/xml-schema.md` - Complete XML element hierarchy

### Context Optimizer

Transform data files for optimal Claude reasoning:

```bash
python .claude/skills/context-optimizer/scripts/transform_context.py input.json --format xml --output optimized.xml
python .claude/skills/context-optimizer/scripts/transform_context.py data.csv --format xml --add-metadata
```

Core principle: Claude's attention follows recency gradient (strongest at start/end). Place documents at TOP, queries at END.

## Key Career Metrics

When referencing achievements, these are the headline numbers:
- 325 AI use cases analyzed (McDonald's)
- $1.5B pipeline generated (Google Cloud, 9 months)
- $3.3B largest opportunity identified (Microsoft/Tribune)
- $2.5M internal investment raised (Microsoft partnerships)
- 88 program contributors managed (Google Cloud Industry BA)
- 784+ people trained across programs
- 45+ architecture artifacts created (McDonald's operating model)
- 35+ years career span

## Archive Directory

The `/archive` directory contains the original Markdown source files used to generate the XML. If corrections are needed, update the XML files directly in `/experience` (they are the source of truth for resume generation).
