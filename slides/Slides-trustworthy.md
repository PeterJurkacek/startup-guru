---
marp: true
theme: custom-default
title: Trustworthy AI
paginate: true
footer: 'AI: Dental'
---
<!-- _footer: ""-->
<!-- speaker_notes: In this presentation, we'll explore how our AI system for dental care adheres to the ALTAI principles for trustworthy AI. By following these principles, we ensure the development and deployment of reliable and responsible AI that benefits the dental field. -->

# Trustworthy AI
## AI:Dental

![bg right](img/mascot/AID_5.svg)

---

# AI System Introduction

---

## AI System Introduction

<div class='columns3'><div>

## Input
- Dental X-rays (OPG, Intraoral)

</div><div>

## AI Analysis:
- Identifies individual teeth
- Classifies pathologies (cavities, infections, etc.)
- Detects past procedures (fillings, root canals)

</div><div>

## Output:
- Comprehensive report with findings & visuals
- Integrates with patient records
- Educational platform for student learning

</div></div>

---

# AI:Dental Examples of Trustworthiness

Following key principles of Assessment List for Trustworthy Artificial Intelligence (ALTAI) for developing **responsible** and **ethical** **AI systems** in healthcare


<!-- 
ALTAI seven principles
- Human Agency and Oversight
- Technical Robustness and Safety
- Privacy and Data Governance
- Transparency
- Diversity, Non-discrimination and Fairness
- Societal and Environmental Well-being
- Accountability
-->

---

## Human Agency and Oversight

<!-- Human Agency and Oversight: This principle ensures that humans maintain control over AI systems and are ultimately accountable for their decisions. -->

- Radiologist reviews all flagged images by the AI system to confirm or reject the findings
- In the user interface, we implement visual distinctions between AI-generated opinions and those provided by human professionals.
- To tackle overreliance, we are integrating AI into education itself so students learn to use AI as a tool rather than as a second opinion.

<!-- Image: (Left side) Consider adding an image of dentists working together or a student learning dentistry.

---

## Principle 1: Data-Centric AI

Focus on high-quality data, not just complex models. 

* **Explanation:** Clean, accurate data leads to more reliable AI outcomes.

<!-- Image: (Left side) Consider adding an image of a data chart or graph to represent data quality. -->

---

<!-- Technical Robustness and Safety: AI systems should be designed and built to be reliable and secure, with safeguards in place to mitigate risks. -->
## Technical Robustness and Safety

- Ensure the AI meets safety standards for medical devices (Software as a medical device, Quality management system)
- Currently, we do not support image upload feature through our system because we don't have mechanisms to deal with adversarial attacks.
- Our AI is provided as a service, so we can simply make the service unavailable in the event of its failure or misuse
- Our system does not replace doctor opinion, and all final decisions are made by dental professionals.
- Data encryption and access controls


<!-- Image: (Left side) Consider adding an image of a checkmark or shield to represent safety and security.

---


## Privacy and Data Governance

<!-- Privacy and Data Governance: This principle emphasizes the importance of protecting personal data and ensuring its responsible use in AI development and deployment. -->


- We are using data that was collected with explicit consent or from a public dataset, which states that all data was collected in a legal and ethical manner.
- We have prepared friendly and easily understandable materials to explain to patients how their data will be used. Additionally, this information is available in our privacy policy terms and conditions.
- In this case, we have consent management in place. If a patient does not give explicit consent, we do not obtain their data and do not use it in any further steps.
- In case of possible misuse of personal and sensitive data or sharing of concerns about their privacy patients have to contact their clinic first, and the clinic has to report this to us.

![bg right:20% 70%](img/mascot/AID_7.svg)

<!-- - Protect patient privacy and ensure data legitimacy.

### Examples:
- Patient Data Pseudoanonymization
- Own Data Acquisition with Patient Consent
- Public datasets legal and ethical considerations
- Data-centric AI -->
<!-- Image: (Left side) Consider adding an image of a lock or shield to represent data privacy.
 -->

<!-- Patient privacy is paramount. We anonymize patient data while maintaining its legitimacy through direct acquisition with informed consent. This ensures we protect patient confidentiality while building a robust dataset for AI development.
Responsible data collection and management practices are essential for trustworthy AI. We prioritize patient privacy by anonymizing data while ensuring its validity through informed consent procedures.
 -->


---

## Transparency
<!-- Transparency: AI systems should be understandable, allowing users to comprehend how they arrive at decisions. -->


