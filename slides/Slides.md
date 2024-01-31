---
marp: true
theme: custom-default
title: Bridging the Gap
paginate: true
footer: 'AI:Dental'
---

<!-- Add this anywhere in your Markdown file -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

<!-- <style>
  section {
    background: '#ABF7CE';
    font-family: 'DMSans-AID-Headline', 'DMSans-AID-Text';
  }
</style> -->
<!--
HD 1280 x 720	13.333	7.5
Full HD 1920 x 1080	19.999	11.25
Quad HD 3840 x 2160	39.999	22.50
4K 4096 x 2160	42.664	22.50 
-->

<!-- https://docs.decksetapp.com/English.lproj/Formatting/13-auto-scaling.html -->

<!-- _paginate: skip -->
<!-- _footer: "" -->
# Bridging the Gap
## How AI Connects Dental Clinics with Students
![bg right 50%](img/image.png)
AI:Dental

---
<!-- _backgroundColor: '#A478FF' -->
<!-- _color: '#000' -->
# Brief Intro
![bg grayscale opacity:.6 left](img/cto_profile_02.jpeg)

Peter Jurkáček
CTO at AI:Dental

peter.jurkacek@aidental.ai
![drop-shadow 40%](img/linkedin_02.JPG)

<!-- 
# Problem statement
- Studenti idu na kliniku nepripraveni
- Proces pridelovania stundetov na kliniky nie je transparentny
- Challanges in dental education
    - Curricular Relevance (Stream data from real clinics automatically)
    - Clinical Training Opportunities (Transform data to training materials)
    - Ethical and Legal Challenges (Consents)
    - Access to Education (Free)
- Students' and Professor's pain points
- Relatable story 
-->

<!-- References
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8238744/
https://pubmed.ncbi.nlm.nih.gov/30861309/ 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9026102/
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5334326/
https://www.researchgate.net/publication/



(1996 Room for improvement? The accuracy of dental practitioners who diagnose bony pathoses with radiographs)[https://pubmed.ncbi.nlm.nih.gov/8665324/]
-->
---
# Bridging <u>the Gap</u>
## How AI Connects Dental Clinics with Students
![bg right 50%](img/image-1.png)
<!-- ---
To democratize dental health through AI by enhancing precision, affordability, and accessibility in education and patient care. 
Shaping the future of the dentistry through creating the conditions for everyone to access the affordable and personalised healthcare.  -->

---
<!-- _footer: "1. 2022 Evaluation of radiographic interpretation skills of undergraduate dental students studying in a dental college of Punjab, India – A comparative study" -->
# The Gap
Dental students' accuracy ranges from **48% - 65%** in radiograph interpretation<sup>[1]</sup>

![bg left](img/qexample.png)

<!-- Which is problematic becuase Dental  radiographs  are  essential in  making  an accurate diagnosis, performing dental procedures, in evaluating procedural success and in documentation of dental and oral health -->

[1]: https://www.researchgate.net/publication/367683626_Evaluation_of_radiographic_interpretation_skills_of_undergraduate_dental_students_studying_in_a_dental_college_of_Punjab_India_-_A_comparative_study

<!-- 
![bg transparent 100% 20%](image-7.png)
![bg 65%](tfe_answers/pdentits-answers-E.png) 
-->
<!-- *Expert 1*, *Expert 2* -->

<!-- interpreting radiographs (i.e., orthopantomograms, OPTs) is an error-prone process, even in experts -->
<!-- low-prevalence anomalies earlier and high-prevalence anomalies -->
---
<!-- _footer: "2. 2022 Dental Students’ Knowledge, Confidence, Ability, and Self-Reported Difficulties in Periodontal Education: A Mixed Method Pilot Study" -->
# Why the Gap?<sup>[2]</sup>
![bg vertical left:30% 60%](img/image-2.png)
- Limited or no access to relevant radiographs (X-rays)
- Instructor inconsistency
![bg 60%](img/image-3.png)

[2]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9026102/

---
# <u>Bridging</u> the Gap
## How AI Connects Dental Clinics with Students
![bg right 50%](img/image-1.png)

---

## The Bridge - AI:Dental for Education

- A) Auto-transform radiographs into assignments (train, test, evaluate).

- B) Apply supervised learning with visual explanations

- C) Search for relevant radiographs (Google Lens for dentistry).

---
## A) Auto-transform radiographs into assignments
#

<div class="columns">
<div>
Digital Medical Record

![w:512](img/321b949b-b01d-49b0-97a8-75af270f5e98.jpg)
    <!-- ![w:256](EMR_semafor.png) -->
</div>
<div>

Questions & Answers
![w:512](img/edu_quiz.png)

</div>
</div>

---
<!-- _footer: "3. An Explainable Deep Learning Model to Prediction Dental Caries Using Panoramic Radiograph Images (2023)" -->
## B) Apply supervised learning with visual explanations
#

<div class="columns">
<div>
Questions & Answers

![w:512](img/edu_quiz.png)
</div>
<div>

Saliency maps<sup>[3]</sup>
![w:512](img/grad-cam.png)

</div>
</div>

[3]: https://www.researchgate.net/publication/366946851_An_Explainable_Deep_Learning_Model_to_Prediction_Dental_Caries_Using_Panoramic_Radiograph_Images

---
<!-- _footer: "4. Dental CLAIRES: Contrastive LAnguage Image REtrieval Search for Dental Research (2023)" -->

<!-- 
https://www.sciencedirect.com/science/article/pii/S2772442523001491 
https://www.mdpi.com/2075-5309/13/2/275
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10283104/
-->
## C) Search for relevant radiographs<sup>[4]</sup>

![w:1000px](img/image_retrieval.png.png)
<!-- ![bg left 100%](edu-app/catalog.png) -->

[4]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10283104/

---
# Advantages for Dental Clinics
- Performance evaluation
- Onboarding zamestnancov
- Ušetrený čas a peniaze
- save 5 minutes per visit with assisted diagnostics
- Patient treatment outcomes
- Better dental care

---
# Future Developments / Next steps
![bg right 50%](img/image-1.png)
### Spoluprace s univerzitami po celom svete
### Case studies
- Meduni & LFUK & Bangalore
- Subjectivity of a dentists
- AI reader study
### CE mark
- Spadame pod MDR preto potrebujeme CE mark
- clinical investigation
---