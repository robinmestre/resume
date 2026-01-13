# Current Role: McDonald's Corporation

**Period:** March 2024 â€“ Present  
**Title:** Principal AI Architect (Generative AI)  
**Level:** Director-equivalent  
**Location:** Chicago, IL  
**Manager:** Reports to Senior Director (Chief Architect) with dotted line to VP (Wei)

---

## Role Overview

Principal Architect initially focused on architecture operating model and MarTech domain architecture. Transitioned to Generative AI Principal Architect role to leverage AI expertise and lead McDonald's enterprise AI platform strategy.

### Primary Responsibilities

- Designing target state architecture for AI across 10 architectural layers
- Developing enterprise AI platform architecture on Google Cloud Platform (GCP)
- Creating agentic architecture patterns using A2A protocol and Model Context Protocol (MCP)
- Architecting multi-agent systems for internal business functions
- Evangelizing AI capabilities across business units
- Collaborating with AI Engineering, Legal (AI counsel), and Business Strategy teams

---

## Major Initiative 1: AI Platform Architecture

### 10-Layer Target State Architecture

Designed and documented comprehensive enterprise AI platform architecture for McDonald's on GCP.

| Layer | Name                           | Description                      | Key Components                                    |
| ----- | ------------------------------ | -------------------------------- | ------------------------------------------------- |
| 1     | **Interface**                  | User-facing interaction layer    | Multi-channel AI experiences, conversational UI   |
| 2     | **Agent Orchestration**        | Agent coordination and routing   | A2A protocols, Gravitee Agent Mesh                |
| 3     | **Agent Runtime**              | Execution environment            | Agent lifecycle, state management                 |
| 4     | **Tools & Functions**          | Reusable capabilities            | MCP integrations, API connectors                  |
| 5     | **Models**                     | Foundation and fine-tuned models | Gemini, Claude, Llama (multi-model strategy)      |
| 6     | **Knowledge & Data**           | Information layer                | RAG pipelines, vector databases, knowledge graphs |
| 7     | **MLOps/AIOps**                | Model operations                 | Lifecycle management, monitoring, versioning      |
| 8     | **Infrastructure**             | Compute resources                | GCP, edge computing, Kubernetes                   |
| 9     | **AI Developer Experience**    | Builder enablement               | SDKs, tooling, templates, documentation           |
| 10    | **Governance & Observability** | Control plane                    | Responsible AI, compliance, audit, FinOps         |

### Three-Platform Model

| Platform                | Scope                                                                    | Key Requirements                                                                       |
| ----------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| **Restaurant Platform** | 40K+ locations globally                                                  | Edge computing, offline capability, 99.99% uptime, IoT (fryers, grills, refrigeration) |
| **Consumer Platform**   | Mobile app, kiosk, web, drive-thru                                       | CDN delivery, auto-scaling, real-time personalization                                  |
| **Company Platform**    | HR, Finance, Legal, IS&P, Supply Chain, Global Impact, EDAA, Global Tech | Internal business functions, Zero Trust access                                         |

### Key Architectural Decisions

| Decision            | Choice                              | Rationale                                        |
| ------------------- | ----------------------------------- | ------------------------------------------------ |
| Primary cloud       | Google Cloud Platform               | Enterprise-wide migration, existing relationship |
| Agent communication | A2A (Agent-to-Agent) protocol       | Standard for inter-agent coordination            |
| Tool integration    | Model Context Protocol (MCP)        | Unified tool and data access pattern             |
| Event streaming     | Confluent Kafka                     | Enterprise scale (millions of orders/day)        |
| Agent management    | Gravitee                            | Agent registry, policy enforcement               |
| Model strategy      | Multi-model (Gemini, Claude, Llama) | Avoid vendor lock-in, best-fit selection         |
| Edge computing      | Mandatory for restaurants           | Internet outages cannot stop operations          |

### Related Deliverables

