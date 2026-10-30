# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
 1: dict(n="Martin Kološ", y="* 1981", st="fam", sex="M", f=["* 1981 Nový Jičín"], r=[], note="Žijící – údaje jen základní."),
 2: dict(n="Milan Kološ", y="* 1959", st="fam", f=["* 1959 Ostrava"], r=[], note="Žijící – údaje jen základní."),
 3: dict(n="Alena Rebrošová", y="* 1960", st="fam", f=["* 1960"], r=[], note="Žijící – údaje jen základní."),
 4: dict(n="Oldřich Kološ", y="* 1935", st="fam", f=["* 21. 12. 1935"], r=[],
         note="Strom MyHeritage: zemřel, datum úmrtí neuvedeno."),
 5: dict(n="Marie Spurná", y="* 1936", st="fam", f=["* 1936"], r=[],
         note="Strom MyHeritage neuvádí úmrtí – zatím vedena jako žijící (údaje jen základní)."),
 8: dict(n="Oldřich Kološ", y="* 1911", st="fam", f=["* 8. 9. 1911 Starý Jičín"], r=[],
         note="Strom MyHeritage: zemřel, datum úmrtí neuvedeno."),
 9: dict(n="Štěpánka Stodůlková", y="* 1913", st="fam", f=["* 31. 7. 1913"], r=[],
         note="Strom MyHeritage: zemřela, datum úmrtí neuvedeno."),
 16: dict(n="Viktor Kološ", y="* 1886", st="fam", f=["* 14. 12. 1886", "× Aloisie Mocková"], r=[]),
 17: dict(n="Aloisie Mocková", y="* 1886", st="fam", f=["* 8. 10. 1886", "× Viktor Kološ"], r=[]),
 18: dict(n="František Stodůlka", y="* 1883", st="fam", f=["* 13. 4. 1883"], r=[]),
 19: dict(n="Emilie Kantorová", y="* 1888", st="fam", f=["* 11. 4. 1888"], r=[]),
 32: dict(n="Valentin Kološ", y="", st="fam", f=[], r=[], note="Strom MyHeritage: bydliště Klokočov."),
 33: dict(n="Mariana Veselková", y="", st="fam", f=[], r=[], note="Strom MyHeritage: bydliště Klokočov."),
 34: dict(n="Alois Mocek", y="", st="fam", f=[], r=[], note="Strom MyHeritage: bydliště Lešná."),
 35: dict(n="Františka Bajarová", y="", st="fam", f=[], r=[], note="Strom MyHeritage: bydliště Vysoká."),
 36: dict(n="Jan Stodůlka", y="", st="fam", f=[], r=[]),
 37: dict(n="Marie Frydrych", y="", st="fam", f=[], r=[],
          note="Ve stromu MyHeritage příjmení v mužském tvaru – správně asi Frydrychová; ověřit v matrice."),
 38: dict(n="Josef Kantor", y="", st="fam", f=[], r=[]),
 39: dict(n="Barbora", y="", st="fam", f=[], r=[], note="Rodné příjmení ve stromu chybí."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
 8: ("Kološové", "Hlavní rod. Podle rodinného stromu z Klokočova, ve 20. století Starý Jičín."),
 9: ("Stodůlkovi", "Rod prababičky Štěpánky Stodůlkové (* 1913)."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
 ("Kdo byli rodiče Marie Spurné (* 1936)?", "Otevřené: ve stromu chybí."),
 ("Kdo byli rodiče Aleny Rebrošové (* 1960)?", "Otevřené: ve stromu chybí."),
 ("Kde se narodili Viktor Kološ (* 1886) a Aloisie Mocková (* 1886)?", "Otevřené: rodinný strom uvádí jen data; rodiče bydleli v Klokočově a v Lešné."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
