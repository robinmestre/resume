# Career History: Google Cloud

**Company:** Google Cloud  
**Period:** March 2016 â€“ March 2023  
**Duration:** 7 years  
**Location:** Chicago, IL (Central Region)

---

## Overview

Seven-year tenure at Google Cloud spanning three distinct roles across customer engineering, value engineering, and program management. Progressed from enterprise security evangelism to leading global value engineering strategy to managing large-scale cross-functional enablement programs.

### Role Progression

| Period                | Role                        | Organization         | Focus                                                |
| --------------------- | --------------------------- | -------------------- | ---------------------------------------------------- |
| Mar 2016 â€“ Dec 2017 | Principal Strategic Advisor | Customer Engineering | Enterprise security, C-level engagement              |
| Jan 2018 â€“ Nov 2019 | Head of Value Engineering   | Sales Strategy       | Global value engineering, TCO, migrations            |
| Dec 2019 â€“ Mar 2023 | Principal Program Manager   | Industry Enablement  | Competitive intel, enablement, business architecture |

---

## Career Philosophy at Google Cloud

Approached Google Cloud tenure with an **interdisciplinary problem-solving philosophy** (influenced by John Dewey). Having worked in the Microsoft ecosystem for decades, recognized the value of experiencing different parts of a large organization. Each role transitionâ€”even the difficult onesâ€”was an opportunity to learn another facet of the business and build cross-functional relationships.

---

## Role 1: Principal Strategic Advisor

**Period:** March 2016 â€“ December 2017  
**Organization:** Customer Engineering  
**Manager Level:** Director

### Context

Google Cloud was a nascent organization and new entrant in the enterprise field. The primary challenge was establishing enterprise credibility with Fortune 500 customers accustomed to working with Microsoft and AWS.

**Team Context:** The team was small (~10 people nationally) and somewhat experimental. Manager was field-based and led this "Field CTO" team directly.

### Primary Responsibilities

- Supporting sales teams by conveying technical capabilities to C-level executives
- Developing and delivering enterprise security and compliance messaging
- Managing strategic customer accounts in the Central Region
- Advising startups on Google Cloud architecture

### Key Accounts

| Account                   | Industry                     | Work Performed                                                                                                                                        |
| ------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PayPal**                | Financial Services           | First account; developed and delivered security capabilities briefing to broader audience beyond CISO                                                 |
| **Capital One**           | Financial Services           | Security and compliance presentations                                                                                                                 |
| **HSBC**                  | Financial Services           | Security and compliance presentations                                                                                                                 |
| **Target**                | Retail                       | Security engagement                                                                                                                                   |
| **Best Buy**              | Retail                       | Security engagement                                                                                                                                   |
| **Kohl's**                | Retail                       | Largest Central Region customer; coordinated Kubernetes adoption for mobile backend, catalog search on GCP, Hadoop migration to BigQuery and DataProc |
| **Highland Technologies** | Financial Services (Trading) | Managed critical situation for high-compute customer (125K cores scaling to 450K); resolved Cloud Front End bandwidth constraints                     |

#### Highland Technologies: Deep Technical Case Study

**Context:** Highland Technologies (trading firm) processed algorithmic trades in the cloud. Initially routed traffic between AWS and Google Cloud, but found GCP provided resources more quickly, performed better, and was faster and cheaper. Consequently, routed all trading algorithms to GCP, consuming ~120,000 cores.

**Problem Discovery:**

- Started noticing failures difficult to trace (not appearing meaningfully in logs)
- Concurrent incident: SnapChat (major client) experienced outage and raised high-priority ticket
- Site Reliability Engineers (SREs) reached out after discovering high utilization by Highland Technologies

**Investigation:**

- Gained access to internal behind-the-scenes infrastructure tools through SREs
- Discovered Cloud Front-end Service (routes traffic to/from disk storage for Google Cloud Storage) was being flooded
- Met with client to determine root cause
- **Root cause:** Job sizes were incredibly small; each job wrote outputs to files read by next job; massive I/O from thousands of simultaneous small file operations flooded the CFEs

