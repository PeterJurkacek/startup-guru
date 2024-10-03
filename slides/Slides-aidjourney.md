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

# Ako začať, pokračovať a neprestávať

--- 

### Ako začať?
# Znalosť domény
- Zubár, Pacient
- RTG snímka
- Anotácie / Posudok / Patológia / Kaz / Plomba
- Programátor
- ...

--- 

### RTG snímka
# Pohľad pacienta
- Vidí zuby, plomby

![bg right:60% w:750](img/tf/15.png)

--- 

### RTG snímka
# Pohľad zubára
- Kazy niesú viditeľné volným okom  
- Pomocná metóda

![bg right:60% w:750](img/tf/16.png)

---

### Čo potom?
# Pochopenie problému

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

### Čo potom?
# Identifikácia relevatných prípadov použitia

---

### Identifikácia relevatných prípadov použitia
- > UC01 Identifikácia kazu
- > UC02 Ident. chýbajúcej koreňovej výplne
- UC03 Posúdene kvality promby
- UC04 ...
![bg left w:500](img/mascot/AID_0_smile.svg)


<!-- ![bg vertical left](img/tf/06.png)
![bg](img/tf/07.png) -->

---

### Je to možné spraviť?
# Analýza existujúcich prístupov

---

### Analýza existujúcich prístupov
# Existujúce prístupy
- Komerčné vs Výskum
- Metódy: Segmentácia, Detekcia, Klasifikácia
- Datasety
    - Osobné údaje
    - Chýbajúce súhlasy pacientov
    - Chýbajúce metadáta o pacientoch

![bg vertical left](img/tf/04.png)
![bg](img/tf/05.png)

---

### Podme na to
# Návrh riešenia

---

# Návrh riešenia

![bg vertical right](img/tf/06.png)
![bg](img/tf/07.png)

- Semantická segmentácia
- Vlastný dataset

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

### Najdlhšia fáza
# Ladenie / Redizajn
- Zlepšiť dataset
- Zlepšiť model
- Redefinovať problém & riešenie

![bg left](img/mascot/AID_15.svg)

---

### Najdlhšia fáza
# Ladenie / Redizajn
- ~~Zlepšíme dataset~~
- ~~Zlepšíme model~~
- Redefinovať prípady použitia

![bg left](img/mascot/AID_15.svg)

---

# Redefinovať prípady použitia
- Naozaj potrebujeme segmentovať kaz? -> Nie
    * Stačí keď budeme vedieť identifikovať choré zuby
    * > UC01: Posúdenie prítomnosti kazu na zube
- Naozaj potrebujeme segmentovať chýbajúcu koreňovú výplň? -> Nie
    * Mali by sme vedieť posúdiť kvalitu koreňovej výplne
    * Mali by sme vedieť posúdiť prítomnosť lézie
    * > UC02: Posúdenie kvality koreňovej výplne zuba
    * > UC03: Posúdenie prítomnosti lézie pri zube

![bg right:20% 100%](img/mascot/AID_15.svg)

---

### Redefinovať prípady použitia
# Rozhodovací strom zubára

![bg right:60% 90%](img/sankey.svg)

---

### Redefinovať prípady použitia
> UC01 Posudzovanie zuba na prítomnosť problémov
    - kaz
    - nekvalitnej výplne
    - periapikálnej lézie
    - ...
![bg right:60% 90%](img/sankey.svg)

---

# Znova treba spraviť
- Analýza existujúcich prístupov
- Návrh riešenia
- Realizácia
- Ladenie / Redizajn

![bg right 90%](img/mascot/AID_0_sad.svg)

---

### Realizácia
# Vytvorenie nového datasetu
- ~~140 snímok, 1 zubár,~~ 2 mesiace
1000 snímok, 1 zubár

- ~~88~~ -> 600 chýbajucich koreňových výplní
- **600 periapikálnych lézií**

![bg left:50%](img/tf/11.png)
 
---

# Aktuálny stav?

---

### Aktuálny stav
# Napojenie sa na klinické dáta
- Anotovanie dát pri každej návšteve pacienta 
- Zubný kríž (Čísla zubov so zoznamom patológií)
![bg right:60% 90%](img/semafor.png)

---

### Aktuálny stav
# Kontrola kvality dát
- Edukačná platforma a crowdsourcing

![bg right:50% 90%](img/edu/4.png)

---

### Aktuálny stav?
- Dataset obsahuje viac ako 120 rôznych nálezov
- AI zatiaľ klasifikujeme okolo 10 nálezov pre každý zub
- Pripravujeme sa na klinickú evaluáciu

---

# Ak sa do toho chcete pustiť potrebujete
1. Znalosť domény
2. Pochopiť problém
3. Identifikovať prípady použitia
4. Analýzovať existujúce prístupy
5. Návrhnúť riešenie
6. Realizovať
7. Ladiť / Redizajnovať
