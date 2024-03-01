---
marp: true
theme: custom-default
title: Unlocking the Future of Dentistry
paginate: true
footer: 'AI:Dental'

---

<!-- _paginate: skip -->
# Demystifying **AI** in Dentistry 
Deep dive into **Blackbox** for in X-Ray diagnostics
<!--
- Welcome students to the session.
- Brief overview of the agenda. 
-->

![bg right 60%](img/image-1.png)

---

<!-- Understanding AI in Diagnostics -->
# What is the **AI**?

![bg left 60%](img/image-3.png)

*Artificial Intelligence (AI) is the **simulation of human intelligence** processes by computer systems.*

---

# **Human Intelligence** in dentistry?
## E.g Dental professional
<div class="mermaid">
flowchart LR
  input["An X-Ray image"]
  model["Dental professional"]
  output["Opinion"]

  input --> model --> output
</div>

---

# **Simulation** of **Human Intelligence** in dentistry?
## E.g Artificial intelligence
<div class="mermaid">
flowchart LR
  input["An X-Ray image"]
  model["AI"]
  output["Opinion"]

  input --> model --> output
</div>


---
<div class="columns">

<div>

## How **You as a student** can become **Dental professional**?
- Relevant X-ray images
- Dental professionals' opinions

</div>

---

<div class="columns">

<div>

## How You as a student can become Dental professional?
- Relevant X-ray images
- Dental professionals' opinions

</div>
<div>

## How **AI as a student** can become **Dental professional**?
- Relevant X-ray images
- Dental professionals' opinions

</div>

---

<!-- - Title: "Training Our AI: From Annotations to Classification" -->
# **Let's train yourself** and also our AI

[-] You will go trought our excersices in x-ray interpretation
[-] AI will go trought our excersices
[-] Compare you vs AI

---
<!-- # Advantages of AI in Dentistry
- Improved accuracy and efficiency in diagnosis.
- Reduction of human error and subjectivity.
- Enhanced speed in processing and analyzing large datasets.
- Potential for early detection and prevention of dental issues.

--- -->

# Hands-On Training with Our Education Platform
- Train on specific pathologies with **Quiz**
- Train on real patients' cases with **Tagging per patient**
- Search for relevant cases with **Catalog of cases**

![bg right 90%](img/edu_app.png)

--- 

<!-- Decoding X-Rays: Visual Explanation with Saliency Maps -->
# Visual Explanation with Saliency Maps
- Introduction to saliency maps for image interpretation.
- Demonstration of saliency maps highlighting important features in X-ray images.
- Importance of visual explanations for understanding AI decisions.

---

# Conclusion and Next Steps
- Recap of key points covered in the session.
- Encouragement for students to continue exploring AI in dentistry.
- Next steps for further learning and engagement with the education platform.

---
<!-- - Title: "Engage, Inquire, Explore" -->

# Q&A
- Open the floor for questions and discussion.
- Encourage students to share their thoughts, concerns, and ideas.

---

# 9: Thank You
- Title: "Thank You for Joining Us"
- Express gratitude to the students for their participation.
- Contact information for further inquiries or follow-up.

Note: Each slide should be visually appealing with relevant graphics, images, and minimal text for effective communication. Interactive elements such as demonstrations and real-time examples can enhance engagement and understanding.

<!-- Needed for mermaid, can be anywhere in file except frontmatter -->


# Mermaid
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  const callback = function () {
    alert('A callback was triggered');
  };
  const config = {
    startOnLoad: true,
    flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'cardinal' },
    securityLevel: 'loose',
  };
  mermaid.initialize({config});
</script>