**Technical Constraints:**

- Cloud Front-end machines were highly optimized hardware
- Hardware Engineering Team didn't have chips needed to create additional machines on short notice
- Critical situation affecting two key customers (Highland + SnapChat)

**Solution Approach:**

1. Conducted detailed analysis of cause, current state, and proposed solutions from client perspective
2. Worked with SREs, product team members, and engineering leadership
3. Collaborated with client to redistribute workloads and reduce I/O demands on individual cloud front-ends

**Outcome:**

- Short-term: Managed load carefully while waiting for hardware
- Long-term: New hardware assembled and deployed
- **Unexpected win:** The workload distribution design proved better than client's original architectureâ€”client stuck with the new distributed design even after capacity was available

### Achievements

| Achievement                              | Details                                                                                                                                           | Keywords                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Enterprise security evangelist**       | Became de-facto security SME; created reusable security messaging                                                                                 | security, compliance, enterprise    |
| **Security specialist team creation**    | Co-developed and presented workshop with product/engineering for hand-selected customer engineers globally; became first security specialist team | training, security, specialist      |
| **External speaking**                    | Presented at RSA Conference, Advisen Risk Management Conference, Rackspace conference                                                             | public speaking, thought leadership |
| **Google Cloud Architect certification** | Earned certification during tenure                                                                                                                | GCP, certification                  |
| **Startup advisory**                     | Advised startups and reviewed architectures on Google Cloud                                                                                       | architecture review, startups       |
| **Fast Magazine article**                | Authored thought leadership on AI, IoT, and productivity integration for optimal working experiences                                              | thought leadership, AI, IoT         |

### Reason for Transition

Organizational restructuring. "Field CTO" team was deprecated when Office of the CTO was formed.

**Full Context:** The reorg was unexpected but understandable. Google Cloud was maturing quickly, and corporate wanted to assume responsibility for this function. The people hired into these roles were former VP executives with deep industry expertise (20+ years). The original team was somewhat experimentalâ€”appreciated that the role was deemed so important that leadership wanted to staff it with the best possible people.

**Personal Response:** Understood the business logic. Required to find new internal role, which led to Value Engineering.

---

## Role 2: Head of Value Engineering

**Period:** January 2018 â€“ November 2019  
**Organization:** Sales Strategy & Operations  
**Scope:** Global

### Context

Value Engineering was a relatively new function at Google Cloud (~18 months old). Predecessor had assessed ~$150M in business through Stratozone partnership. Function needed to scale to support Google Cloud's growth ambitions.

### Primary Responsibilities

- Developing, executing, and scaling global value engineering strategy
- Providing direct deal support for strategic accounts
- Managing ISV partnerships (Stratozone, CloudPhysics)
- Building and leading global assessment and planning program

### Strategic Initiatives

#### Global Assessment & Planning Program

Built comprehensive program by consolidating fragmented initiatives:

| Component    | Source                        | Capability             |
| ------------ | ----------------------------- | ---------------------- |
| Stratozone   | Existing ISV partnership      | TCO assessment         |
| CloudPhysics | Intel partnership (unmanaged) | Asset discovery        |
| Velostrata   | Recent acquisition            | VM migration execution |

**Discovery Story:** Based on experience in previous role, looked for related initiatives across Google that could be consolidated. Found two:

1. **CloudPhysics (Intel Partnership):**

   - Google had partnership with Intel to drive compute adoption through migration assessments
   - Partner team assigned to manage relationship was not effectively managing it (fell outside their core responsibilities)
   - Program wasn't widely adopted; strategy relied on Google Cloud partners who weren't leveraging it
   - Funding paid to partners for assessments wasn't significant enough to drive adoption
   - Partner team was happy to hand off the partnershipâ€”limited resources and unfamiliar territory for them

