# Change Specification Document
**Generated:** 2026-01-14  
**Purpose:** Align career files with interview positioning guidance  
**Status:** PENDING APPROVAL  

---

## Overview

This document specifies changes to three XML files based on coaching session insights captured in `interview-positioning.xml`. Changes focus on:

1. **Builder-Architect Hybrid Positioning** — Elevate hands-on technical work
2. **Stratozone M&A as Headline** — Most durable Google achievement
3. **Language Precision** — Fix "managed" vs "led," "achieved" vs "identified"
4. **Technical Credibility Evidence** — Add deployed agents, coding examples
5. **Honest Reframing** — Tribune as opportunity not outcome

---

## File 1: career-profile.xml

### Change 1.1: McDonald's Agents Activity — Emphasize Production Deployment

**Location:** `<activity id="mcd-2024-agents">`

**Current Text (Result section):**
```xml
<r>Deployed 5 AI agents supporting architecture team productivity. Agents now provide automated architecture reviews, strategic decision support, research synthesis, and program status reporting. Reduced manual effort for architecture assessments by enabling consistent, repeatable analysis.</r>
```

**New Text:**
```xml
<r>Built and deployed 4 AI agents currently running in production supporting architecture team: GenAI Architecture Assistant for compliance scoring, Decision Advisor for strategic analysis, Current State Researcher for baseline reports, and Business Architecture Modeler for capability analysis. Agents provide automated, repeatable analysis that reduced manual architecture assessment effort. Fifth agent (Global Program Management) in development.</r>
```

**Rationale:** Emphasizes "built and deployed" (builder claim) and "running in production" (not paper architecture). Corrects count to 4 deployed + 1 in development. Provides interviewer-ready specificity.

---

### Change 1.2: McDonald's Agents Activity — Update Action to Match

**Location:** `<activity id="mcd-2024-agents">` → `<action>`

**Current Text:**
```xml
<action>Developed 5 specialized AI agents: GenAI Architecture Assistant for reviewing AI architectures with compliance and readiness scoring; Decision Advisor for strategic decision support with adversarial analysis; Current State Researcher for exhaustive Confluence search and baseline reports; Business Architecture Modeler for capability modeling using BIZBOK and TOGAF; Global Program Management Agent for executive insights on critical projects.</action>
```

**New Text:**
```xml
<action>Personally developed 4 specialized AI agents now in production: GenAI Architecture Assistant for reviewing AI architectures with compliance and readiness scoring; Decision Advisor for strategic decision support with adversarial analysis; Current State Researcher for exhaustive Confluence search and baseline reports; Business Architecture Modeler for capability modeling using BIZBOK and TOGAF. Currently building Global Program Management Agent for executive project insights.</action>
```

**Rationale:** "Personally developed" reinforces builder credibility. Clarifies 4 in production, 1 in development.

---

### Change 1.3: Google Value Engineering — Elevate Stratozone Acquisition

**Location:** `<activity id="google-2018-stratozone">`

**Current Title (implicit in situation):**
```xml
<situation>Google Cloud Engineering did not want to develop discovery/assessment capabilities internally. Group Product Manager for Compute wanted tooling to support VM migrations and supplement Velostrata. Acquisition was preferred path over internal development.</situation>
```

**New Text:**
```xml
<situation>Google Cloud Engineering preferred acquiring discovery/assessment capabilities rather than building internally. Group Product Manager for Compute needed tooling to support VM migrations. Multiple acquisition candidates existed (CloudPhysics, Stratozone) requiring technical evaluation and strategic recommendation.</situation>
```

**Rationale:** Sets up acquisition story more clearly. Positions Robin as evaluator, not just observer.

---

### Change 1.4: Google Stratozone — Strengthen SME Role Language

**Location:** `<activity id="google-2018-stratozone">` → `<action>`

**Current Text:**
```xml
<action>Served as SME for GPM evaluating acquisition options including CloudPhysics and Stratozone. Conducted analysis and due diligence on multiple partners. Recommended Stratozone as most capable platform with breadth for enterprise needs. Actively participated in meetings and negotiations with Stratozone leadership. Maintained strong relationship with Stratozone CEO throughout process.</action>
```

**New Text:**
```xml
<action>Served as subject matter expert advising Group Product Manager on acquisition candidates. Conducted build-vs-buy analysis and technical due diligence comparing CloudPhysics and Stratozone capabilities. Authored recommendation for Stratozone based on enterprise breadth and integration potential with Velostrata. Participated in vendor negotiations alongside GPM. Maintained direct relationship with Stratozone CEO that facilitated deal progression.</action>
```

**Rationale:** Adds "build-vs-buy analysis" (defensible claim from interview-positioning.xml). Makes contribution clearer without overclaiming.

---

