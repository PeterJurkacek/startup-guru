---
marp: true
theme: gaia
class: invert
paginate: true
---

<!-- _paginate: skip -->
# AI Demystified
## A Framework for Legal Minds

![bg right:40%](img/mascot/AID_5.svg)

---

# AI Demystified
A practical framework to decipher AI buzzwords and understand what artificial intelligence really is — and isn't.

### Speaker: Peter Jurkáček, CTO

<!-- Greetings, I'm PJ, a CTO. I have a Master's degree in Computer Science and Artificial Intelligence from the Slovak University of Technology in Bratislava. I have five years of experience working as a full-stack developer and a full-stack data scientist. Now, I lead technology strategy and innovation as CTO at AI:Dental — a company building AI for dentistry. Today I'm here to give you a practical toolkit for understanding AI from a legal perspective. -->

---

## Agenda
- What is Artificial Intelligence (AI)?
- AI tasks in the legal domain
- Process of creating intelligence
- The AI Buzzword Decoder
- Will AI replace lawyers?
- AI Regulation: Why lawyers matter

![bg right:40%](img/mascot/AID_14.svg)

---

# What is **AI**?

![bg left](img/mascot/AID_1.svg)

*Artificial Intelligence (AI) is the **simulation of human intelligence processes** by computer systems.*

---

## Human intelligence processes in law?
**Legal professional**, experienced in reviewing contracts and identifying risky clauses

<!-- Think of a senior lawyer who has reviewed thousands of contracts. They can quickly spot problematic terms, missing protections, and non-standard language. That's human intelligence at work — pattern recognition built from experience. -->

---

## Simulation of Human Intelligence processes?
~~Legal professional~~ **Artificial intelligence**, experienced in reviewing contracts and identifying risky clauses

<!-- Now replace the lawyer with a computer algorithm trained on thousands of reviewed contracts. It has "learned" from examples what risky clauses look like — that's the simulation of human intelligence. -->

---

<!-- 
Differentiating Human Intelligence and Artificial Intelligence 
-->
## Human intelligence
* A **Human** with ability to learn from experiences **to solve different tasks**

## Artificial intelligence
> * An **Algorithm** with ability to learn from experiences
**to solve different tasks** without being explicitly programmed

---

## AI Tasks in the Legal Domain
### Natural language processing (NLP)
- Contract analysis, Legal research chatbot, Document summarization

### Computer vision
- Document scanning & OCR, Signature verification

### Predictive analytics
- Case outcome prediction, Litigation risk assessment

### Multimodal
- Case similarity search

---

<!-- _header: Natural language processing task -->
## T01: Document Analysis
- Input: Scanned contract (PDF/image)
- > Algorithm: OCR + NLP pipeline
- Output: **Extracted clauses**, key terms, parties, dates, obligations

<!-- OCR (Optical Character Recognition) converts images of text into machine-readable text. NLP then processes that text to identify and categorize the important elements. This is how AI can process thousands of documents that would take a legal team weeks. -->

---

<!-- _header: Natural language processing task -->
## T02: Contract Review — Flag Risky Clauses

- Input: Contract text
- > Algorithm: Text classifier (e.g. BERT, Legal-BERT)
- Output: **Flagged clauses** with risk category
  - *e.g. "Unlimited liability clause detected — HIGH RISK"*

<!-- BERT is a language model pre-trained on massive text corpora. Legal-BERT is a variant fine-tuned on legal text. The classifier learns from thousands of human-reviewed contracts what patterns indicate risk. -->

---

<!-- _header: Natural language processing task -->
## T03: Legal Research Chatbot
- Input: Legal question
  *"What are the key precedents on data breach liability under GDPR in the healthcare sector?"*
- > Algorithm:
  > - LLM (e.g. GPT, Gemini)
  > - RAG (Retrieval-Augmented Generation)
- Output: Relevant case law, statutes, and analysis

<!-- RAG means the AI first retrieves relevant documents from a legal database, then generates an answer grounded in those documents. This reduces hallucination — the tendency of LLMs to make things up. -->

---

<!-- _header: Predictive analytics task -->
## T04: Case Outcome Prediction
- Input: Case facts, jurisdiction, legal area
- > Algorithm: Classifier trained on historical case data
- Output: **Predicted outcome probability**
  - *e.g. "72% likelihood of ruling in favor of plaintiff"*