2. **Velostrata (Acquisition):**
   - Recently acquired company that performed actual VM migrations
   - Had no discovery and assessment capability
   - Natural integration point with Stratozone/CloudPhysics

**Strategic Rationale for Consolidation:**

- Made no sense to have different strategies for migrating VMs
- Collaboration with others who had similar goals was essential given limited resources
- Created end-to-end program: discovery â†’ TCO assessment â†’ planning â†’ migration execution

**Stratozone Contract Negotiation Strategy:**

| Their Incentive                                                                | Our Offer                                            | Outcome                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------ |
| More field adoption = more consulting engagements (where they made real money) | Scale out the program dramatically                   | 10X increase in their business |
| Modules we wanted to license had low uptake (no partners at our scale)         | Take the modules for free                            | Cost them virtually nothing    |
| N/A                                                                            | Reinvest savings into global training and enablement | Funded 20-city training tour   |

**Velostrata Integration:**

- Velostrata was a startup in Israel acquired by Google Cloud in 2018
- Velostrata performed actual VM migrations but had no discovery/assessment capability
- Worked with Stratozone to build integration between tools
- Stratozone: discovery, TCO calculations, planning
- Velostrata: migration execution
- (Note: Was not involved in the Velostrata acquisition)

**Stratozone Acquisition: Direct Involvement**

As the program gained momentum, it caught the attention of the **Group Product Manager (GPM) for Compute** at Google Cloud. He was excited by the results and wanted to provide tooling in the Google Cloud stack to better support VM migrations and supplement Velostrata.

**Why Acquisition vs. Build:**

- Google Cloud Engineering team did not want to develop discovery/assessment capabilities internally
- Had more complex, higher-priority initiatives to work on
- Acquisition was the preferred path

**My Role in Acquisition Decision:**

| Activity              | Details                                                                           |
| --------------------- | --------------------------------------------------------------------------------- |
| **SME consultation**  | GPM approached me as subject matter expert for perspective on acquisition targets |
| **Options evaluated** | CloudPhysics, Stratozone, and other partners                                      |
| **Due diligence**     | Conducted analysis and due diligence on multiple partners                         |
| **Recommendation**    | Recommended Stratozoneâ€”most capable platform, broad enough for enterprise needs |
| **Negotiations**      | Actively participated in meetings and negotiations with Stratozone                |

**Stratozone's Positioning for Acquisition:**

- To strengthen their acquisition case, Stratozone extended their platform to integrate with Velostrata
- This made the combined solution (discovery â†’ assessment â†’ planning â†’ migration) seamless

**Outcome:**

- Stratozone acquired by Google Cloud in 2020
- Product rolled into Google Cloud Platform
- Today known as **Google Cloud Migration Center**

**Program Scope:**

- Asset discovery
- Total Cost of Ownership (TCO) analysis
- VM migration planning
- Migration execution

#### Global Sales Enablement Tour

| Metric              | Value                                                                 |
| ------------------- | --------------------------------------------------------------------- |
| Cities visited      | 20 (Europe, North America, Asia)                                      |
| Sales force trained | ~1/3 of global sales force                                            |
| Training focus      | Stratozone, CloudPhysics for asset discovery, TCO, migration planning |

#### Contract Negotiation

Successfully renegotiated Stratozone contract:

- Secured additional capabilities at no cost
- Reinvested savings into global sales enablement program

### Achievements

| Achievement                       | Metric                                                                                                                              | Keywords                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Pipeline generation**           | $1.5B in 9 months                                                                                                                   | pipeline, revenue, growth                                 |
| **Pipeline growth rate**          | 10X (from ~$150M baseline)                                                                                                          | scale, growth                                             |
| **Forecast accuracy improvement** | 60% improvement                                                                                                                     | forecasting, data-driven                                  |
| **Sales cycle reduction**         | 70% reduction                                                                                                                       | efficiency, sales operations                              |
| **Win rate improvement**          | 5% increase for VM migration                                                                                                        | win rate, competitive                                     |
| **Stratozone acquisition**        | Recommended acquisition target, conducted due diligence, participated in negotiations; product became Google Cloud Migration Center | M&A, acquisition, due diligence, strategic recommendation |