### Change 1.5: Google Stratozone — Update Result for Durability

**Location:** `<activity id="google-2018-stratozone">` → `<r>`

**Current Text:**
```xml
<r>Stratozone acquired by Google Cloud in 2020 based on recommendation and due diligence. Product rolled into Google Cloud Platform and became Google Cloud Migration Center. Created seamless discovery to migration solution through Stratozone-Velostrata integration.</r>
```

**New Text:**
```xml
<r>Stratozone acquired by Google Cloud (2020). Recommendation contributed to acquisition decision. Product became Google Cloud Migration Center—still in production today. Created seamless discovery-to-migration solution through Stratozone-Velostrata integration. Key proof point: "I build things that last even when my role doesn't."</r>
```

**Rationale:** Adds "still in production today" to emphasize durability. Includes interviewer talking point. Softens "based on" to "contributed to" for honesty.

---

### Change 1.6: Google IBA Program — "Led" Not "Managed"

**Location:** `<activity id="google-2021-iba-program">` → `<r>`

**Current Text:**
```xml
<r>Delivered comprehensive business architecture content for 12 industries with 6 reference use cases. Managed 88 contributors without direct authority using granular tasks, two-week sprints, and peer recognition. Doubled traffic to industry enablement content. Program became basis for Principal Architect Level 300 accreditation. Unified methodology adopted across previously siloed teams.</r>
```

**New Text:**
```xml
<r>Delivered comprehensive business architecture content for 12 industries with 6 reference use cases. Led 88 contributors across 10 workstreams without direct authority—coordinated through granular task breakdown, two-week sprints, and peer recognition. Doubled traffic to industry enablement content. Program became basis for Principal Architect Level 300 accreditation standard (still in use). Unified methodology adopted across previously siloed teams.</r>
```

**Rationale:** Changes "Managed" to "Led" (no direct reports). Adds "(still in use)" for durability claim. Adds workstream count for specificity.

---

### Change 1.7: Tribune Activity — Honest Opportunity vs. Outcome

**Location:** `<activity id="microsoft-2011-tribune-tablet">` → `<r>`

**Current Text:**
```xml
<r>Identified $3.3B opportunity (11M subscribers at $300 BOM for tablet devices). Connected Tribune with Windows product team, OEM/ODM team for hardware, and Microsoft Advertising for ad inventory. Lost Windows tablet deal due to Windows tablet performance but won major Azure deal and advertising partnership. Recognized with Gold Club Nomination (2012), three consecutive Top Contributor Awards, and MGX Best in Class Field Execution (2013).</r>
```

**New Text:**
```xml
<r>Identified $3.3B market opportunity (11M Tribune subscribers × $300 tablet BOM). Capability demonstration led to CEO access within one week of initial EVP meeting. Connected Tribune with Windows, OEM/ODM, and Advertising teams. Windows tablet deal lost due to platform performance, but relationship yielded Azure Content Cloud deal ($1.5M annual savings) and advertising partnership. Recognition: Gold Club Nomination (2012), three consecutive Top Contributor Awards, MGX Best in Class Field Execution (2013).</r>
```

**Rationale:** Clarifies "opportunity" not "deal." Adds CEO access speed as proof point. Links to Azure win as actual outcome.

---

### Change 1.8: Scripps/Food Network — Emphasize Coding Contribution

**Location:** `<activity id="microsoft-2012-scripps">` → `<action>`

**Current Text:**
```xml
<action>Secured speaking slot at executive briefing. Met with COO Mark Hale who was supportive but deferred to brand managers. COO arranged meeting with CEO Ken Lowe at CES Las Vegas. Secured CEO support for Food Network app on Windows/Windows Phone. Faced timeline pressure with only few months to deliver and insufficient developer resources. Personally wrote much of Windows 8 application in C# with Windows libraries alongside technical evangelist colleague. Learned new Windows Runtime (WinRT) platform while delivering under deadline.</action>
```

**New Text:**
```xml
<action>Secured speaking slot at executive briefing. Met COO who arranged CEO meeting at CES Las Vegas. Secured CEO support for Food Network app on Windows/Windows Phone. Faced timeline pressure with months to deliver and insufficient developer resources. Personally coded significant portions of Windows 8 application in C# using WinRT APIs—learned new platform while delivering under deadline. Collaborated with technical evangelist colleague on architecture and remaining components.</action>
```

**Rationale:** "Personally coded" is stronger than "personally wrote." Adds "WinRT APIs" for technical specificity. Reinforces builder-architect hybrid positioning.

---

### Change 1.9: Principio/Agentient — Add MCP Integration Detail

**Location:** `<activity id="principio-2024-agentient">` → `<action>`

