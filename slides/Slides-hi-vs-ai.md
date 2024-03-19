---
marp: true
theme: default
paginate: true
---

<!-- _paginate: skip -->
# AI:Dental X-Ray Diagnostics 
## Shaping Human and Artificial intelligence hand in hand

---

## Introduction
- Startup: AI:Dental 
- Interests: X-ray Diagnostics AI and Education Platform
- Speaker: Peter Jurkáček, CTO
- Mission Statement: Enhancing Diagnostic Accuracy and Education in Dentistry Through AI Technology

---

## Agenda
- Understanding AI (definitions and concepts)
- Utilizing AI in AI:Dental
- Creating AI and HI with examples
- The role of regulations in AI development
- Will we be overruled by AI?
- Q&A session for in-depth discussions

---

# What is AI?
## *Simulation of Human Intelligence by Machines*

--- 

<!-- 
Differentiating Human Intelligence and Artificial Intelligence 
-->
# Oversimplify the complexity
## Human Intelligence
* Human with ability to solve different complex tasks

## Artificial Intelligence
* Algorithm with ability to solve different complex tasks

---

## Complex task
*Complex task refers to a problem or objective that demands sophisticated computational methods, such as machine learning, natural language processing, computer vision, or other AI techniques*

---

# AI:Dental's Complex Tasks
## Computer vision *(Images)*
- T01: Detect Suspicious Regions in dental x-rays
- T02: Classify dental conditions and abnormalities for specific region
- T03: Visual explanation to aid dentist in interpretation
- T04: Provide suggestions for appropriate treatment for specific region

## Natural language processing *(Text)*
- T05: Interactive learning with real-time guidance

## Multimodal *(Images + Text)*
- T06: Search for relevant X-ray images

---

### Computer vision task
# T01: Detect Suspicious Regions in dental x-rays
- **Input:** X-ray image
- **Methods:** DINO (Object detector)
- **Output:** Region of interest represented by x, y, width, height coordinates

<!-- _footer: "[(2022) DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection](https://arxiv.org/abs/2203.03605)" -->
---

### Computer vision
# T02: Classify dental conditions and abnormalities for specific region

- **Input:** Region of interest + X-ray image
- **Methods:** EfficientNet (Image classifier)
- **Output:** Severe tooth decay

<!-- _footer: "[(2019) EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)" -->

---

### Computer vision
# Provide suggestions for appropriate treatment

- **Input:** Region of interest + X-ray image
- **Methods:** EfficientNet (Image classifier)
- **Output:** Root canal treatment

<!-- _footer: "[(2019) EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)" -->

---

### Computer vision
# T03: Visual explanation to aid dentist in interpretation.

- **Input:** Region of interest
- **Method:** GALORE, Grad-CAM, Grad-CAM++
- **Output:** Saliency map

---

## Multimodal
# T06: Search for relevant X-ray images

- **Input:** Text or X-ray image prompt
- **Methods:** 
  - Image encoder (ResNet-50)
  - Text encoder (DistilBERT)
  - Projection function
- **Output:** The most similiar X-ray image

<!-- _footer: "[(2023) Dental CLAIRES: Contrastive LAnguage Image REtrieval Search for Dental Research](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10283104/)"-->

---

## Natural language processing
# Real-time guidance

- **Input:** Question, Student's answer, Correct answer
- **Method:** 
  - Cusomized chatbot (e.g. Chatgpt)
    - Response Generation and Control with low temperature
    - Knowledge Management with external knowledge bases
    - Conversation Flow Management with chain of thought prompting
    - Robustness and Reliability with building defensive APIs and user interfaces
- **Output:** Clarification of correct answer

---

# But how can create those AIs?

---

# Process of creating an AI
- Task Definition:
  * Identifying the objectives and goals of the AI system learning process
- Exercise (Training) creation: 
  * Prepare dataset
  * Development of training procedure/activity/script
- Performance Evaluation
  * Performance metrics definition
  * Development testing procedure/activity/script

---

## Process of creating AI
- Task Definition: 
  * T02 Classify dental conditions and abnormalities for specific region
- Exercise Creation
  * Prepare dataset: 1000 train samples (x-rays + expert opinions)
  * Training procedure: Supervised learning
- Performance Evaluation
  * Performance metrics definition: Precision, Recall, F1score
  * Testing procedure: Compare AI on 100 test samples (x-rays + expert opinions)

---

## Process of creating AI
- Task Definition: 
  * T06 Search for relevant X-rays
- Exercise Creation
  * Prepare dataset: 1000 train samples (x-rays + expert opinions)
  * Training procedure: Contrastive Learning
- Performance Evaluation
  * Performance metrics definition: Precision, Recall, F1score
  * Testing procedure: Compare AI on 100 test samples (x-rays + expert opinions)

---

# What about creating Human Intelligence?

---

# Process of creating Human Intelligence
- Task Definition: 
  * T02 Classify dental conditions and abnormalities for specific region
- Exercise Creation
  * Prepare dataset: 1000 train samples (x-rays + expert opinions)
  * Training procedure: https://edu.aidental.ai (tagging per patient, quiz)
    - Supervised learning
- Performance Evaluation
  * Performance metrics definition: Precision, Recall, F1score
  * Testing procedure: Compare their answers on 100 test samples (x-rays + expert opinions)

---

# Can AI Conquer the World?

---

# Process of creating AI
- Task Definition: 
  * T2024 Conquer the world
- Exercise Creation
  * Dataset: ?
  * Training procedure: ?
- Performance Evaluation
  * Performance metrics: ?
  * Testing procedure: ?

---

## AI Regulations
- Current regulations
- Ensuring Trustworthiness in AI Systems
- Ethical considerations
- Adherence to privacy regulations in handling patient data.
- Bias and discrimination
- Transparency, accountability, and fairness in AI algorithms

---

## Q&A
- AI - simulation of human intelligence
- Complex tasks in dentistry
- Process of creating AI and HI with examples
- Will we be overruled by AI?
- The role of regulations in AI development