### Strategic Account Engagements

| Account      | Work Performed                                                      |
| ------------ | ------------------------------------------------------------------- |
| **Walmart**  | Business case for TPUs for real-time recommendations on Walmart.com |
| **Pandora**  | Data analysis initiative for song recommendation optimization       |
| **Broadcom** | Defect rate reduction for microchip testing                         |
| **Equifax**  | Business value of cloud security                                    |

### Headcount Expansion Effort

- Built business case for team expansion
- Secured provisional approval from sales strategy & operations
- New sales leadership brought in external value engineering executive
- Decision made to hire more experienced candidates to lead expanded organization

### Reason for Transition

Leadership change resulted in hiring external candidates to lead expanded value engineering organization. Transitioned to Program Management role.

**Full Context:** This transition was a significant disappointment. 10X growth in pipeline ($1.5B in 9 months) is no small featâ€”expected a strong performance review. Instead, found myself being pushed out and replaced.

**Why It Made Business Sense:**

- New hires had 20+ years of value engineering experience specifically
- My experience was limited to a few clients and the Stratozone partnership
- Recognized Google's pattern: plant seeds, experiment with new ideas, then scale up with experienced leaders
- This was the right business decision even though it was personally difficult

**Considered Leaving Google?** Yes. But decided to stay because:

- Opportunity to learn another part of Google (similar to how Microsoft ecosystem experience across multiple roles proved valuable)
- Strong relationships developed from being an early Google Cloud employee
- Google is a compelling brand
- Reputation from Value Engineering results was solid

**How I Found Next Role:**

- Explored opportunities with people I'd worked with previously
- Some roles couldn't work due to level requirements
- Landed position in Competitive Intelligence as a bridge role

**Lessons Learned:**

1. **Think outside the box** to make a difference
2. **Collaboration and partnership** can be very powerful
3. **Accept what you can't control** and move on
4. **Focus on peer partnerships**â€”find people you can trust with mutually beneficial relationships
5. **Stay attuned to external dynamics** that can affect your role and career

**Positive Outcomes:**

- Walked away with strong experience and a meaningful win to be proud of
- Developed excellent relationship with Stratozone CEO and leadership team

---

## Role 3: Principal Program Manager

**Period:** December 2019 â€“ March 2023  
**Organization:** Industry Enablement  
**Scope:** Global

### Context

Transitioned through multiple initiatives within the broader enablement organization, starting with competitive intelligence as a bridge role, then moving to industry enablement and ultimately leading the largest cross-functional program of career.

### Initiative 3.1: Competitive Intelligence

**Period:** November 2019 â€“ Early 2020 (bridge role)

**Why Competitive Intelligence?** This was explicitly a short-term bridge role while seeking a more prominent position. After the Value Engineering transition, explored opportunities with people previously worked with. Some roles couldn't work due to level requirements. Landed in Competitive Intelligence as a stepping stone.

#### Responsibilities

- Research, analyze, and document competitive insights
- Train Googlers and partners on competitive positioning
- Focus areas: Azure, Anthos, infrastructure modernization, application modernization

#### Achievements

| Achievement                       | Details                                                                                                                                       | Keywords                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **AWS re:Invent 2019 synopsis**   | Authored analysis for global sales force                                                                                                      | competitive intelligence, AWS                |
| **Goldman Sachs survey response** | Prepared response for CEO Thomas Kurian and senior leaders                                                                                    | executive communications, investor relations |
| **Azure compute training**        | Created and presented at global sales conference; 500+ attendees; 4.6 average rating                                                          | training, Azure, competitive                 |
| **UIUC AI partnership**           | Led and mentored postgraduate students on competitive analysis AI model using NER, relationship extraction, sentiment analysis, summarization | AI/ML, NLP, university partnership           |

