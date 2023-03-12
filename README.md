## Akademia Górniczo-Hutnicza

### Wydział Elektrotechniki, Automatyki, Informatyki i Elektroniki

### Kierunek Informatyka Data Science

## Informatyka Systemów Złożonych

# Projekt

### Algorytmy budowania fraktalnych krajobrazów

### Jakub Robak, Maciej Ługowski

### Kraków, 15 Stycznia 2023


## 1 Wprowadzenie

Fraktalne krajobrazy to obrazy generowane przez matematyczne algorytmy Są one szczególnie interesujące, ponieważ mają
nieregularną strukturę, która jest podobna na różnych skalach. Fraktale są często używane w grafice komputerowej, pro-
jektowaniu architektonicznym i naukach przyrodniczych, poniewzaż ich nieregularna struktura jest podobna do naturalnych
krajobrazów, takich jak góry, rzeki i drzewa. Algorytmy fraktalne pozwalają na generowanie realistycznie wyglądających
krajobrazów z minimalną ilością danych, co jest szczególnie przydatne w przypadku symulacji komputerowych. Oznacza że
często używa się ich do generowania elementów krajobrazu w filmach lub generowania losowych map w grach video.

## 2 Algorytmy generowania krajobrazów fraktalnych

Obecnie jest dużo sposobów na generowanie fraktalnych krajobrazów. W projekcie uwzględniamy 2: Triangle Division Algo-
rithm oraz Diamond-Square Algorithm, które są jednymi z najskuteczniejszych. Oba polegają na wygenerowaniu macierzy o
rozmiarze NxN zawierającej współrzędne punktów. W następnych punktach zostanie opisany opis działania algorytmów.

### 2.1 Triangle Division Algorithm

Na początku wybieramy ’s’ będące parametrem pochyłości stoku. Im większa wartość ’s’ tym większe są różnice w wyso-
kościach. Trzeba również wybrać rozmiar parametr ’N’ który będzie oznaczał wielkość planszy - 2 N. Algorytm przebiega
następująco:

- Wybranie Pierwszego Trójkąta (Na połowie macierzy) poprzez zainicjalizowanie wybranymi wartościami jego wierz-
    chołków.
- Następnie wybierane są punkty na środku utworzonych krawędzi. Ich wartość wynosi średnią z punktów leżących na 2
    sąsiednich wierzchołkach powiększoną o liczbę z przedziału[−ks:ks]gdziekto długość krawędzi trójkąta
- Podział trójkąta na 4 mniejsze poprzez połączenie ze sobą punktów utworzonych w poprzednim kroku oraz powtórzenie
    poprzednich punktów.

Po zakończeniu wykonywania kroków należy powtórzyć operację dla 2 trójkąta

### 2.2 Diamond-Square Algorithm

Algorytm przebiega następująco:

- Zaczynamy od ustawienia wszystkich narożników na tę samą losową wartość:
- Następnie ustawiamy środek tak, aby był średnią z 4 rogów plus losowa wartość.
- I ustaw punkt środkowy każdej krawędzi jako średnią swoich punktów narożnych plus losowa wartość.


## 3 Wizualizacja

Algorytmy zwracają macierz z wysokością punktów. Do wizualizacji tej macierzy została użyta biblioteka mayavi która po-
zwala utworzyć rzut 2d oraz 3d. Wraz ze wzrostem rozmiaru macierzy generowane są większe oraz bardziej szczegółowe mapy.
Biblioteka Myavi pozwala również zmieniać motyw kolorystyczny przez co można uzyskać różne typy terenu. Tak wygląda
przykładowa mapa wygenerowana dla macierzy o rozmiarze 210.

```
Rysunek 1: Przykład mapy 3D z motywem ’terrain’
```
```
Rysunek 2: Przykład mapy 2D z motywem ’gist earth’
```

```
Poniższy obrazek przedstawia tą samą mapę. Zmieniony jest jedynie motyw kolorystyczny na różne odcienie brązu.
```
```
Rysunek 3: Przykład mapy 3D z motywem ’copper’
```
Powyższe obrazki przedstawiały plansze wygenerowane za pomocą algorytmu Diamond-Squar. Charakterystyczne jest, że
krajobraz przez niego wygenerowany przypomina kształtem kopce ponieważ punkt środkowy jest tworzony poprzez 4 punkty
znajdujące się w rogach kwadratu. Jeśli wylosowana permutacja jest ujemna dostajemy lej który w zależności od dobranej
kolorystyki może przypominać jezioro lub zagłębienie. Gdy wylosowana permutacja była pozytywna dostajemy kopiec będący
szczytem góry.

```
Rysunek 4: Przykład mapy 3D z motywem gist earth’
```