| Deliverable                                 | Description                                                                                                            |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| AI Opportunities & Challenges Paper         | Comprehensive analysis including conceptual and logical architecture designs; primary input for technical architecture |
| ServiceNow vs. Gemini Enterprise Assessment | System of Action comparison across Interface, Orchestration, Agent Runtime, Tools & Functions, and Models layers       |
| Gravitee Deep Discovery                     | Capabilities assessment for AI agent registry and policy enforcement                                                   |
| Google Collaboration                        | Vetting strategy and approach for Gen AI platform on GCP                                                               |
| AI Engineering Collaboration                | Close work on components for custom AI agents and tools                                                                |
| Legal Counsel Partnership                   | Codifying responsible AI guidelines and governance                                                                     |
| Genpact RFI                                 | Authored RFI to assess AI capabilities in finance domain                                                               |

---

## Major Initiative 2: Business Function AI Strategy

### Strategic Role

Worked closely with McDonald's business strategy team. **Led the technology strategy portion** of the overall AI strategy for McDonald's Corporation.

### AI Megatrends Research

Researched and authored **10 papers on AI megatrends** using AI-assisted research and synthesis:

| #   | Paper                             | Scope                                                |
| --- | --------------------------------- | ---------------------------------------------------- |
| 1   | Global Impact AI Megatrends       | Government relations, communications, sustainability |
| 2   | Global Tech AI Megatrends         | IT infrastructure, development, operations           |
| 3   | EDAA AI Megatrends                | Enterprise data analytics and AI                     |
| 4   | Global Finance AI Megatrends      | Accounting, treasury, FP&A                           |
| 5   | Global IS&P AI Megatrends         | Procurement, sourcing, supplier management           |
| 6   | Global Legal AI Megatrends        | Contracts, compliance, litigation                    |
| 7   | Global Supply Chain AI Megatrends | Logistics, planning, operations                      |
| 8   | Global People AI Megatrends       | HR, talent, learning & development                   |
| 9   | Executive Summary Report          | Cross-functional synthesis for leadership            |
| 10  | Technical Summary Report          | Architecture implications and patterns               |

### Use Case Analysis

| Metric                         | Value   |
| ------------------------------ | ------- |
| Total AI use cases identified  | **325** |
| Business functions analyzed    | **8**   |
| Reusable architecture patterns | **22**  |

**Functions Covered:**

- Global Impact
- Global Tech
- EDAA (Enterprise Data Analytics & AI)
- Global Finance
- Global IS&P (Information Systems & Procurement)
- Global Legal
- Global Supply Chain
- Global People (HR)

### Current Work: Value Stream Mapping

Currently deconstructing and mapping 325 use cases to value streams to:

- Assess buy vs. build decisions
- Identify automation opportunities
- Identify AI decision-support opportunities
- Assess business value AI can provide

---

## Major Initiative 3: Architecture Operating Model

### Framework Development

Established comprehensive architecture operating model following company reorganization.

| Deliverable                      | Count                                        |
| -------------------------------- | -------------------------------------------- |
| Core services defined            | 9                                            |
| Standardized artifacts           | ~45                                          |
| Architecture domains covered     | 5 (Solution, Business, Enterprise, Data, AI) |
| Architect roles defined          | 14                                           |
| Architecture services documented | 12                                           |
| Value streams mapped             | 40                                           |

**Methodologies Applied:**

- Six Sigma (SIPOC)
- SCAMPI/A
- BIZBOK
- TOGAF

### AI-Powered Architecture Agents

Developed AI agents to automate architecture tasks and provide analytical insights:

| Agent                               | Capabilities                                                                                                                                                                                                                                               |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GenAI Architecture Assistant**    | Reviews Gen AI architectures (RAG, agents, fine-tuning, prompts, conversational AI, vision, hybrid). Assesses quality, compliance, cost, readiness. Outputs Confluence reviews with recommendations, risk analysis, production readiness scores.           |
| **Decision Advisor**                | Strategic decision support for enterprise architects. Generates diverse options, performs adversarial analysis, provides calibrated recommendations with confidence ranges. For cloud platforms, AI strategy, architecture patterns, technology selection. |
| **Current State Researcher**        | Deep research via exhaustive Confluence search. Maps findings to 10-layer architecture. Generates baseline reports. Evaluates implementation and readiness status.                                                                                         |
| **Business Architecture Modeler**   | Capability modeling using BIZBOK and TOGAF. Optimized for MarTech domain in QSR industry.                                                                                                                                                                  |
| **Global Program Management Agent** | Executive insights on status and business cases for McDonald's critical projects.                                                                                                                                                                          |