**Transition to Industry Enablement:**

- Wanted to get into sales strategy and operations for greater global impact
- Had a good working relationship with the Industry Enablement manager
- He needed someone to help build the team
- Originally meant as stepping stone to sales strategy, but stayed longer than expectedâ€”so much GTM work to be done
- Still gained valuable sales strategy experience

### Initiative 3.2: Enablement Standardization

**Period:** 2020 (parallel to industry enablement)

#### Problem Statement

- Lack of SME resources for content production
- No standardization in document artifacts and training content
- Reactive engagement (last-minute requests)
- Inefficiencies and redundancies across teams

#### Solution Developed

| Deliverable                | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| **Tiered standards model** | 4 tiers reflecting level of enablement detail required |
| **Document templates**     | 5 standardized templates                               |
| **Course outlines**        | 6 detailed sales and technical course outlines         |
| **AppSheet tracking app**  | Built app to manage and track artifact status          |

#### Best Practices Applied

- Bloom's taxonomy for learning objectives
- Sales cycle stage alignment
- Learner retention assessment guidance

#### Results

- Standards adopted across enablement teams
- Integrated into GTM process for product launches
- Proactive SME engagement (vs. reactive)
- Reduced content pipeline inefficiencies
- Improved stakeholder satisfaction (upstream and downstream)

### Initiative 3.3: Industry Enablement

**Period:** 2020 â€“ 2022

#### Scope

Global Public Sector and Telecommunications sales and customer engineering teams

#### Deliverables Produced

- Sales FAQs
- Quickstart guides
- Sales playbooks
- Event content packages
- On-demand training courses

#### AI-Powered Content Production Innovation

Developed innovative pipeline to address SME scarcity and content staleness:

```
Source Content (videos, webinars, docs)
    â†“
Adobe Premiere (speech-to-text transcription)
    â†“
ChatGPT / Google Bard (narrative synthesis and cleanup)
    â†“
Manual editing (accuracy, current messaging)
    â†“
WaveNet / WellSaid Labs (text-to-speech voiceover)
    â†“
Adobe Audition (audio remastering)
    â†“
Adobe Premiere (final video production)
    â†“
Intellum LMS (modular course deployment)
```

#### Results

| Metric                 | Before    | After   | Improvement    |
| ---------------------- | --------- | ------- | -------------- |
| Course production time | 6-8 weeks | <1 week | ~85% reduction |
| SME time required      | Days      | Hours   | ~90% reduction |

#### DoD JWCC Contract Support

- Assigned to support Joint Warfighting Cloud Capability (JWCC) contract
- Required 11 courses in 2 months over holiday period
- Successfully delivered all 11 courses using AI-powered pipeline

**Learning a New Domain Rapidly: Public Sector/DoD Deep Dive**

**Context:** Public sector/DoD was completely new territoryâ€”had never worked in this space. The JWCC contract had been signed with competitors included, creating high urgency to skill up the team quickly so Google Cloud could work credibly with the DoD. This wasn't just JWCCâ€”the entire team supporting state and local government needed enabling. It was a new team.

**How I Got Up to Speed:**

| Step | Action                                                                                                         |
| ---- | -------------------------------------------------------------------------------------------------------------- |
| 1    | Met with various leaders within the public sector organization to understand strategies and selling approaches |
| 2    | Identified volunteers to collaborate and review content                                                        |
| 3    | Gathered source material: strategy documents, webinars, presentations from leaders                             |
| 4    | Applied AI content pipeline: speech-to-text â†’ LLM synthesis â†’ text-to-speech â†’ video production          |

**Results:**