### Ethical caveat
- Predictions reflect **historical bias**, not justice
- Never a substitute for legal judgment

---

<!-- _header: Multimodal task -->
## T05: Case Similarity Search

- Input: Case description or legal brief (text)
- > Algorithm:
  > - Text encoder (e.g. Legal-BERT)
  > - Projection function for similarity matching
- Output: **Most similar precedent cases** ranked by relevance

<!-- This is the same technology behind search engines, but specialized for legal text. It encodes the meaning of a case into a mathematical representation and finds the closest matches in a database. -->

---

# But how can we create those AIs?

---

## Process of creating an AI
- Task Definition:
  * Identifying the objectives and goals of the AI system learning process
- Learning process:
  * Supervised / Self-supervised / Unsupervised / Reinforcement
  * Prepare dataset
  * Development of training procedure
- Performance evaluation:
  * Performance metrics definition
  * Development of testing procedure

---

## Process of creating AI
- Task Definition:
  * T02 Classify risky clauses in contracts
- Learning process:
  * Prepare dataset: 1000 labeled contracts (text + lawyer annotations)
  * Training procedure: Supervised learning
- Performance evaluation:
  * Performance metrics: Precision, Recall, F1-score
  * Testing procedure: Compare AI on 100 test contracts (text + lawyer annotations)

---

## Process of creating AI
- Task Definition:
  * T05 Search for relevant precedent cases
- Learning process:
  * Contrastive learning
  * Prepare dataset: 10,000 case summaries (text + citations)
  * Training procedure: Contrastive learning
- Performance evaluation:
  * Performance metrics: Precision, Recall, F1-score
  * Testing procedure: Compare AI on 500 test queries (query + expected results)

---

# What about creating Human Intelligence?

---

## Process of creating Human Intelligence
- Task Definition:
  * T02 Classify risky clauses in contracts
- Learning process:
  * Prepare dataset: Case studies, textbooks, contract templates
  * Training procedure: Law school lectures, moot courts, internships
    - Supervised learning (by professors and mentors)
- Performance evaluation:
  * Performance metrics: Accuracy, completeness, reasoning quality
  * Testing procedure: Bar exam, practical assessments, peer review

---

## The Parallel

| | **AI** | **Lawyer** |
|---|---|---|
| **Data** | Labeled contracts | Case studies & textbooks |
| **Training** | Algorithm optimization | Law school & practice |
| **Evaluation** | Test dataset & metrics | Bar exam & peer review |
| **Experience** | More data = better | More cases = better |

Both humans and AI need **data**, **practice**, and **evaluation**.
The framework is identical — the medium is different.

---

# The AI Buzzword Decoder

![bg right:40%](img/mascot/AID_4.svg)

<!-- This is the most important section for your future career. Every AI product, every startup pitch, every policy paper will throw AI terminology at you. Here's how to cut through it. -->

---

## 3 Questions to Decode Any AI Claim

### 1. What is the **task**?
*What exactly is the AI supposed to do?*

### 2. What **data** was it trained on?
*How much? How representative? How recent? Who labeled it?*

### 3. How was it **evaluated**?
*On what test set? By whom? What metrics? Published or self-reported?*

> If any answer is **missing or vague** — be skeptical.

---

## Buzzword Glossary

| Buzzword | Plain English |
|---|---|
| **Machine Learning** | Algorithm that learns patterns from data |
| **Deep Learning** | Machine learning using many-layered neural networks |
| **Neural Network** | Algorithm loosely inspired by the brain's structure |
| **LLM** | Large Language Model — AI trained on massive text to generate language |
| **GPT** | A specific family of LLMs by OpenAI |
| **RAG** | Retrieval-Augmented Generation — AI that looks up sources before answering |
| **Hallucination** | When AI confidently generates false information |
| **Training Data** | The examples an AI learned from |
| **Fine-tuning** | Adapting a general AI to a specific domain |
| **Bias** | Systematic error from unrepresentative data or design |

---

## Applying the Decoder

**Claim:** *"Our AI uses advanced deep learning to predict case outcomes with 95% accuracy"*