### Thought Leadership Papers

| Paper                                                  | Impact                                                                                                                                              |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Google Distributed Cloud Strategy**                  | Educated teams on GDC Edge capabilities. Defined decision criteria for edge vs. cloud workload placement. Became organizational standard reference. |
| **Business Architecture & Process Engineering for AI** | Applied process engineering to structured analysis of business processes. Identified AI/ML opportunities for business value.                        |
| **AI and Digital Twins**                               | Explored AI + digital twin intersection. Included conceptual architecture for McDonald's implementations.                                           |

---

## Major Initiative 4: MarTech Domain Architecture

### Amazon Loyalty Partnership (Loyalty-Linked Partnerships)

| Activity                         | Description                                                 |
| -------------------------------- | ----------------------------------------------------------- |
| Enterprise architecture strategy | Developed overall EA strategy for partnership               |
| Value streams                    | Built out value streams for loyalty linking                 |
| Capability modeling              | Conducted capability analysis                               |
| Account linking architecture     | **Co-designed** WebView approach for secure account linking |
| Architecture diagrams            | Created high-level enterprise and conceptual diagrams       |
| Sequence diagrams                | Developed account linking flow sequences                    |
| Earn/burn patterns               | Defined cross-platform loyalty integration patterns         |

### Subscription Service Strategy

| Activity                | Description                                                                       |
| ----------------------- | --------------------------------------------------------------------------------- |
| MarTech stack mapping   | Mapped subscription to existing stack (mParticle, Braze, SessionM, Dynamic Yield) |
| Requirements definition | Identified comprehensive functional and non-functional requirements               |
| Vendor assessment       | Assessed **5 vendors** in subscription payment domain                             |
| Feasibility analysis    | Led SME collaboration on **25 subscription constructs** (McKinsey-identified)     |

---

## Major Initiative 5: GCP Champs Training Program

### Program Design

Designed and supported implementation of cloud training program to accelerate GCP adoption and workforce upskilling.

### Results

| Metric                              | Result | Impact                 |
| ----------------------------------- | ------ | ---------------------- |
| Direct participants                 | 154    | â€”                    |
| Certifications passed               | 100    | â€”                    |
| Additional employees pulled through | 166    | **2X** enrollees       |
| Courses enrolled                    | 1,210  | â€”                    |
| Courses completed                   | 732    | **7X** completion rate |
| Labs started                        | 3,288  | â€”                    |
| Labs passed                         | 2,249  | **6X** increase        |

### Recognition

- Program highly praised by CIO
- CIO sought to integrate into broader Tech Academy initiative for Global IT
- Established scalable model for cloud education

---

## Major Initiative 6: Documentation & Communication

### AI Platform Content Hub

Created content hub for communicating AI platform architecture information.

**Design Principles:**

- Progressive disclosure for multiple audiences
- Executive layer: Strategy and business outcomes
- Director layer: Technical strategy and critical components
- Architect layer: Detailed specs and decision records

**Status:** In development

---

## Stakeholder Relationships

| Stakeholder                    | Relationship        | Nature                                           |
| ------------------------------ | ------------------- | ------------------------------------------------ |
| Wei (VP)                       | Strong ally         | Former Google colleague, sponsor for advancement |
| Chief Architect (Sr. Director) | Sponsor             | Secured buy-in for operating model               |
| AI Engineering Team            | Close collaboration | Building AI agent capabilities                   |
| Legal Counsel (AI)             | Close partnership   | Responsible AI governance                        |
| AI Business Strategy Team      | Close collaboration | Tech-business alignment                          |
| Google Cloud                   | External partner    | Platform strategy validation                     |
| CIO                            | Indirect            | Praised GCP Champs program                       |

