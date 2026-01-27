# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Personal career data repository for Robin Mestre containing structured career history, achievements, and five Claude Code skills:
- **resume-generator**: Generates ATS-optimized resumes tailored to job descriptions
- **update-experience**: Adds or updates career experience in XML files with STAR format enforcement
- **linkedin-updater**: Generates LinkedIn profile update instructions with copy-paste content
- **career-fit-assessor**: Red team/blue team career fit assessment against job requirements
- **context-optimizer**: Formats data files for optimal Claude reasoning and extraction

## Repository Structure

```
resume/
├── experience/           # XML-formatted career data (optimized for Claude)
│   ├── career-profile.xml        # Full career with positions, achievements, keywords
│   ├── career-summary.xml        # Condensed version for quick reference
│   ├── career-positions.xml      # Position-focused extraction
│   └── interview-positioning.xml # Interview prep, talking points, vulnerability handling
├── jobs/                 # Job opportunities (text format)
│   └── *.txt                 # Job descriptions to apply for
├── resumes/              # Generated application materials
│   └── {company-job-title}/  # Subfolder per job (slug format)
│       ├── resume.md             # Tailored resume in Markdown
│       └── cover-letter.md       # Cover letter in Markdown
├── linkedin/             # Generated LinkedIn profile updates
│   └── profile-update-{date}.md  # Section-by-section update instructions
├── job_applications.xml  # Application log (auto-generated)
└── .claude/skills/       # Claude Code skills
    ├── resume-generator/     # Resume tailoring skill
    ├── update-experience/    # Career data management skill
    ├── linkedin-updater/     # LinkedIn profile optimization skill
    ├── career-fit-assessor/  # Job fit assessment skill
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

**Four XML Files:**
- `career-profile.xml` (~93KB, ~28K tokens) - Full career data for resume generation
- `career-summary.xml` (~9KB, ~3K tokens) - Quick reference for initial matching
- `career-positions.xml` (~31KB, ~9K tokens) - Position-focused extraction
- `interview-positioning.xml` (~15KB) - Interview prep, talking points, vulnerability handling

## Using the Skills

### Resume Generator

Triggered by phrases like "tailor my resume for", "generate resume for this JD", or "help me apply to".

Workflow:

1. **Knockout screening**: Check for disqualifying factors (missing credentials, experience gaps, location)
2. **Context selection**: User specifies seniority level, function type, and company type to calibrate weighting
3. Parse job description for keywords, requirements, seniority markers
4. Load career data from `experience/career-profile.xml`
5. Match STAR activities using multi-level tags (direct=3, adjacent=2, contextual=1)
6. Convert STAR→CAR for resume bullets (Situation+Task→Challenge, Action→Action, Result→Result)
7. **Above-the-fold optimization**: Place strongest evidence in top third for 7-second recruiter scan
8. **Authenticity verification**: Avoid AI-detection patterns; enforce precise metrics, named projects
9. **LinkedIn consistency alerts**: Flag discrepancies that could trigger recruiter investigation
10. Generate Markdown resume optimized for ATS
11. Save to `resumes/{company-job-title-slug}/resume.md`
12. Log application to `job_applications.xml` with timestamp and URL (if present)

Output organization:

- Subfolder naming: company + job title as lowercase slug (e.g., `google-senior-engineer`)
- URL capture: If job description file contains a URL at start/end, it's logged automatically

Key references:

- `.claude/skills/resume-generator/references/ats-optimization.md` - ATS formatting rules
- `.claude/skills/resume-generator/references/achievement-frameworks.md` - Power verbs, quantification
- `.claude/skills/resume-generator/references/context-profiles.md` - Weight calibration by seniority/function/company type

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

### LinkedIn Updater

Triggered by phrases like "update my LinkedIn", "optimize my LinkedIn profile", "refresh my LinkedIn", or "LinkedIn best practices".

Workflow:

1. Load career data from `experience/career-summary.xml`, `career-profile.xml`, and `interview-positioning.xml`
2. Extract positioning, key metrics, differentiators, and STAR activities
3. Apply LinkedIn best practices (headline formulas, About structure, keyword optimization)
4. Generate section-by-section Markdown with copy-paste content blocks
5. Save to `linkedin/profile-update-{date}.md`

Output format includes:

- **Headline options**: 3 variations using formula `[Role] | [Specialization] | [Quantified Value] | [Key Differentiator]`
- **About section**: 5-part structure (hook, who you help, proof points, philosophy, CTA)
- **Experience bullets**: STAR→CAR conversion for each role
- **Skills ordering**: Tiered approach (Core → Secondary → Long-tail)
- **Featured recommendations**: Certifications, articles, board positions
- **Implementation checklist**: Step-by-step action items

Key reference:

- `.claude/skills/linkedin-updater/references/linkedin-best-practices.md` - Formulas, power verbs, keyword strategy

### Career-Fit-Assessor

Triggered by phrases like "assess this job", "should I apply", "evaluate this role", "career fit assessment", or "red team this opportunity".

Two modes:

- **Quick** (default): BLUF + Red/Blue argument table + Interview prep recommendations
- **Detailed**: Full CSF analysis with weighted scoring + passion alignment assessment

Workflow:

1. Load career data from XML files in `experience/`
2. Parse job description to identify 8-12 Critical Success Factors (CSFs)
3. Run red team/blue team analysis on each CSF (arguments FOR and AGAINST)
4. Calculate fit percentage with confidence level
5. Generate interview prep recommendations (strengths to emphasize, gaps to address)

Output (Quick mode):

- **BLUF**: Fit percentage and confidence level
- **Red/Blue table**: Adversarial arguments for each CSF
- **Interview prep**: Strengths to emphasize, gaps to address, likely questions

Output (Detailed mode):

- Full CSF table with weights (1-10) and fit scores (0-10)
- Weighted fit calculation
- Key assumptions and confidence analysis
- Passion alignment assessment (interest, growth, impact, lifestyle, identity)
- Strategic recommendations with evidence hierarchy

Key reference:

- `.claude/skills/career-fit-assessor/references/detailed-assessment-criteria.md` - CSF methodology, scoring, passion-fit matrix

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

## Data Management

The XML files in `/experience` are the source of truth for all career data. Use the `update-experience` skill to add or modify career data with proper STAR format enforcement.
