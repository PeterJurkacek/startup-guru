---
marp: true
theme: custom-default
paginate: true
footer: AI:Dental
---

# Ako sme učili AI interpretovať RTG snímky
## AI:Dental

![bg right:40%](img/mascot/AID_1.svg)

--- 

<!-- _color: '#000' -->
<!-- _footer: "" -->
# Brief Intro
<!-- "Hi everyone, I'm [Your Name], the CTO of [Your AI Company]. Beyond the world of technology, I'm passionate about sports, enjoy a good cup of coffee, and appreciate the art of craft beer. Today, I'm not just here to talk tech; I'm open to connecting on shared interests. Scan the QR code on my Linked for a virtual meetup. Let's dig in"
-->
![bg opacity right](img/57e2696d-f37a-4111-8f3d-72bada4c77c5.JPG)

Peter Jurkáček
CTO at AI:Dental


<div class="aid" style="
text-align:center;
vertical-align:middle;
padding-top:30px;
width:412px;
">

<img class=aid-img src='img/qr_1.png'>

`peter.jurkacek@aidental.ai`
</div>

--- 

# Ako sme začali, pokračovali a neprestávali s AI

--- 

### Ako sme začali?
# Znalosť domény
- Interpretácia RTG snímok
- Zubár, Pacient
- Anotácie / Posudok / Patológia / Kaz / Plomba


![bg right:40%](img/321b949b-b01d-49b0-97a8-75af270f5e98.jpg)

--- 

### RTG snímka
# Pohľad pacienta
- Vidí zuby, plomby

![bg right:60%](img/tf/15.png)

--- 

### RTG snímka
# Pohľad zubára
- Kazy niesú viditeľné volným okom  
- Pomocná metóda

![bg right:60%](img/tf/16.png)

---

### Máme znalosť, čo potom?
# Identifikácia problému

![bg right:60% w:750](img/tf/13.png)

---

### Pohľad 6 zubárov
# Subjektivita
- 3 našli, 3 nenašli
- Únava
- Rôzne skúsenosti
![bg right:60% w:750](img/tf/14.png)

---

### Pohľad 1 zubára
# Konzistetnosť
- Niektoré patológie nemajú presne definované hranice

![bg right:60% w:700](img/tf/12.png)

---

### Identifikovali sme problém, čo potom?
# Zadefinovali sme si prípady použitia

---

### Zadefinovali sme si prípady použitia
# Prípady použitia
- > UC01: Identifikácia kazu
- > UC02: Ident. chýbajúcej koreňovej výplne
- UC03: Posúdene kvality plomby
- UC04: ...
![bg left w:500](img/mascot/AID_0_smile.svg)


<!-- ![bg vertical left](img/tf/06.png)
![bg](img/tf/07.png) -->

---

### Ako sme využili prípady použitia?
# Analýza existujúcich prístupov

---

### Analýza existujúcich prístupov
# Existujúce prístupy
- Komerčné vs Výskum
- Prístupy: 
    - Segmentácia, Detekcia, Klasifikácia
- Datasety
    - Chýbajúce súhlasy pacientov
    - Chýbajúce metadáta o pacientoch
    - Snímka je osobný údaj

![bg vertical left](img/tf/04.png)
![bg](img/tf/05.png)

---

### Ako sme využili analýzu?
# Návrh riešenia

---

# Návrh riešenia

![bg vertical right](img/tf/06.png)
![bg](img/tf/07.png)

- Semantická segmentácia
- Vlastný dataset
- > UC01: Identifikácia kazu
- > UC02: Ident. chýbajúcej koreňovej výplne

---

### Realizácia
# Vytvorenie vlastného datasetu
140 snímok, 1 zubár, 2 mesiace
- > 716 Kazov
- > 88 Chýbajúca výplň

![bg vertical left](img/tf/06.png)
![bg](img/tf/07.png)

---

### Realizácia
# Natreńovanie vlastného modelu
> UC01 Identifikácia kazu 
- modrá (zubár)
- červená (ai)
- zelená (zhoda)

![bg right:50% vertical w:650](img/tf/08.png)
![bg w:650](img/tf/09.png)

---

### Neboli sme spokojní s výsledkom
# Ladenie / Redizajn
- Zlepšiť dataset
- Zlepšiť model
- Redefinovať problém & riešenie

![bg left](img/mascot/AID_15.svg)

---

### Neboli sme spokojní s výsledkom
# Ladenie / Redizajn
- ~~Zlepšíme dataset~~
- ~~Zlepšíme model~~
- Redefinovať prípady použitia

![bg left](img/mascot/AID_15.svg)

---

# Redefinovať prípady použitia
- Naozaj potrebujeme segmentovať kaz? -> Nie
    * Zubárovi stačí keď budeme vedieť identifikovať choré zuby
    * > UC01: Posúdenie prítomnosti kazu na zube
- Naozaj potrebujeme segmentovať chýbajúcu koreňovú výplň? -> Nie
    * Zubára zaujíma zlá kvalita koreňovej výplne, ktorá môže spôsobiť vznik lézie
    * > UC02: Posúdenie kvality koreňovej výplne zuba
    * > UC03: Posúdenie prítomnosti lézie pri zube

<!-- ![bg right:20% 100%](img/mascot/AID_15.svg) -->

---

### Checli sme aby to bolo škálovateľné
# Rozhodovací strom zubára

![bg right:60% 90%](img/sankey.svg)

---

### Checli sme aby to bolo škálovateľné
> UC01: Posudzovanie problémov na zube
![bg right:60% 90%](img/sankey.svg)

---

# Museli sme začať od znova
- Analýza existujúcich prístupov
- Návrh riešenia
- Realizácia
- Ladenie / Redizajn

![bg right 90%](img/mascot/AID_0_sad.svg)

---

### Realizácia
# Vytvorenie nového datasetu
- ~~140 snímok, 1 zubár,~~ 2 mesiace
    - 1000 snímok, 1 zubár

- ~~88~~ chýbajucich koreňových výplní
    - 600 chýbajucich koreňových výplní
    - 600 periapikálnych lézií

![bg left:50%](img/tf/11.png)
 
---

# Aktuálny stav?
![bg right 90%](img/mascot/AID_0_smile.svg)

---

### Napojili sme sa na dátový zdroj
# Klinické dáta
- Anotovanie dát pri každej návšteve pacienta 
- Zubný kríž (Čísla zubov so zoznamom patológií)
![bg right:50% vertical 100%](img/tf/17.png)
![bg right 100%](img/tf/18.png)

---

### Aktuálny stav
# Kontrola kvality dát
- Edukačná platforma a crowdsourcing

![bg vertical right:50% 100%](img/edu/4.png)
![bg right:50% 100%](img/edu/17.png)

---

### Aktuálny stav?
# AI:Dental
- 4M posudkov
- Dataset 58 nálezov
- Aktuálne naša AI okolo 10 nálezov
- Pripravujeme sa na klinickú evaluáciu

![bg right 90%](img/mascot/AID_0_smile.svg)

---

# Final thoughts ako začať a neprestávať
1. Znalosť domény
2. Identifikácia problému
3. Identifikovať prípady použitia
4. Analýzovať existujúce prístupy
5. Návrhnúť riešenie
6. Realizovať
7. Ladiť / Redizajnovať