---

## Keywords for Resume Matching

**AI/ML:** Generative AI, LLM, AI platform, AI architecture, multi-agent systems, agentic AI, RAG, prompt engineering, AI governance, responsible AI, MLOps, AIOps, A2A protocol, MCP, Model Context Protocol

**Cloud:** Google Cloud Platform, GCP, Vertex AI, BigQuery, Cloud Run, Kubernetes, GKE, edge computing, multi-cloud

**Architecture:** Enterprise architecture, solution architecture, AI architecture, business architecture, data architecture, target state architecture, 10-layer architecture, architecture operating model

**Methodology:** Six Sigma, TOGAF, BIZBOK, value engineering, capability modeling, process engineering, SIPOC

**Domain:** QSR, quick service restaurant, MarTech, loyalty, subscription, financial services

**Leadership:** Technology strategy, executive engagement, thought leadership, program management, cross-functional collaboration, vendor assessment

---

## Quantified Achievements Summary

| Achievement                      | Metric                        |
| -------------------------------- | ----------------------------- |
| AI use cases analyzed            | 325                           |
| Business functions covered       | 8                             |
| Architecture patterns identified | 22                            |
| AI megatrend papers authored     | 10                            |
| Architecture layers designed     | 10                            |
| Architecture services defined    | 9                             |
| Standardized artifacts           | ~45                           |
| Architect roles defined          | 14                            |
| Value streams mapped             | 40                            |
| AI agents developed              | 5                             |
| Subscription constructs analyzed | 25                            |
| Subscription vendors assessed    | 5                             |
| GCP Champs participants          | 154 direct + 166 pull-through |
| GCP certifications achieved      | 100                           |
| GCP labs passed                  | 2,249                         |
| GCP courses completed            | 732                           |

---

## Timeline

| Date         | Milestone                                              |
| ------------ | ------------------------------------------------------ |
| March 2024   | Joined McDonald's as Principal Architect               |
| Q2 2024      | Architecture Operating Model established               |
| Q2-Q3 2024   | GCP Champs program execution                           |
| Q3 2024      | MarTech domain architecture (Amazon, Subscription)     |
| Q3-Q4 2024   | AI Platform target state architecture design           |
| Q4 2024      | Business function AI use case analysis (325 use cases) |
| Q4 2024      | AI megatrend papers authored                           |
| Current      | Use case to value stream mapping                       |
| Feb/Mar 2025 | Career checkpoint (bonus payout)                       |

---

# Concurrent: Principio Group (Venture Studio)

**Period:** April 2023 â€“ Present  
**Role:** Founder & Principal  
**Status:** Active (parallel to McDonald's)

## Overview

Venture studio developing AI-powered products for solopreneurs and startups. Reconstituted after leaving Google Cloud to capitalize on generative AI opportunity.

## Ventures

### Agentient

Product development lifecycle platform with AI-powered tools:

| Product | Purpose                          |
| ------- | -------------------------------- |
| Spark   | Ideation and concept development |
| Flow    | Workflow automation              |
| Prism   | Analysis and insights            |
| Vantage | Strategic planning               |
| Foundry | Development tooling              |
| Ignite  | Launch and go-to-market          |
| Academy | Learning and enablement          |

### WaivePath

Sales enablement platform with AI-driven insights and best practices.

| Deliverable            | Count   |
| ---------------------- | ------- |
| Best practices curated | 300-350 |
| Long-form articles     | ~44     |
| Podcasts               | ~44     |
| AI prompt templates    | 50-60   |
| Workshop templates     | 50      |
| Specialized AI agents  | 8       |

**Technical Stack:**

- Frontend: React, Next.js
- Backend: Firebase (Functions, Auth, Storage, Firestore)
- Compute: Google Cloud Run
- AI: Anthropic Claude, Google Gemini
- Payments: Stripe
- Imagery: MidJourney

## Keywords

Startup, venture studio, SaaS, AI agents, product development, Firebase, Cloud Run, solopreneur
