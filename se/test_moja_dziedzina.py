from copy import deepcopy
from pathlib import Path
from silnik import wczytaj_baze, wnioskuj_w_przod, wnioskuj_wstecz

baza = wczytaj_baze(Path(__file__).parent.parent / "wiedza" / "moja_dziedzina.json")
CASES = [
 ({"preferowany_obszar":"programowanie","ocena_matematyki":4.2,"tryb_pracy":"zespolowy","znajomosc_programowania":"podstawowa"}, "BACKEND"),
 ({"preferowany_obszar":"analiza danych","ocena_matematyki":4.5,"tryb_pracy":"indywidualny","znajomosc_programowania":"zaawansowana"}, "DATA SCIENCE"),
 ({"preferowany_obszar":"programowanie","ocena_matematyki":4.0,"tryb_pracy":"indywidualny","znajomosc_programowania":"zaawansowana"}, "BACKEND"),
 ({"preferowany_obszar":"grafika","ocena_matematyki":3.2,"tryb_pracy":"zespolowy","znajomosc_programowania":"podstawowa"}, None),
 ({"preferowany_obszar":"sieci","ocena_matematyki":3.8,"tryb_pracy":"zespolowy","znajomosc_programowania":"podstawowa"}, "DEVOPS/SIECI"),
]
for facts, expected in CASES:
 forward, trace = wnioskuj_w_przod(baza, facts)
 answers=[]
 def ask(attr, reason):
  answers.append(attr); return facts[attr]
 backward_trace=[]
 backward=wnioskuj_wstecz(baza, "decyzja", {}, ask, backward_trace)
 assert forward.get("decyzja")==expected, (facts, forward, trace)
 assert backward==expected, (facts, backward, backward_trace)
 assert len(answers)==len(set(answers)), answers
 print(f"[OK] {expected!r}; przód={trace}; wstecz={backward_trace}; pytania={answers}")

# Konflikt: dokładamy konkurencyjną regułę i sprawdzamy pierwszeństwo pierwszej.
conflict=deepcopy(baza)
conflict["reguly"].insert(7, {"id":"KONFLIKT","jesli":[["profil","==","techniczny"]],"to":["decyzja","DATA SCIENCE"],"metafora":"Testowa reguła konkurencyjna.","coto":"Testowa decyzja."})
facts=CASES[0][0]
result, trace=wnioskuj_w_przod(conflict,facts)
assert result["decyzja"]=="DATA SCIENCE" and "KONFLIKT" in trace, (result,trace)
print("[OK] Konflikt: pierwsza pasująca reguła wygrywa")

