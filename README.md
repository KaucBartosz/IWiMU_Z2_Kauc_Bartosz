## Konsultacja wstecz

Przykładowa konsultacja systemu wspomagającego wybór ścieżki specjalizacji na studiach. Po strzałce podano odpowiedź użytkownika.

```text
=== Wnioskowanie wstecz ===
Który obszar najbardziej Cię interesuje? (programowanie/sieci/grafika/analiza danych) → programowanie
Wolisz pracować indywidualnie czy zespołowo? (indywidualny/zespolowy) → zespolowy
Jaka jest Twoja ocena z matematyki? → 4.2
Polecam: BACKEND
Reguły: R4 -> R1 -> R8
```

System rozpoczął od ustalenia profilu na podstawie preferowanego obszaru. Następnie zapytał o tryb pracy i ocenę z matematyki, ponieważ te dane są potrzebne do sprawdzenia reguły prowadzącej do decyzji BACKEND. Nie pytał o znajomość programowania, gdyż obecne reguły nie wykorzystują tego atrybutu. Odpowiedzi są zapamiętywane, więc system nie zadaje ponownie tego samego pytania.

## Strategia rozwiązywania konfliktów reguł

W bazie obowiązuje kolejność reguł: pierwsza pasująca reguła ustalająca dany wniosek ma pierwszeństwo, a ustalony fakt nie jest nadpisywany. Reguły decyzji są umieszczone po regułach ustalających wnioski pośrednie, dzięki czemu ich przesłanki mogą zostać najpierw wyprowadzone.

Test konfliktu tworzy kopię bazy w pamięci i wstawia przed regułami decyzji regułę `KONFLIKT`, która dla profilu technicznego proponuje DATA SCIENCE. Dla tych samych danych wejściowych wynik testowy to DATA SCIENCE, ponieważ ta reguła sprawdzana jest przed właściwą regułą BACKEND. Bez reguły testowej system wskazuje BACKEND. Test pokazuje, że kolejność konkurujących reguł wpływa na wynik; oryginalny plik bazy nie jest zmieniany przez test.

## Uruchamianie

Polecenia należy uruchamiać z katalogu głównego projektu:

```text
python se/sprawdz_format.py wiedza/moja_dziedzina.json
python se/test_silnik.py
python se/test_moja_dziedzina.py
```

`moja_dziedzina.json` zawiera 27 reguł. Testy własnej bazy sprawdzają pięć przypadków wnioskowania w przód i wstecz, w tym próg 4.0 i brak wyniku, oraz osobny przypadek konfliktu reguł. `test_silnik.py` jest dostarczonym autotestem przykładowej bazy kawy.