### Decoded:
- **Task?** Predict court rulings — OK, that's specific
- **Data?** Unknown — what cases? Which jurisdiction? How old? **Red flag.**
- **Evaluation?** "95% accuracy" — on what test set? How was it split? Was it cherry-picked? **Red flag.**

### Verdict: Sounds impressive, but **unverifiable without transparency**

![bg right:25%](img/mascot/AID_8.svg)

---

## Applying the Decoder

**Claim:** *"Our AI-powered contract review tool eliminates the need for legal review"*

### Decoded:
- **Task?** Review contracts — but for what? All clauses? Specific risks?
- **Data?** Unknown — what types of contracts? What jurisdictions?
- **Evaluation?** "Eliminates the need" — no metric at all. **Major red flag.**

### Verdict: **Marketing, not science.** AI assists, it does not eliminate legal judgment.

---

# Can AI Conquer the World?

---

## Process of creating AI
- Task Definition:
  * T2026 Conquer the world
- Learning process:
  * Dataset: ?
  * Training procedure: ?
- Performance evaluation:
  * Performance metrics: ?
  * Testing procedure: ?

<!-- The framework exposes the absurdity. Without a clear task, data, and evaluation — there is no AI. "General AI" or "superintelligence" is not something you can just train. The hype often skips over these fundamental requirements. -->

---

## Can AI Replace Lawyers?

### What AI **cannot** do:
- Exercise legal **judgment** in novel situations
- Provide **ethical reasoning** and moral counsel
- Build **client relationships** and trust
- Argue with **persuasion** and empathy in court
- Take **professional responsibility** for advice

### What AI **will** change:
- Legal research — hours to minutes
- Due diligence — automated document review
- Contract drafting — first drafts and clause libraries
- Case management — predictive triaging

> AI is a **power tool**, not a replacement. The lawyer who uses AI will outperform the one who doesn't.

---

# AI Regulation
## Why Lawyers Matter

![bg right:40%](img/mascot/AID_10.svg)

---

## EU AI Act — Risk-Based Framework

### Unacceptable Risk (Banned)
- Social scoring by governments, real-time biometric surveillance

### High Risk (Strict obligations)
- AI in justice and law enforcement, credit scoring, hiring
- Requires: conformity assessment, transparency, human oversight

### Limited Risk (Transparency obligations)
- Chatbots, deepfake generators
- Requires: users must be informed they interact with AI

### Minimal Risk (Free use)
- Spam filters, AI in video games

---

## GDPR and AI

- **Art. 22** — Right not to be subject to solely automated decision-making
- **Right to explanation** — Individuals can request meaningful information about the logic of automated decisions
- **Data minimization** — Only collect data necessary for the purpose
- **Purpose limitation** — Data collected for one purpose cannot be repurposed without consent
- **Consent** — Explicit consent required for processing sensitive data

### Key question for lawyers:
*Does the AI system make or significantly assist decisions that affect individuals' rights?*

---

## Key Legal Challenges in AI

### Liability
- Who is responsible when AI makes a wrong decision — the developer, the deployer, or the user?

### Bias and Discrimination
- AI trained on biased historical data can perpetuate and amplify discrimination

### Intellectual Property
- Who owns AI-generated content — the user, the developer, or no one?

### Evidence and Trust
- Deepfakes, AI-generated documents — how do courts assess authenticity?

---

## Trustworthy AI — 7 Principles (ALTAI)

1. **Human Agency and Oversight** — Humans remain in control of AI decisions
2. **Technical Robustness and Safety** — AI systems work reliably and securely
3. **Privacy and Data Governance** — Personal data is protected (GDPR)
4. **Transparency** — AI decisions are traceable and explainable
5. **Diversity, Non-discrimination and Fairness** — AI avoids bias
6. **Societal and Environmental Well-being** — AI benefits society broadly
7. **Accountability** — Mechanisms exist for responsibility and redress

> As future legal professionals, you will **define, interpret, and enforce** these principles.

---

## Q&A

- AI = simulation of human intelligence
- Every AI has a **task**, **data**, and **evaluation** — use this to decode any claim
- The 3-question decoder: Task? Data? Evaluation?
- AI will **augment**, not replace lawyers
- Regulation is where **law meets technology**
- Your role: bridge the gap between technology and society

![bg right:35%](img/mascot/AID_7.svg)

<!-- jou -->