| Before                                       | After                                |
| -------------------------------------------- | ------------------------------------ |
| Content development timeline: many months    | A few weeks                          |
| Senior executive recording time: significant | Review only (no recording needed)    |
| Content maintenance: difficult               | Easy to update when products changed |

**Recognition:** Put in charge of the entire public sector enablement program by the chief executive hired to handle government affairs globally.

**Key Success Factors:**

- Leveraged existing AI-powered content pipeline developed earlier
- Used existing content from leaders rather than requiring new recordings
- Modular course design enabled rapid assembly
- Reduced burden on senior executives to just review rather than create

### Initiative 3.4: Industry Business Architecture Program

**Period:** 2021 â€“ 2023

#### Context

Digital transformation increasingly owned by business leaders (not IT). Sales teams lacked industry knowledge to engage business executives. Needed to position Google Cloud as trusted partner for strategic business initiatives.

#### Program Scope

**Largest program managed in career** by complexity of deliverables and number of contributors.

| Dimension              | Scale                                                     |
| ---------------------- | --------------------------------------------------------- |
| Total contributors     | 88                                                        |
| Workstream teams       | 10                                                        |
| Cross-functional teams | 3 (Security/Compliance, Partners, Technical Architecture) |
| Industries covered     | 12                                                        |
| Use cases documented   | 6 (reference examples)                                    |

#### Phase 1: Accenture Engagement

3-month consulting engagement to develop initial bill-of-materials for 6 industries:

| Deliverable              | Description                               |
| ------------------------ | ----------------------------------------- |
| Industry trends          | Market and technology trends by industry  |
| Value chains             | End-to-end value chain maps               |
| Business capability maps | Capability models by industry             |
| Metrics                  | KPIs and performance indicators           |
| Maturity models          | High-level capability maturity frameworks |
| Data models              | Logical and conceptual data models        |
| Cloud positioning        | Guidance on positioning GCP throughout    |

#### Phase 2: Field Accessibility

- Created internal website to surface and cross-link content
- Launched at global sales conference
- Called for volunteers; received overwhelming response

#### Phase 3: Content Expansion

**Added Resources:**

- McKinsey persona research (by industry)
- Marketing research company market data
- Expanded from 6 to 12 industries

**Additional Deliverables:**

- Custom user journeys
- Time streams
- Key drivers and performance indicators
- Discovery and qualification questions
- Reference architectures (infrastructure, data, security)
- Implementation roadmaps
- Pricing guidance
- Business value models

#### Phase 4: Cross-Organizational Alignment

Partnered with multiple stakeholders:

| Stakeholder                                                 | Initiative                     | Collaboration                                            |
| ----------------------------------------------------------- | ------------------------------ | -------------------------------------------------------- |
| Principal Architect community lead (Distinguished Engineer) | Complementary methodology      | Joint program sponsorship; she engaged senior leadership |
| Customer Success                                            | Business architecture workshop | Methodology alignment                                    |
| Solution Architecture teams                                 | Solution architecture content  | Downstream integration                                   |
| Infrastructure Architecture teams                           | Migration content              | Downstream integration                                   |
| Professional Services                                       | Delivery methodology           | Process alignment                                        |

**Distinguished Engineer Partnership: Deep Dive**

**Context:** The Distinguished Engineer was responsible for managing principal architects globallyâ€”ensuring they were adequately trained, skilled, and ready to engage major clients on strategic initiatives. She was relatively new to the company.

**How Partnership Formed:**

- Easy to approach because she was new and looking to make impact
- Proposed collaboration so both could achieve more with limited resources
- **Her strengths:** Executive relationships and access
- **My strengths:** Skills and practices for implementing and enabling principal architects

**Division of Labor:**

| Her Focus                                              | My Focus                                                |
| ------------------------------------------------------ | ------------------------------------------------------- |
| Executive-level engagement and messaging               | Managing 88 customer-facing technical roles             |
| Securing priorities and support from leadership        | Building reference architectures for various industries |
| Bringing in principal architects from across functions | Putting processes and infrastructure in place           |