**Current Text:**
```xml
<action>Designed 7-module product suite (Spark, Flow, Prism, Vantage, Foundry, Ignite, Academy) covering ideation, prompt management, research, value engineering, requirements, GTM, and training. Architected technical stack using React/Next.js, Firebase, Cloud Run, Agent Development Kit, RAG Engine, and semantic search. Conducted market validation through secondary research and startup founder interviews. Adopted MVP release approach based on WaivePath learnings.</action>
```

**New Text:**
```xml
<action>Designed 7-module product suite (Spark, Flow, Prism, Vantage, Foundry, Ignite, Academy) covering ideation, prompt management, research, value engineering, requirements, GTM, and training. Architected and am personally building technical stack: React/Next.js frontend, Firebase backend, Cloud Run for compute, MCP (Model Context Protocol) for tool integration, and RAG pipeline for knowledge retrieval. Implemented custom MCP servers connecting Claude to Notion, filesystem, and sequential reasoning tools. Applied MVP approach based on WaivePath market validation learnings.</action>
```

**Rationale:** Adds "personally building" (builder credibility). Adds MCP specifics with concrete tool examples. Shows same protocols used at McDonald's appearing in personal work.

---

### Change 1.10: Update Key Metrics Context for Tribune

**Location:** `<key-metrics>` → `<metric id="largest-opportunity">`

**Current Text:**
```xml
<metric id="largest-opportunity" value="$3.3B" context="Microsoft/Tribune tablet initiative"/>
```

**New Text:**
```xml
<metric id="largest-opportunity" value="$3.3B" context="Microsoft/Tribune tablet opportunity (identified, not closed)"/>
```

**Rationale:** Honest framing prevents interview stumble.

---

## File 2: career-summary.xml

### Change 2.1: Update Headline Positioning

**Location:** After `<identity>` section, add new element

**Add New Element:**
```xml
<!-- POSITIONING: Builder-Architect Hybrid -->
<positioning>
  <headline>AI leader who builds strategy AND the platforms to execute it</headline>
  <differentiators>
    <diff>Architect who codes: 4 McDonald's agents in production, WaivePath 8-agent system, Food Network Windows 8 app</diff>
    <diff>Zero-to-one builder: Stratozone became Migration Center, Value Engineering 10X growth, accreditation standards still in use</diff>
    <diff>Rapid executive engagement: Tribune CEO access in 1 week, AON competitive win, McDonald's CIO/VP adoption</diff>
  </differentiators>
</positioning>
```

**Rationale:** Provides quick-reference positioning for resume generation. Surfaces key differentiators upfront.

---

### Change 2.2: Update Google Position Highlights — Stratozone First

**Location:** `<position id="google-2018">`

**Current Text:**
```xml
<highlights>$1.5B pipeline in 9 months, 10X growth, Stratozone acquisition</highlights>
```

**New Text:**
```xml
<highlights>Stratozone acquisition (now Migration Center), $1.5B pipeline in 9 months (10X growth)</highlights>
```

**Rationale:** Leads with most durable achievement. Adds "now Migration Center" for interviewer context.

---

### Change 2.3: Update Microsoft 2008 Position Highlights

**Location:** `<position id="microsoft-2008">`

**Current Text:**
```xml
<highlights>$3.3B Tribune opportunity, AON competitive win, $1.5M Azure savings</highlights>
```

**New Text:**
```xml
<highlights>$3.3B Tribune opportunity identified (led to Azure win), AON competitive win vs Google, $1.5M Azure savings</highlights>
```

**Rationale:** Clarifies Tribune was opportunity leading to actual win. Specifies AON was against Google.

---

### Change 2.4: Update Tribune Metric Context

**Location:** `<key-metrics>` → Tribune metric

**Current Text:**
```xml
<metric id="largest-opportunity" value="$3.3B" context="Microsoft/Tribune tablet initiative"/>
```

**New Text:**
```xml
<metric id="largest-opportunity" value="$3.3B" context="Microsoft/Tribune opportunity (capability demo led to Azure win)"/>
```

**Rationale:** Honest framing with connection to actual outcome.

---

## File 3: career-positions.xml

### Change 3.1: McDonald's Agents — Mirror Profile Changes

**Location:** `<activity id="mcd-2024-agents">`

**Current Text:**
```xml
<action>Developed 5 specialized AI agents: GenAI Architecture Assistant, Decision Advisor, Current State Researcher, Business Architecture Modeler, Global Program Management Agent.</action>
<r>Deployed 5 AI agents supporting architecture team. Reduced manual effort for assessments with consistent, repeatable analysis.</r>
```

**New Text:**
```xml
<action>Personally developed 4 specialized AI agents now in production: GenAI Architecture Assistant, Decision Advisor, Current State Researcher, Business Architecture Modeler. Currently building Global Program Management Agent.</action>
<r>Built and deployed 4 AI agents running in production. Agents provide automated, repeatable analysis reducing manual architecture assessment effort. Fifth agent in development.</r>
```

