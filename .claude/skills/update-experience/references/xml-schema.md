# Career Profile XML Schema Reference

Complete element hierarchy for `experience/career-profile.xml`.

## Root Element

```xml
<career-profile version="1.0" last-updated="YYYY-MM-DD">
```

## Element Hierarchy

```
career-profile
├── identity
│   ├── name
│   ├── current-title
│   ├── current-employer
│   ├── location
│   ├── citizenship
│   ├── contact {phone, email, linkedin}
│   ├── languages {language[@proficiency]}
│   └── career-span[@years]
├── key-metrics
│   └── metric[@id, @value, @context]
├── expertise
│   └── domain[@id, @tier, @years]
│       ├── name
│       ├── skills {skill}
│       └── technologies {tech}
├── positions
│   └── position[@id, @type]
│       ├── company
│       ├── title
│       ├── level
│       ├── location
│       ├── dates[@start, @end]
│       ├── reporting
│       └── initiatives
│           └── initiative[@id]
│               ├── name
│               └── activities
│                   └── activity[@id, @type]
│                       ├── situation
│                       ├── task
│                       ├── action
│                       ├── result
│                       └── tags
│                           └── domain[@ref]
│                               ├── skill
│                               └── technology
├── credentials
│   ├── education {degree}
│   ├── certifications {certification}
│   ├── board-positions {position}
│   ├── speaking {engagement}
│   └── volunteering {activity}
└── keywords
    └── category[@name]
```

## Position Attributes

| Attribute | Values | Description |
|-----------|--------|-------------|
| `id` | `{company-abbrev}-{start-year}` | Unique identifier (e.g., `mcd-2024`, `google-2016`) |
| `type` | `current`, `previous`, `advisory` | Employment status |

## Activity Attributes

| Attribute | Values | Description |
|-----------|--------|-------------|
| `id` | `{position-id}-{year}-{topic}` | Unique identifier (e.g., `mcd-2024-10layer`) |
| `type` | `strategic`, `technical`, `leadership` | Category of achievement |

## Domain Attributes (Expertise)

| Attribute | Values | Description |
|-----------|--------|-------------|
| `id` | slug format | Reference key (e.g., `ai-ml`, `cloud-platforms`) |
| `tier` | `1`, `2`, `3` | Expertise depth (1=10+ yrs, 2=5-10 yrs, 3=2-5 yrs) |
| `years` | `N+` | Years of experience |

## STAR Elements

Each activity contains four required STAR elements:

```xml
<activity id="example-2024-topic" type="strategic">
  <situation>
    Business context or problem that created the need.
    Focus on: gap, opportunity, challenge, or organizational change.
  </situation>
  <task>
    Specific responsibility or assignment given.
    Focus on: what you were asked to do, your role, your ownership.
  </task>
  <action>
    Concrete steps taken to address the task.
    Focus on: power verbs, methods, tools, collaborations, decisions.
  </action>
  <result>
    Quantified outcome with inline metrics.
    Focus on: numbers ($, %, count), business impact, adoption, recognition.
  </result>
  <tags>
    <!-- Reference existing domains from <expertise> section -->
  </tags>
</activity>
```

## Tags Structure

Tags link activities to expertise domains:

```xml
<tags>
  <domain ref="ai-ml">
    <skill>Multi-agent systems</skill>
    <skill>RAG pipelines</skill>
    <technology>Gemini</technology>
    <technology>Claude</technology>
  </domain>
  <domain ref="enterprise-architecture">
    <skill>Architecture governance</skill>
    <technology>TOGAF</technology>
  </domain>
</tags>
```

## Current Domain IDs

### Tier 1 (10+ years)
- `enterprise-architecture` - Target state, operating models, TOGAF
- `cloud-platforms` - GCP, Azure, migration, TCO
- `technology-evangelism` - Presentations, storytelling, demos
- `program-management` - Cross-functional, global programs, training

### Tier 2 (5-10 years)
- `ai-ml` - GenAI, LLMs, agents, RAG, governance
- `value-engineering` - TCO, business cases, ROI
- `sales-enablement` - Training, competitive intel, courses
- `business-development` - C-level, partnerships, deals

### Tier 3 (2-5 years)
- `six-sigma` - Process improvement, root cause, control plans
- `martech-loyalty` - Loyalty programs, CDP, personalization
- `software-development` - Python, C#, React, Firebase

## Credentials Sections

### Education
```xml
<education>
  <degree>
    <name>Bachelor of Commerce (BCom)</name>
    <institution>University of South Africa (UNISA)</institution>
    <year>1996</year>
    <field>Business Management, Industrial Psychology</field>
  </degree>
</education>
```

### Certifications
```xml
<certification>
  <name>Google Cloud Professional Cloud Architect</name>
  <issuer>Google Cloud</issuer>
  <year>2018</year>
</certification>
```

### Speaking Engagements
```xml
<engagement type="external|internal">
  <event>Conference Name</event>
  <year>2024</year>
  <topic>Presentation Topic</topic>
  <metrics>Optional: attendees, rating</metrics>
</engagement>
```

## Key Metrics

Headline numbers for quick reference:

```xml
<metric id="unique-slug" value="$1.5B" context="Description of achievement"/>
```

Current metrics include:
- `ai-use-cases` (325)
- `pipeline-generated` ($1.5B)
- `largest-opportunity` ($3.3B)
- `people-trained` (784+)
- `program-contributors` (88)
- `architecture-artifacts` (45+)
- `internal-investment` ($2.5M)

## XML Formatting Rules

1. **Indentation**: 2 spaces per level
2. **Dates**: ISO format `YYYY-MM` for start/end, `present` for current
3. **IDs**: lowercase, hyphen-separated slugs
4. **Metrics**: Include unit with value (e.g., `$1.5B`, `784+`, `10X`)
5. **Escaping**: Use `&amp;` for `&` in text content