**Collaboration Model:**

- She provided initial high-level outline of what she was trying to achieve
- I elaborated with additional detail and built the operational infrastructure
- Met every 3 weeks to maintain alignment and get her "air cover" support

**Handling Disagreement:**

- One minor disagreement early on: she pushed back on integrating some parts of my existing business architecture work into the final reference architecture
- Resolved by: explaining how it fit into the picture and demonstrating other tools I had created that we could leverage
- She quickly bought in once she saw the value
- That was the only disagreementâ€”partnership ran smoothly thereafter

**Developed unified engagement model** based on design thinking "methods" conceptâ€”documented common activities across all teams in simple, shareable format.

#### Phase 5: Scaling with 20% Project and Volunteer Management

Launched 20% project to recruit Technical Program Managers:

- 10 workstream teams
- 3 cross-functional teams
- Federal program sponsorship for US apprentice (assigned to documentation)

**Managing 88 Contributors Without Direct Authority: Deep Dive**

**Context:** Google Cloud hired top performers, many of whom were fairly new to the company given rapid growth. Being one of the early Google Cloud employees, had developed visibility within certain circles.

**Recruitment Approach:**

- Made a strong pitch at global sales conference when launching the program
- Top performers are always looking for ways to lean in and have more impact
- Called for volunteersâ€”received overwhelming response ("more volunteers than I could manage")

**Managing Volunteer Engagement:**

| Challenge                                                       | Solution                                                                                 |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Volunteers might not follow through due to primary work demands | **Granular tasks:** Broke work into small, manageable pieces                             |
| Unpredictable availability                                      | **Two-week sprints:** If someone was free, they could complete a task and move on        |
| Couldn't manage 88 people directly                              | **10 TPMs:** Organized all contributors under domain-specific Technical Program Managers |
| Horizontal work crossing domains                                | **Influential TPM leads:** Assigned most capable TPMs to cross-domain responsibilities   |

**Recognition and Motivation:**

| Tactic                     | Details                                                                           |
| -------------------------- | --------------------------------------------------------------------------------- |
| **Google peer bonuses**    | Encouraged TPMs to provide peer recognition (included meaningful monetary reward) |
| **Additional recognition** | Personally provided peer bonuses to standout contributors                         |
| **Annual review feedback** | Offered to provide positive feedback for annual reviewsâ€”many took me up on it   |

**Communication Cadence:**

| Frequency     | Activity                                                  |
| ------------- | --------------------------------------------------------- |
| Weekly        | 1:1 meetings with each TPM                                |
| Weekly        | Cross-TPM coordination meeting                            |
| Every 3 weeks | Alignment meeting with Distinguished Engineer (air cover) |
| Regular       | Email updates to all volunteers                           |
| Ongoing       | Website with information and resources                    |

**Conflict Management:**

- Workstreams were quite separate, minimizing conflicts
- Cross-domain work led by most influential TPMs who managed collaboration well
- No significant conflicts arose

#### Phase 6: Level 300 Accreditation Integration

Program became basis for Principal Architect Level 300 accreditation:

- Architects complete building materials for specific use case
- Present to committee including head of Principal Architecture
- Earn Level 300 accreditation upon approval

#### Results

| Achievement                     | Impact                                             |
| ------------------------------- | -------------------------------------------------- |
| Comprehensive bill-of-materials | 6 industries, 6 use cases (reference examples)     |
| Cross-group collaboration       | Unified methodology across previously siloed teams |
| Accreditation integration       | Became key component of Level 300 program          |
| Traffic increase                | **Doubled** traffic to industry enablement content |

### US Apprenticeship Program Sponsorship

Sponsored apprentice through federal partnership program:

- Provided professional development opportunity
- Assigned website maintenance and documentation responsibilities
- Provided performance feedback for annual review

---

## Reason for Leaving Google Cloud

