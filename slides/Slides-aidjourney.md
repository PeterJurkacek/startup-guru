---
marp: true
theme: custom-default
paginate: true
footer: AI:Dental
---

# Ako sme učili AI rozumieť X-rayom
## AI:Dental

![bg right](img/ai_output.png)

--- 

# Problem

## Zubár
- Nekonzistentnosť
- Subjektivita
## Poisťovňa
- Žiadna kontrola

---

# Riešenie
## Poskytnúť systém, ktorý objektívne posúdi RTG snímku
- UC01 Nájdenie kazu
<!-- ![bg vertical right w:300](img/tf_ucs/uc01.jpg)
![bg w:300](img/tf_ucs/uc02.jpg) -->
![bg right ](img/tf_ucs/uc03.jpg)

---
# Dostupné datasety v zubarine?
- Osobné údaje
- Chýbajúce súhlasy pacientov
- Chýbajúce metadáta o pacientov

![bg vertical left](img/tf/04.png)
![bg](img/tf/05.png)

---
# Vytvorenie vlastného datasetu

![bg vertical right](img/tf/06.png)
![bg](img/tf/07.png)

*140 snímok, 2 zubári, 5 mesiacov*
- 716 Kazy
- 928 Sklovina
- 842 Dentín
- 430 Plomba
- 155 Koreňová výplň

---

# UC01 Nájdenie kazu AI vs Zubár

- modrá (lekár)
- červená (ai)
- zelená (zhoda)

![bg right:65% vertical](img/tf/08.png)
![bg](img/tf/09.png)

---

# UC02 Chýbajúca koreňová výplň
- Segmentácia
![bg right:50%](img/tf/07.png)

---
# UC02 Chýbajúca koreňová výplň
- Redefinovanie ~~Segmentácie~~ na **detekciu**
![bg left:50%](img/tf/10.png)

---

# Nový dataset

-1000 snímok, 2 skupiny po 6 zubárov, **2 mesiace**
- 1515 koreňových výplní
- ~600 chýbajucich koreňových výplní
- ~600 periapikálnych lézií

![bg left:50%](img/tf/11.png)

---

## Zatiaľ sme pokryli len 2-3 problémy a stálo nás to approx. 1 rok práce

![bg right 90%](img/mascot/AID_0_sad.svg)

---

## Rozhodovací strom zubára

![bg right:60% w:700](img/sankey.svg)

---

# Ako na to ideme teraz?

---
# Anotované dáta priamo z kliniky 
![](img/semafor.png)

---

## Kontrola kvality dát pomocou Edukačnej platformy

![bg right:60% 90%](img/edu/4.png)

---

## Podarilo sa nám oanotovať

![bg right:60% w:900](img/edu/14.png)

---

## Lessons learnt

- Vážte si ľudí čo challanguju vaše riešenia
- Pokiaľ chcete trénovať vlastnú AI bez dát to nepôjde
- (Update 2024) AI si viete integrovať aj bez toho aby ste ju trénovali
