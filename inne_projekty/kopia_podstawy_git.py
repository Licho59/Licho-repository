PODSTAWY GIT:

1.Założenie repozytorium na 2 sposoby:
- z poziomu katalogu projektu(w Bashu) wykonać polecenie < git init > (co stworzy nowy katalog o nazwie .git wraz z niezbędnymi plikami)
- sklonowanie istniejącego repozytorium z innego serwera(np. z GitHuba – kopiowanie linka protokołu https!, SSH jest dodatkowym protokołem wymagającym klucza) – poprzez polecenie < git clone ‘link’>

2. Rozpoczęcie kontroli wersji istniejących plików:
- śledzenie plików rozpoczyna się od utworzenia początkowej rewizji,
- polecenia:
<git add file.ext > - (dodaje pojedynczy plik lub ‘< git add . >’ dodaje wszystkie zmodyfikowane oraz nieśledzone pliki) = w terminologii git jest to tzw. ‘stage’
<git add README > -
<git commit –m ‘initial project version’> - zatwierdzanie zmian od razu z komentarzem w cudzysłowiu,
<git reset HEAD file.ext > - cofa dodany plik(lub wszystkie) ze śledzenia,
<git status > - sprawdza status plików w repozytorium,
- pliki śledzone(to te, które znalazły się w ostatniej migawce) mogą być niezmodyfikowane, zmodyfikowane lub oczekiwać w poczekalni(po dodaniu ich poleceniem add),
- pliki nieśledzone – widziane przez Git (czerwony kolor) poprzez porównanie z ostatnią migawką, ale ich śledzenie rozpocznie się dopiero po wydaniu polecenia < git add >,
- utworzenie nowego pliku(np. w repozytorium) z poziomu wiersza poleceń poprzez edytor Windowsa < notepad file.ext > lub w macOS < vim file.ext > .

3. Dodawanie zmodyfikowanych plików do poczekalni:
- < git add file.ext > - wysyła zmodyfikowany plik do poczekalni(był w trybie śledzenia z poprzedniej migawki),
- < git status > - pozwala sprawdzić aktualny stan plików w repozytorium,
- ewentualne dodatkowe zmiany w pliku wymagają ponownie polecenia < git add file.ext >, inaczej polecenie zatwierdzające uwzględni tylko pierwszą modyfikację,
- < git diff > - pokazuje wszystkie zmiany dokonane w plikach jeszcze przed wysłaniem do poczekalni (w odróżnieniu od < git status >),
- < git diff –staged > - pokazuje wszystkie zmiany przekazane do poczekalni, zanim zostaną zatwierdzone(z ang. commited).

4. Zatwierdzanie zmian:
- w Windows warto wskazać nazwę edytora, który będzie użyty w trakcie commitu ( < git config –global core.editor notepad > , w macOS domyślny jest Vim),
- < git commit > - zatwierdzenie zmian w repozytorium, po którym następuje uruchomienie edytora w celu podania charakterystyki wprowadzonych zmian,
- < git commit –v > - do komentarza trafią również zmodyfikowane wiersze,
- < git commit –m ‘initial project version’> - zatwierdzanie zmian od razu z komentarzem w cudzysłowiu.
- pomijanie poczekalni poprzez < git commit –a – m ‘actualized READMI’> (opcja ‘- a’ zastępuje add, ‘-m’ jest komentarzem do rewizji) – obejmuje wszystkie pliki śledzone.
-----------------------------------------------------