**Event:** Laid off in January 2023 as part of Google's 12,000-employee workforce reduction.

**Context:**

- Role was not deemed essential
- Half of the team was cut in January 2023
- Team was fully dissolved a year later

**Performance at Time of Layoff:**

- Two back-to-back "Exceeds Expectations" ratings
- For this level, "Exceeds Expectations" was a significant achievementâ€”high output was already expected
- Was working nights and weekends to achieve these ratings
- The layoff stung given this track record

**Severance and Transition:**

- Given advance notice
- Very good severance package

**How I Processed It:**

- Layoffs are never easy, especially as a top performer
- However, was excited about the prospects of taking time off
- Saw opportunity to capitalize on the Generative AI wave

**What I Did Next:**

- Reconstituted Principio Group (venture studio)
- Joined forces with former Google colleagues to form WaivePath
- **Key motivation:** When mobile apps became a thing years ago, was late to the game and wished I had caught that wave early. Was not going to let the AI wave pass by.

---

## Keywords for Resume Matching

**Cloud:** Google Cloud Platform, GCP, BigQuery, DataProc, Kubernetes, GKE, Anthos, VM migration, cloud migration, TCO, infrastructure modernization, application modernization, Google Cloud Migration Center

**Value Engineering:** TCO analysis, business case, ROI, pipeline generation, asset discovery, migration planning, Stratozone, CloudPhysics

**Competitive Intelligence:** Azure, AWS, competitive analysis, competitive positioning, market intelligence

**Enablement:** Sales enablement, training, content development, LMS, Intellum, course development, standardization

**Architecture:** Enterprise architecture, business architecture, industry architecture, reference architecture, capability modeling, value chains

**AI/ML:** NLP, NER, relationship extraction, sentiment analysis, speech-to-text, text-to-speech, WaveNet, ChatGPT, Bard

**Program Management:** Global programs, cross-functional, stakeholder management, 20% projects, methodology development

**Executive Engagement:** C-level, CISO, CEO, investor relations, Goldman Sachs

**Security:** Enterprise security, compliance, RSA Conference

**Industries:** Financial services, retail, public sector, telecommunications, DoD, JWCC

---

## Quantified Achievements Summary

| Achievement                       | Metric                         |
| --------------------------------- | ------------------------------ |
| Pipeline generated                | $1.5B in 9 months              |
| Pipeline growth                   | 10X                            |
| Forecast accuracy improvement     | 60%                            |
| Sales cycle reduction             | 70%                            |
| Win rate improvement              | 5%                             |
| Global training tour              | 20 cities, ~1/3 of sales force |
| Competitive intel training        | 500+ attendees, 4.6 rating     |
| Content production time reduction | 6-8 weeks â†’ <1 week          |
| SME time reduction                | Days â†’ Hours                 |
| JWCC courses delivered            | 11 courses in 2 months         |
| Program contributors managed      | 88                             |
| Industries covered                | 12                             |
| Traffic increase                  | 2X to enablement content       |

---

## Timeline

| Date      | Event                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Mar 2016  | Joined as Principal Strategic Advisor                                   |
| 2016      | Google Cloud Architect certification                                    |
| Dec 2017  | Transitioned to Value Engineering (reorg)                               |
| Jan 2018  | Became Head of Value Engineering                                        |
| 2018      | Built global assessment & planning program                              |
| 2018      | Global training tour (20 cities)                                        |
| 2018-2019 | Generated $1.5B pipeline                                                |
| 2020      | Stratozone acquisition completed (became Google Cloud Migration Center) |
| Nov 2019  | Transitioned to Program Management                                      |
| Nov 2019  | Competitive Intelligence (bridge role)                                  |
| 2020      | Industry Enablement & Standardization                                   |
| 2020-2022 | Industry enablement content production                                  |
| 2021-2023 | Industry Business Architecture program                                  |
| Mar 2023  | Left Google Cloud (layoff)                                              |
