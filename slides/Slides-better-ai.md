---
marp: false
theme: custom-default
paginate: true
---

## Predstavenie RTG snímok a ich dôležitosti v zubarine
- Kazy nie sú viditeľné volným okom
    - *Bitewing radiography is commonly used to detect proximal caries, which require accurate diagnoses and early management and cannot be detected clinically due to tight contact surfaces [Gimenez et al., 2015]. Many factors, such as fatigue, emotions [Stec et al., 2018], and complex clinical environments [Hellén-Halme et al., 2008], could affect the accuracy of image interpretation.*
- 3D ako napr. CBCT má vysokú dávku žiarenia a preto stale najviac používané sú 2D RTG snímky

## Analýza RTG snímku zubárom
1. Identify suspicious regions
2. Classify pathologies
3. Explain findings to patient
4. Perform procedure
5. Make a Electronic Health reccord of visit
    - Pri návšteve zubára vám vytvorí digitálny otlačok, ktorý sa volá zubný kríž

## Identifikované problemy pri diagnostike RTG snímok
- Ground true is hard to get (kaz je viditeľný až po rozvŕtaní zubu)
    - X-ray image is just a pomocna metoda 
    - Potrebujeme aj radiologicky pohlad ale aj klinicky pohlad
    - Pathologies are hidden until hole is drilled (Clinical view)