```
Rysunek 5: Przykład mapy 2D z motywem ’gist earth’
```
Powyższe obrazki są wygenerowane przy pomocy algorytmu Triangle Division Algorithm. Charakterystyczne dla tego
algorytmu jest tworzenie długich ciągów o podobnych wartiościach. Wynika to z zabrania średniej wartości z końców odcinka
będącego bokami trójkąta. Przez to podczas wizualizacji powstają długie i strome łańcuchy górskie oraz rzeki odpowiadające
małym wartością w macierzy.

## 4 Generowanie Dużej Planszy

Podczas pojedynczego wywołania algorytmu zwracana jest macierz NxN. Aby utworzyć ciekawsze plansze można połączyć
kilka takich macierzy z różnymi parametrami. Pozwala to na większe zróżnicowanie terenu.

### 4.1 Typy Plansz

Na potrzeby projektu zostały utworzone 3 typy plansz. Każda z nich reprezentowała inny BIOM

4.1.1 Góry

Jest to plansza z dużym parametrem pochylenia stoku. Zwracana macierz nie ma również wartościu ujemnych przez co na
wizualizacji na tych obszarach nie występuje woda. Dominującymi kolorami będzie tutaj brązowy oraz biały symbolizujące
ośnieżone szczyty gór. W zależności od użytego algorytmu tworzenia terenu możemy mieć różne typy gór. W Diamond-
Square Algorithm będą to częsciej pojedyncze góry przypominające kopiec. W Triangle Division Algorithm częściej będą
długie ciągnące się szczyty lub wąwozy wynikające z połączenia 2 trójkątów.

4.1.2 Doliny

Plansza ma mniejszy parametr pochylenia niż Góry. Mogą występować tutaj wartości ujemne przez co tworzą się woda.
Dominuje tutaj kolor zielony oznaczający w płaskie trawiaste tereny. Niebieskie elementy mogą być jeziorami które często
występują przy używaniu Diamond-Square Algorithm lub rzekami podczas używania Triangle Division Algorithm.

4.1.3 Woda

Plansza zawiera jednakowe małe wartości proporcjonalne do pozostałych plansz. Na początku woda ma płaskie dno. Płynnie
przechodzi jednak w płytsze oraz głębsze części.


### 4.2 Łączenie Plansz

Większa plansza składająca się z kilku biomów uzyskiwana jest poprzez połączenie kilku macierzy liczbowych w jedną wiekszą
macierz. Do pierwszej macierzy dostawiane są kolejne. Proces ten wykonwyany jest zarówno w pionie jak i poziomie. Na
obrazkach poniżej widać jedną dużą planszę połączoną z 9 mniejszych - po 3 z każdego typu. Duża plansza ma charakter
warstwowy na samym początku jest pas gór, następnie są doliny oraz morze. Problemem są przejścia pomiędzy mniejszymi
planszami. Można go rozwiązać poprzez wygładzenie oraz uśrednienie wartości macierzy w okolicy miejsc połączeń mniejszych
plansz.

```
Rysunek 6: Przykład mapy 3D
```
```
Rysunek 7: Przykład łączonej mapy 2D
```
## 5 Wygładzanie

Wygładzanie połączonych plansz było niezbędne aby pozbyć się ekstremów oraz aby łączena map były bardziej naturalne.
Krawędzie pomniejszych map nie były do siebie dopasowane oraz miały duże skoki wartości.
Do wygładzania wykorzystaliśmy dwie metody:

1. Dla przykładu z rysunku 3 stworzyliśmy tablicę która jest "przekątną"figury a następnie użyliśmy jej do wyrównania
    terenu. Wyrównywanie polegało na korekcji wartośći w macierzy w zależności od tego czy dana wartość była większa
    czy mniejsza od wartości macierzy "przekątnej"figury.


```
Rysunek 8: Przykład połączonej mapy 3D
```
```
Rysunek 9: Przykład "przekątnej"figury
```
Otrzymaliśmy następującą powierzchnię


```
Rysunek 10: Przykład mapy 3D po zastosowaniu wygładzania
```
```
Rysunek 11: Przykład mapy 2D po zastosowaniu wygładzania
```
2. Dalej można zauważyć skoki wartości, aby się ich pozbyć zastosowaliśmy inny sposób wyrównywania polegający na
    iteracji po mapie blokami a nastepnie korygowaniu ekstremów w tych blokach.


```
Rysunek 12: Przykład mapy 3D po zastosowaniu drugiego wygładzania
```
```
Rysunek 13: Przykład mapy 2D po zastosowaniu drugiego wygładzania
```
## 6 Wnioski

Do budowy fraktalnych krajobrazów wykorzystaliśmy dwa algorytmy, Triangle Division Algorithm oraz Diamond-Square
Algorithm. Największym problemem jaki napotkaliśmy, było połączenie mniejszych map w taki sposób aby krawędzie nie
były widoczne. Aby go skorygować, wykorzystaliśmy dwie metody wygładzania.