**Rationale:** Consistency with profile changes.

---

### Change 3.2: Google Stratozone — Mirror Profile Changes

**Location:** `<activity id="google-2018-stratozone">`

**Current Text:**
```xml
<action>Served as SME evaluating CloudPhysics and Stratozone. Conducted analysis and due diligence. Recommended Stratozone. Participated in negotiations.</action>
<r>Stratozone acquired by Google Cloud (2020). Became Google Cloud Migration Center. Created seamless discovery-to-migration solution.</r>
```

**New Text:**
```xml
<action>Served as SME advising GPM on acquisition candidates. Conducted build-vs-buy analysis and technical due diligence. Authored recommendation for Stratozone. Participated in vendor negotiations. Maintained CEO relationship facilitating deal.</action>
<r>Stratozone acquired by Google Cloud (2020). Recommendation contributed to decision. Became Google Cloud Migration Center—still in production today. Created seamless discovery-to-migration solution.</r>
```

**Rationale:** Consistency with profile changes.

---

### Change 3.3: Google IBA — Mirror Profile Changes

**Location:** `<activity id="google-2021-iba-program">`

**Current Text:**
```xml
<r>Delivered content for 12 industries with 6 use cases. Managed 88 contributors without direct authority. Doubled traffic to enablement content. Became basis for Level 300 accreditation.</r>
```

**New Text:**
```xml
<r>Delivered content for 12 industries with 6 use cases. Led 88 contributors across 10 workstreams without direct authority. Doubled traffic to enablement content. Became basis for Level 300 accreditation standard (still in use).</r>
```

**Rationale:** Consistency with profile changes.

---

### Change 3.4: Tribune Tablet — Mirror Profile Changes

**Location:** `<activity id="microsoft-2011-tribune-tablet">`

**Current Text:**
```xml
<r>Identified $3.3B opportunity (11M subscribers x $300 BOM). Connected Tribune with Windows, OEM/ODM, Advertising teams. Won Azure deal and advertising partnership. Gold Club, Top Contributor, MGX Best in Class recognition.</r>
```

**New Text:**
```xml
<r>Identified $3.3B market opportunity (11M subscribers × $300 BOM). Capability demo led to CEO access within 1 week. Windows tablet lost to platform issues, but relationship yielded Azure Content Cloud deal ($1.5M savings). Recognition: Gold Club, 3x Top Contributor, MGX Best in Class.</r>
```

**Rationale:** Consistency with profile changes.

---

### Change 3.5: Scripps/Food Network — Mirror Profile Changes

**Location:** `<activity id="microsoft-2012-scripps">`

**Current Text:**
```xml
<action>Secured executive briefing. Met COO then CEO at CES. Secured CEO support for Food Network app. Personally wrote much of Windows 8 app in C# alongside technical evangelist.</action>
```

**New Text:**
```xml
<action>Secured executive briefing. Met COO then CEO at CES. Secured CEO support for Food Network app. Personally coded significant portions of Windows 8 app in C# using WinRT APIs—learned platform while delivering under deadline.</action>
```

**Rationale:** Consistency with profile changes.

---

### Change 3.6: Agentient — Mirror Profile Changes

**Location:** `<activity id="principio-2024-agentient">`

**Current Text:**
```xml
<action>Designed 7-module suite (Spark, Flow, Prism, Vantage, Foundry, Ignite, Academy). Architected stack (React/Next.js, Firebase, Cloud Run, ADK, RAG). Conducted founder interviews.</action>
```

**New Text:**
```xml
<action>Designed 7-module suite. Personally building stack: React/Next.js, Firebase, Cloud Run, MCP for tool integration, RAG pipeline. Implemented custom MCP servers connecting Claude to Notion and filesystem. Applied MVP approach from WaivePath learnings.</action>
```

**Rationale:** Consistency with profile changes.

---

## Summary of Changes

| File | Changes | Impact |
|------|---------|--------|
| career-profile.xml | 10 changes | Major — positioning, language, technical depth |
| career-summary.xml | 4 changes | Medium — positioning section, highlight order |
| career-positions.xml | 6 changes | Medium — consistency sync with profile |

---

## Approval Workflow

**Option A: Approve All**
Reply "approve all" and I'll execute all 20 changes.

**Option B: Approve with Exceptions**
Reply with specific change IDs to exclude (e.g., "approve all except 1.5 and 2.1").

**Option C: Review First**
Reply "show me [change ID]" to see the exact file diff for any specific change.

**Option D: Reject**
Reply "reject" with feedback to revise the specification.

---

*This document was generated based on coaching session insights. Changes prioritize honest, defensible positioning while strengthening builder-architect narrative.*
