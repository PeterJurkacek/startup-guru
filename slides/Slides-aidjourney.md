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

# Problem
- Nekonzistentnosť zubárov
- Subjektivita zubárov

![bg right:60% w:700](img/tf/12.png)

---

## Návrh riešenia
### Poskytnúť systém, ktorý objektívne posúdi RTG snímku
> UC01 Nájdenie kazu
<!-- ![bg vertical right w:300](img/tf_ucs/uc01.jpg)
![bg w:300](img/tf_ucs/uc02.jpg) -->
![bg right 90%](img/tf/03.jpg)

---
# Dostupné datasety v zubarine?
- Osobné údaje
- Chýbajúce súhlasy pacientov
- Chýbajúce metadáta o pacientoch

![bg vertical left](img/tf/04.png)
![bg](img/tf/05.png)

---
# Vytvorenie vlastného datasetu

![bg vertical right](img/tf/06.png)
![bg](img/tf/07.png)

140 snímok, 2 zubári, **5 mesiacov**
> - 716 Kazov
- 928 Sklovina
- 842 Dentín
- 430 Plomba
- 155 Koreňová výplň
- 88 Chýbajúca výplň

---

> UC01 Nájdenie kazu 
- modrá (zubár)
- červená (ai)
- zelená (zhoda)

![bg right:50% vertical w:650](img/tf/08.png)
![bg w:650](img/tf/09.png)

---

## Čo vieme spraviť aby sme mali konzistentnejšie anotácie?
- Zlepšíme fokus zubára: ~~celá snímka~~ -> konkrétny zub
- Zjednodušíme anotovanie ~~kreslenie~~ -> klasifikácia

---

> UC01 Posudzovanie zubov na prítomnosť kazu
- Konkrétny zub, Klasifikácia
- Detekcia, Klasifikácia zubov

![bg right:60% 95%](img/edu/16.png)

---

> UC02 Segmentácia chýbajúcej koreňovej výplne
![bg right:50%](img/tf/07.png)
- 88 polygónov chýbajúcej výplňe

---

> UC02 Klasifikácia koreňov s chýbajúcou koreňovou výplňou
- Namiesto polygónov budeme zberať detekované korene a klasifikovať
![bg left:50%](img/tf/10.png)

---

## Vytvorenie nového datasetu
~~140 snímok, 2 zubári, 5 mesiacov~~
1000 snímok, 2 skupiny po 6 zubárov, **2 mesiace**

1515 koreňových výplní, **600 chýbajucich koreňových** výplní a navyše aj **periapikálnych lézií**

![bg left:50%](img/tf/11.png)

---

Zatiaľ sme pokryli len 2-3 problémy a stálo nás to approx. 1 rok práce
- Vačšina bola práca s dátami

![bg right 90%](img/mascot/AID_0_sad.svg)

---

## Rozhodovací strom zubára

![bg right:60% w:700](img/sankey.svg)

---

# Ako na to ideme teraz?

---
# Anotované dáta priamo z kliniky 
- Zubný kríž -> Zub + patológie + liečby
![](img/semafor.png)

---

# Kontrola kvality dát
## Edukačná platforma a crowdsourcing

![bg right:50% 90%](img/edu/4.png)

---

## Podarilo sa nám oanotovať approx. 
    - 120K zubov
    - 1M posudkov

![bg right:60% w:900](img/edu/14.png)

---

## Lessons learnt
- Vážte si ľudí čo challanguju vaše riešenia
- Pokiaľ chcete trénovať vlastnú AI bez dát to nepôjde
- (Update 2024) AI si viete integrovať aj bez toho aby ste ju trénovali