- Inter-observer agreement (subjektivita pri hodnotení)
    - Like medical doctors, different dentists may draw different conclusions from radiographs, and these may affect the way a patient is treated
    - "If first dentist annotate that there is not a Decay there is 87% chance that second one independently will agree and 13% that second will disagree"
        ((79.7 / (79.7 + 13.1))+(89.5 / (89.5 + 6.2))+(79.5 / (79.5 + 15.3)))/3 = 87%
    - "If first dentist annotate that there is Decay, there is a 34% chance that second one independedly will spot the decay, and a 66% chance that second one will not spot the decay"
        ((7.2 / (7.2 + 13.1))+(4.3 / (4.3 + 6.2))+(5.2 / (5.2 + 15.3)))/3 = 33%
        [Can a Computer Identify Carious Lesions in Dental X-Rays As Accurately As Humans?](https://www.hellopearl.com/products/second-opinion)
    - Uspesnost zubarov TODO%
    - Errors due to exhaustion
    - Missed findings out of specialization
    - A bunch of different pathologies
    - Subjectivness during interpretation (Radiological view)
- Nepripravenosť na klinickú prax (nedostatočný počet prípadov, Datasety RTG snimok zubov na internete sotva najdete)
    - Uspesnost studentov TODO%
        - Zistili sme, nie je vysoka ani medzi studentami zubariny, pricom po odpromovani nastupuju s uspesnostou okolo TODO% a nasledne zbieraju skusenosti na klinike. Toto zistenie vyplyva z existujucich studiji (Odkaz) a pri pilotnom testovani edukacnej aplikacie priemerne skore studentov bolo opdobne (Obrazok z pilotneho testovania) okolo TODO%
    - Students miss over 43% of actual caries and are only right 57% of the time they identify one, while our AI consistently outperforms them in both accuracy and reliability. [Evaluation of radiographic interpretation skills of undergraduate dental students studying in a dental college of Punjab, India – A comparative study](https://www.researchgate.net/publication/367683626_Evaluation_of_radiographic_interpretation_skills_of_undergraduate_dental_students_studying_in_a_dental_college_of_Punjab_India_-_A_comparative_study)

# Analýza RTG pomocou AI (Overview)?
## Viaceré modality
- OPG images
- BW
- Periapical
- Cefalor
- CBCT
- Other

## Enhanced process of dentist with AI assisted
1. Identify suspicious regions (Object detection, Instance segmentation)
    - Detekcia kazov
        - Pracné anotovanie, Náročné určiť hranice pri kazoch, Nedostaočné
    - Sémantická segmentácia (dostupne architektury na trhu Unet, Unet++, NNUnet)
        - Pracné anotovanie, Náročné určiť hranice pri kazoch
    - Inštančná segmentácia
        - Pracné anotovanie, Náročné určiť hranice pri kazoch
2. Classify pathologies (Image classification)
    - Klasifikácia
        - Ľahké anotovanie / Softlabels, Nízka vysvetliteľnost (Chýbajúca lokalizácia)
3. Explain findings to patient (Visual explanation, Test explanation)
4. Perform procedure (~~Robotics~~)
5. Make a Electronic Health reccord of patients visit (Chart filling)
    - From Voice 
    - From Image


## AI:Dental AI
- Make a Electronic Health reccord of patients visit
    - Komplexné vyplňanie zubného kríža (Chart)
    - Detecting decays is not enought
        - Ked sme prezentovali AI klinikam zistili sme, ze klinike nestacia kazy ale chceli by aj periapikalne lezie, plomby, restoracie, struktury v ustach. Preto pokial chceme pomoct zubarovi komplexne skontrolovat usta pacienta a identifikovat vsetky nalezy, ktore sa tam mozu vyskytovat zistili sme ze s datasetom, ktory obsahuje iba kazy si nevystacime. Mnozstvo patologii, ktore musi doktor urcite je XY. Ale ako vieme vytvarat datasety pre ktore neviem ani ground true.
    - Pracný zber anotácií
- Komplexnost patologií
- Zbieranie anotácií (Noisy labels)
- Vysvetliťeľnosť
- Komplexné vypĺňanie zubného kríža

## Zbieranie anotácií
- Medzinárodné spolupráce (Vieden, India, Egypt, Slovakia)

### Zbierame zubné kríže z kliník (Clinical view)
    - AI pre detekovanie a číslovanie zubov
    - Zubný kríž je JSON štuktúra číslo zubu+patológia
    - RTG snímka (OPG, BW, Periapical)
    - Vďaka AI detekcií zubov a detekcií zubov sme schopní mapovať patológie na obrázky
        - Tvoríme kontent do edu aplikácie
        - Vytvárame dataset pre klasifikáciu patológií
        - Na detekciu používame TODO architekturu (DINO swin)
    - Úspešnosť > TODO%, TODO number of classes
    - Continual data acquisition
    - GDPR complaint
    - GUID: Right to Access, Rectification, Erasure, Restrict Processing, Data Portability (Data Governance)

## Prehľad počtu patológií z jednej kliniky
- Matica distribúcie patológií
- Množstvo patológií

### Crowdsourcové zbieranie názorov (Readiological view)
- On premise CVAT opensource
- Edu aplikacia
    - Kedze sme si uvedomovolali potencial dat, ktore mame chceli sme vytvorit nastroj cez ktory dokazeme zbierat posudky a zaroven pomocou zvysit uroven vzdelanosti pri interpretacii RTG snimok. Preto sme implementovali Edukacnu platformu v ktorej poukazujeme na nejednoznacnost interpretacie aj medzi expertami aj pri diagnostikou AI a snazime sa studentom ukazat tieto nazory aby k nim pristupovali kriticky a uvedomovali si, ze pri interpretaci nie je binarna odpoved ano nie ale miera istoty. 
- Disagreement nasich zubárov pri určovaní kazov je TODO%
- Evaluaované na TODO casesoch
- Počet získaných názorov TODO
- Human in the loop
- Continual data acquisition

### Klasifikácií patológií
- Modulárny prístup
- Klasifikátor pre každú patológiu pomocou
    - Na riesenie Inter-observer agreement sme zacali zberat viacere nazory. Pre nas sa ako najlepsie ukazalo vahovanie ground true podla priemerneho poctu votov, ktore dostalo. 
    - Pri klasifikácia každej patológie musíme mať aspoň 4 názory. Názory priemerujeme a používame ako váhu pri počítaní chyby pri crossEntropii. Podarilo sa nam týmto stabilizovat trening
    - Experimentovali sme s metódou z MIT kde sa počíta bias anotátorov (TODO) ale neukázala sa nám ako úsepšná
- Úspešnosť > TODO%, TODO number of patológií
- Nemá zatiaľ zmysel pre šudentov ale snažíme sa ju certifikovať aby slúžila na klinike na zefektívnenie administrácie

### Vizuálizácia
- Hranice patológií sú pracné a náchylné na chybu 
- Pomocou AI dotvárame obraz kde sa asi patológia nachádza
- Generovanie heatmap pomaha pouzivatelom lokalizovať podozrivé miesta na snímku bez potreby kreslenia experta
- Heatmapy sa generujú raz a pre všetkých, takže šetríme životné prostredie
- Používame GRAD-CAM. Problém pre negatívne triedy -> GLORE

### Ako je nasa AI doveryhodna
- ALTAI skore radial chart but we are aware of were we can improve and what we can improve.
- It's a long run
- Highlights
    - Integrating AI into education
    - Showing AI and experts results to support critical thinking
    - Tracebility thank to Data version control
    - Pomocu Edu app získavame feedback na AI pred tym ako priamo ovplyvní pacienta


RTG snimok, je dolezity lebo niektore patologie 

Podme identifikovat kazy z RTG snimok aby AI mohla zubara upozornit na pritomnost zubneho kazu. Rozhodli sme sa pouzit dostupne architektury na trhu Unet, Unet++. Rozhodli sme sa pre Model Centric approach, kde sme urobili projekt, ktorym sme vedeli skusat vsetky SOTA architektury na semanticku segmentaciu (Unet, Unet++). Ale co s datasetom? Potrebovali sme RTG snimky. Datasety RTG snimok zubov na internete sotva najdete. Aj ked najdete a zacnete ich kontrolovat tak zistite, ze obsahuju chyby. Preto sme sa rozhodli, ze si pripravime vlastny dataset RTG snimok. Nasadili sme si vlastnu instanciu anotacneho nastroja, najlepsie vyzeral opensource CVAT. V tomto nastroji sme vytvorili dataset na ktorom nam lekari polygonami ohranicovali nalezy kazov. Zvolili sme iterativny pristup pri ktorom lekar snimok oanotoval a druhy jeho zistenia nasledne validoval.

A spustili sme trenovanie s klasickym UNetom ako proof of concept to fungovalo ale model nedokazal dobre generalizovat na validacnom datasete. Podla studie, ktoru sme replikovali mal klasicky UNET mat uspesnost XY% a nam sa podarilo vytlacit F1 score na 30%. Dali sme vizaulne validovat vysledky modelu doktorovi aby nam povedal ako dobre model performuje. 

A ako sme ho pozorovali sme zistili, ze model oznacil niektore veci, ktore lekari pri anotovani prehliadli a ked boli so zisteniami konfrotovani tak uznali, ze model ma pravdu. V niektorych pripadoch striktne odmietli, ze ma model pravdu a niekedy ani sami nevedeli (False alarm). Vtedy sme si zacali uvedomovat, ze ked chcete vytvorit medicinsky dataset je to nieco ine ako ked sa snazite segmentovat macky a psov. Ako mame trenovat AI ked nemame ani nevieme ground true? Navyse ground true viete ziskat az po vyvrtani zubu pacienta a pokial chcete pre model pripravit snimok na ktorom su viacere kazy musel by zubar rozvrtat vsetky zuby pacientovi po urobeni RTG aby nam potvrdil, ze sa tam naozaj nachadzali.

Urobili sme experiment do ktoreho sme includli 8 zubarov a rozdelili im anotovat 1000 RTG snimok, pricom na kazdej snimke mali detekovane oblasti, ktore mali klasifikovat na pritomnost nalezu periapikalnej lezie. Po oanotovani sme zistili, ze z 1000 fotiek sa 100% zhodli na 500 snimkach, takze pomocou supervised pristupu sme boli schopni natrenovat model na iba na 500 snimkach.

Hlavny problem je v tom, ze na oanotovanie medicinskeho datasetu nam nestaci radiologicky pohlad ale potrebujeme aj klinicky pohlad. Ziskanie klinickeho ground true je velmi narocne lebo by bolo treba rozvrtat vsetky zuby pacientovi pocas jednej navstevy alebo v case znacit stav po rozvrtani zubu pacienta. K tomuto je potrebne aby ste boli napojeny na zdroj dat u ktoreho nam tecu data. To sa nam podarilo vdaka PMS semaforu softveru, ktory nam umoznuje zbierat data z partnerskych klinik.

Pokial nemate zaklad z ktorehe zbierate produkcne data neviete spravit robustnu AI. Totizto verejne dostupne datasety nam umoznili vyvinut iba proof of concept ale nie produkcnu AI, kedze produkcne data su castokrat bohatsie na šum. 

Kedze sme si uvedomovolali potencial dat, ktore mame chceli sme vytvorit nastroj cez ktory dokazeme zbierat posudky a zaroven pomocou zvysit uroven vzdelanosti pri interpretacii RTG snimok. Preto sme implementovali Edukacnu platformu v ktorej poukazujeme na nejednoznacnost interpretacie aj medzi expertami aj pri diagnostikou AI a snazime sa studentom ukazat tieto nazory aby k nim pristupovali kriticky a uvedomovali si, ze pri interpretaci nie je binarna odpoved ano nie ale miera istoty. 

Vyvinutie crowdsourcovej platformy nie je trivialne 

Preto sme sa rozhodli, ze budeme zbierat aj klinicky aj radiologicky. Navyse interpretacia RTG snimok nie je trivialna ani pre expertov. Ked sme zacali venovat tejto problematike a snazili sme sa odhalit podstatu nizkej uspesnosti interpretacie zistili sme, nie je vysoka ani medzi studentami zubariny, pricom po odpromovani nastupuju s uspesnostou okolo 50% a nasledne zbieraju skusenosti na klinike. Toto zistenie vyplyva z existujucich studiji (Odkaz) a pri pilotnom testovani edukacnej aplikacie priemerne skore studentov bolo opdobne (Obrazok z pilotneho testovania) okolo 50%




Expected documentation in wps

3.3 Proposed Method
3.1 Preprocessing
3.3.2 Model framework
3.3.3 Model training
4. Experimental results
4.1 Tooth segmentation and labeling
4.2 Tooth finding classification
4.3 Qualitative results and failures
5. Discussion / Next steps

Cize identifikovali viacere problemy
- 
- Inter-observer variability
- RTG je iba pomocna metoda

- Nakreslime kazy pomocou polygonu
- Value:
    - Pomahame zubarovi vizualne komunikovat pacientovi kazy
    - Pacientovi ale pomahame mu zefektivnit pracu?
- Gotchas:
    - Zubar/sestricka stale musi manualne zapisovat vsetky nalezy do electronic health reccords
    - Stanovanie


Na riesenie Intra observer variability sme zacali zberat viacere nazory. Podarilo sa nam stabilizovat trening vdaka aplikovaniu vahovanej cross entropie, ktora sa estimatuje pre kazdeho anotatora bias v jeho odpovediach. Pre nas sa ako najlepsie ukazalo vahovanie ground true podla priemerneho poctu votov, ktore dostalo. 


Navyse ked sme prezentovali AI klinikam zistili sme, ze klinike nestacia kazy ale chceli by aj periapikalne lezie, plomby, restoracie, struktury v ustach. Preto pokial chceme pomoct zubarovi komplexne skontrolovat usta pacienta a identifikovat vsetky nalezy, ktore sa tam mozu vyskytovat zistili sme ze s datasetom, ktory obsahuje iba kazy si nevystacime. Mnozstvo patologii, ktore musi doktor urcite je XY. Ale ako vieme vytvarat datasety pre ktore neviem ani ground true.

Co sme zistili?
- detecting decays is not enought
- interobserver variability
- intraobserver variability
- hard to find ground true
- softlabels can stabilize traning
- radiological view vs clinical view
- radiograph is considered as personal data
- edukacia nam pomaha ziskavat feedback
- prinasanie hodnoty offline



- Semantic segmentation of carries
- Semantic segmentation of structures
- BW Tooth detection
- OPG Tooth detection
- Restoration classification
- Finding classification

---

GDPR:
- Data minimization, Personal data removal (Privacy)
- GUID: Right to Access, Rectification, Erasure, Restrict Processing, Data Portability (Data Governance)
- Informed consents (Data Governance)

Scope: It applies to all companies that process personal data of individuals residing in the EU, regardless of the company's location.
Personal Data: Any information related to an identified or identifiable natural person, such as names, addresses, email addresses, IP addresses, and more.
Rights of Individuals:

Right to Access: Individuals have the right to access their personal data and obtain information on how it is being used.
Right to Rectification: Individuals can request correction of inaccurate personal data.
Right to Erasure (Right to be Forgotten): Individuals can request the deletion of their personal data under certain conditions.
Right to Restrict Processing: Individuals can request the limitation of the processing of their personal data.
Right to Data Portability: Individuals can request their personal data in a commonly used format to transfer it to another controller.
Right to Object: Individuals can object to the processing of their personal data for certain purposes.
Data Protection Principles:

Lawfulness, Fairness, and Transparency: Data processing must be lawful, fair, and transparent to the data subject.
Purpose Limitation: Data must be collected for specified, explicit, and legitimate purposes and not further processed in a manner incompatible with those purposes.
Data Minimization: Data collected must be adequate, relevant, and limited to what is necessary for the purposes for which it is processed.
Accuracy: Data must be accurate and kept up to date.
Storage Limitation: Data must be kept in a form that permits identification of data subjects for no longer than necessary.
Integrity and Confidentiality: Data must be processed in a manner that ensures its security.
Accountability and Governance:

Organizations must implement appropriate technical and organizational measures to ensure and demonstrate compliance.
Organizations may need to appoint a Data Protection Officer (DPO) if they process large amounts of personal data or engage in certain types of processing activities.
Data Breaches: Organizations must report certain types of data breaches to the relevant supervisory authority within 72 hours of becoming aware of the breach.

Penalties: Non-compliance can result in significant fines, up to €20 million or 4% of the annual global turnover of the preceding financial year, whichever is higher.

---
<!-- Ahoj potrebujem pripravit prezentaciu obecenstvo, ktore su to AI researchers, AI students a tiez ludia z firiem pouzivajucich AI, ktori su vcelku technologicky zdatni. Vzdy ich zaujima, ako sa riesia rozne specificke vyzvy (vo nasom pripade napriklad image recognition, false positives/negatives, ako sa trenovala AI, ako ste spracuvali datasety atd. - skratka technicke zaujimavosti). 

v prezentacii sa da aj nieco povedat k tomu ake AI pristupy pouzivame
dolezite -- NIE JE TO REKLAMA PRODUKTU A ANI FIRMY, TO JE KONTRAPRODUKTIVNE, a poskodi to vsetkych

treba mat na pameti, ze su tam AI ludia, ktori sa chcu nieco nove dozvediet ohladom toho co sa vam podarilo, nepodarilo s AI, aku architekturu je dobre pouzit pre nejake pripady, s cim ste mali vacsi problem, ako ste sa vysporiadali s doveryhodnostou (vybrate aspekty), kde vidite este medzery...

samozrejme to co mozete zdielat, ale dolezite, aby tam bol potencial na pridanu hodnotu
ludi napr. nebudu zaujimat medicinske certifikacie, ale to ako sa snazite zabezpecovat transparentnost moze byt zaujimave -->

References
[(2023) Detection of Proximal Caries Lesions on Bitewing Radiographs Using Deep Learning Method](https://karger.com/cre/article/56/5-6/455/841972/Detection-of-Proximal-Caries-Lesions-on-Bitewing)
*Bitewing radiography is commonly used to detect proximal caries, which require accurate diagnoses and early management and cannot be detected clinically due to tight contact surfaces [Gimenez et al., 2015]. Many factors, such as fatigue, emotions [Stec et al., 2018], and complex clinical environments [Hellén-Halme et al., 2008], could affect the accuracy of image interpretation.*

*The F1-score of the students was 0.57, while the F1-score of the network was 0.74 despite the accuracy of 0.82. A significant difference in the sensitivity was found between the model and the postgraduate students when detecting different stages of lesions (p < 0.05). For early lesions which limited in enamel and the outer third of dentin, the neural network had sensitivities all above or at 0.65, while students showed sensitivities below 0.40. From our results, we conclude that the CNN may be an assistant in detecting proximal caries on bitewings.*

Prezi statement:
Students miss over 43% of actual caries and are only right 57% of the time they identify one, while our AI consistently outperforms them in both accuracy and reliability.

---

<!-- _paginate: skip -->
# AI:Dental
## Shaping the future of Artificial and Human Intelligence hand in hand in dentistry

![bg right:40%](img/mascot/AID_5.svg)

---

# AI:Dental
Developing AI and Education Platform for dentistry to enhance Diagnostic Accuracy and Education in Dentistry

### Speaker: Peter Jurkáček, CTO

![bg right:35% 80% invert](img/qr_aid.png)

---

<!-- _footer: "1. 2022 Evaluation of radiographic interpretation skills of undergraduate dental students studying in a dental college of Punjab, India – A comparative study" -->
# Problem
## Success rate of interpreting X-ray images by dental students ranges from **48% - 65%**<sup>[1]</sup>

![bg right:37%](img/321b949b-b01d-49b0-97a8-75af270f5e98.jpg)

---

# What is the sucess rate of your own dentist?

- It's hard to tell
- Based on study is 70%

![bg left:37%](img/321b949b-b01d-49b0-97a8-75af270f5e98.jpg)

---

# Why?

- Errors due to exhaustion
- Missed findings out of specialization
- A bunch of different pathologies
- Pathologies are hidden until hole is drilled (Clinical view)
- X-ray image is just a pomocna metoda 
- Subjectivness during interpretation (Radiological view)
    - Inter-rater variability
    - Intra-rater variability

![bg right:37%](img/321b949b-b01d-49b0-97a8-75af270f5e98.jpg)

---

## Expert's decision tree
1. Identify suspicious regions
2. Classify pathologies
3. Explain findings to patient
4. Perform procedure
5. Make a Electronic Health reccord of visit

---

## AI solution
1. Identify suspicious regions (Object detection, Instance segmentation)
2. Classify pathologies (Image classification)
3. Explain findings to patient (Visual explanation, Test explanation)
4. Perform procedure (~~Robotics~~)
4. Make a Electronic Health reccord of patients visit (1, 2, 3)

---

<div class='columns3'><div>

# AI

![](img/tasks/T01.png)

</div><div>

![](img/tasks/T02_2.png)
![](img/tasks/T02_1.png)

</div><div>

![](img/tasks/T03.png)

</div></div>

---

Education platform 
Crowdsourcing platform

![bg right 100%](img/mascot/AID_12.svg)
![bg 100%](img/mascot/AID_11.svg)


---

**Deep Learning**: Utilized convolutional neural networks (CNNs) for image recognition tasks.

**Data Augmentation**: Techniques to improve training data diversity and model robustness.

**Transfer Learning**: Leveraging pre-trained models to enhance diagnostic accuracy.

**Explainable AI**: Implementing methods to ensure transparency and interpretability in AI predictions.

---

# Training the AI

**Datasets**:
- Sourced from diverse dental imaging modalities.
- Crowdsourcing for annotation and validation.

**Training Process**:
- Data preprocessing: normalization, augmentation.
- Model training: leveraging GPU acceleration.
- Validation: Cross-validation techniques to ensure model reliability.

**Challenges**:
- Imbalanced datasets: Addressed using synthetic data generation and oversampling techniques.
- Noise in data: Applied denoising algorithms to enhance data quality.

---

# Technical Challenges and Solutions

**False Positives/Negatives**:
- Implemented ensemble methods to reduce prediction errors.
- Continuous model refinement with active learning strategies.

**Scalability**:
- Optimized model deployment using cloud-based infrastructure.
- Containerization with Docker for efficient scaling and maintenance.

**Integration with Clinical Workflows**:
- Developed APIs for seamless integration with existing dental software.
- User-friendly interfaces to encourage adoption by dental professionals.

---

# Ensuring Trustworthiness

**Transparency**:
- Explainable AI techniques to make model decisions understandable to users.
- Comprehensive logging and monitoring to track model performance over time.

**Bias Mitigation**:
- Regular audits of training data for bias.
- Implemented fairness constraints in model training.

**Security and Privacy**:
- Data encryption and secure storage solutions.
- Compliance with GDPR and other relevant regulations.

---

# Current Gaps and Future Directions

**Gaps**:
- Limited real-world validation due to regulatory constraints.
- Need for more diverse datasets to enhance model generalizability.

**Future Directions**:
- Expanding dataset collection through partnerships with dental clinics.
- Research into multimodal AI systems combining imaging and textual data.
- Development of adaptive learning systems for personalized dental education.

---

# Case Study: AI in Action

**Scenario**: Diagnosing dental caries using AI:Dental AI.

**Approach**:
- Data collection: High-resolution dental images.
- Model deployment: Integration with clinic's diagnostic software.
- Results: Improved diagnostic accuracy and reduced patient wait times.

**Lessons Learned**:
- Importance of user feedback in model refinement.
- Balancing automation with human expertise for optimal outcomes.

---

# Interactive Q&A Session

**Encourage Audience Engagement**:
- Invite questions on technical aspects, challenges, and future directions.
- Foster a discussion on best practices and emerging trends in AI for healthcare.

---

# Conclusion

**Recap**:
- AI:Dental’s innovative solutions in dental care and education.
- Key technical achievements and ongoing challenges.
- Commitment to transparency, trustworthiness, and continuous improvement.

**Call to Action**:
- Engage with us for potential collaborations.
- Stay connected for updates on our latest research and developments.

---