- Build trust by making the AI's training data accessible.
- Each model training is reproducible, and we utilize experiment logging to monitor the training and evaluation of a model. Code changes and documentation are versionized in Git.
- We constantly test our software with human professionals and integrate their suggestions.

<!-- * **Example:** 
    - Transparent Dataset in Education platform -->

<!-- Image: (Left side) Consider adding an image of an open book or microscope to represent transparency. -->

<!-- Transparency is key to building trust. We make our dataset available for educational purposes. This allows for scrutiny and understanding of the data used to train our AI, fostering trust in its development process.
By making our training data accessible, we promote transparency and allow for independent evaluation of our AI system. This fosters trust in the development process and the reliability of our AI. -->
---

## Diversity, Non-discrimination & Fairness
<!-- Diversity, Non-discrimination and Fairness: AI systems should be free from bias and ensure fair and inclusive outcomes for all. -->

- Using data from various sources ensuring demographic richness (International Cooperations)
- Annotating data with multiple opinions from various dental professionals
- Analyzing model outputs in terms of demographic biases
- Provide equal Access to educational resources and opportunities for dental students from diverse backgrounds to enhance their learning and diagnostic skills, regardless of geographic location or institutional affiliation.

<!-- Image: (Left side) Consider adding an image of a globe or people from diverse backgrounds to represent data diversity. -->

<!-- We strive to reduce bias in our AI. We incorporate data from various sources, including public datasets and international collaborations. Our data also ensures diverse demographics are represented. This comprehensive approach helps mitigate bias and promotes fair and equitable outcomes for all patients.
Using data from diverse sources and ensuring a representative demographic spread helps mitigate bias in our AI models. This promotes fair and unbiased outcomes for all patients, regardless of background. -->

---
# Societal and Environmental Well-being
<!-- - Societal and Environmental Well-being: The development and use of AI should consider its impact on society and the environment, promoting positive outcomes. -->

- Currently, we have defined functionalities that do not require real-time inference for each user separately but instead utilize batch inference, which caches results for other users.
- The use of our AI system may positively affect the development of professional competencies and digital skills and effectivity

---

# Accountability
<!-- Accountability: There should be clear mechanisms for holding developers and deployers accountable for the actions of AI systems.  -->

- Software as a Medical Device
- Clear Lines of Responsibility

<!-- Image: (Left side) Consider adding an image of a handshake or scales to represent accountability.

Speaker Notes:
We take accountability for our AI system seriously. As a medical device, it adheres to regulations that establish clear lines of responsibility for its development and deployment. In case of any issues, these established lines ensure a clear path for addressing them.
As a medical device, our AI system adheres to regulations that establish clear lines of responsibility for its development and deployment.  This ensures accountability in case of any issues.  We take this responsibility seriously and are committed to maintaining the highest standards for our AI in dental care. -->

---

## Main Challenges to Achieve Trustworthiness

- Data Quality: Maintaining high-quality and diverse datasets.
- Ethical Considerations: Adhering to ethical guidelines.
- Bias Mitigation: Addressing biases in data and models.
- Continual Improvement: Regular updates to adapt to changes.
- Regulatory Compliance: Meeting regulatory standards.

<!-- Speaker Notes:
While we strive for a trustworthy AI system, challenges exist. Maintaining high-quality and diverse data is an ongoing effort. We actively address ethical considerations and work to mitigate potential biases in data and models.  Continual improvement ensures our AI adapts to new information and remains reliable. Finally, meeting regulatory standards is crucial for operating in the healthcare field.
Developing trustworthy AI involves ongoing efforts.  We continuously strive to maintain high-quality and diverse datasets, adhere to ethical guidelines, and address potential biases.  Regular updates ensure our AI adapts to new information and remains reliable.  Finally, meeting regulatory standards is crucial for operating in the healthcare field. -->

---

## Conclusion

- Our AI system prioritizes trustworthiness
- Data-centric approach, ethical practices, collaboration with dental professionals
- Challenges exist, but we are committed
- Transparency and continual improvement ensure reliability and efficacy

<!-- Our AI system is built on the foundation of trustworthiness.  We prioritize a data-centric approach, ethical practices, and collaboration with dental professionals worldwide.  While challenges exist, we are committed to continuous improvement and transparency. This ensures our AI remains reliable and delivers effective outcomes in dental care. -->

---

# Questions & Discussion

Open for questions and discussion.

