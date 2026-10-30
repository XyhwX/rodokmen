# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


- kontrola.py hlásí „rod má už 6 generací – je čas napsat příběh“ hned po importu GEDCOM, i když nic není doložené
  (všechno `fam`). Asi počítat jen generace se stavem `doc`/`prob`.
- Odkazy na fotky v GEDCOM exportu z MyHeritage (sites-cf.mhcache.com) vrací z cloudového prostředí HTTP 403.
- ZA Opava z cloudového prostředí: i po povolení digi.archives.cz a images.archives.cz přesměruje ochrana proti robotům
  na validate.perfdrive.com (Radware) – bez povolení té domény a bez člověka na CAPTCHA to nejde. Playwright hlásí jen
  ERR_TUNNEL_CONNECTION_FAILED, skutečnou příčinu ukáže až stav proxy (recentRelayFailures).
