
def luckyNumbers(n, lucktab):   #funkcja zwracająca informację czy liczba jest liczbą szczęśliwą czy nie. (przeszukujemy listę luckyTab)
    for liczba in lucktab:
        if n==liczba:
            return True
    return False



counter = 0                      #licznik indeksu liczby, która jest aktualnie najnowszą szczęśliwą
luckyTab = []                    #lista przechowująca szczęśliwe liczby
luckyTabCurrent = []             #lista do której w danej iteracji bądą wpisywane liczby poza wykluczonymi

for i in range(1, 10001):        #pętla dzięki której na początku uzyskamy w LuckyTab same liczby nieparzyste
    if (i % 2 != 0):
            luckyTab.append(i)
counter += 1
newLuckier = luckyTab[counter]  #przypisanie do zmiennej newLuckier najnowszej szczęśliwej liczby

while newLuckier < len(luckyTab):                   #cała pętla będzie się wykonywała dopóki najnowsza szczęśliwa liczba będzie mniejsza od długości listy
    for i in range(0, len(luckyTab)):               #tworzymy pętle równą długości listy
        if (i + 1) % newLuckier != 0:               #wyrzucamy indeksy o wielokrotności ostatniej szczęśliwej liczby(zgodnie z założeniem zadania)
            luckyTabCurrent.append(luckyTab[i])

    luckyTab = luckyTabCurrent.copy()               #przypisuję tablicy luckyTab wartości zaaktualizowane
    luckyTabCurrent.clear()                         #czyszczę tablicę pomocniczą, żeby była gotowa na kolejny obrót pętli ;)
    counter += 1                                    #za każdym obrotem pętli zwiększam licznik o 1
    newLuckier = luckyTab[counter]



with open("dane (1).txt", "r") as file:
    howLong = 0                                        #zeruję zmienną howLong, która będzie przechowywać wartość ciągu liczb szczęśliwych
    temporary = []                                     #tworzę listę temporary, która będzie tworzona przy znalezieniu liczby szczęśliwej, dzięki niej, jeżeli znajdziemy najdłuższy ciąg, to odwołując się do jej pierwszego elementu odwołamy się do pierwszego wyrazu ciągu
    maksi = 0                                          #zeruję zmienną maksi, która będzie przechowywała wartość najdłuższego ciągu
    for line in file:
        if luckyNumbers(int(line), luckyTab):
            temporary.append(line)
            howLong += 1
            if (howLong > maksi):                      #porównuję długość aktualnego ciągu z najdłuższym do tej pory, jeżeli aktualny jest dłuższy to go nadpisuje
                maksi = howLong
                pierwsza = temporary[0]
        else:                                          #jeżeli ciąg zostanie przerwany to czyszczę listę temporary oraz zeruję długość aktualnego ciągu
            temporary.clear()
            howLong = 0
                                                       #WYNIKI
print("najdluzszy ciag wyniosl: ", maksi)              #27
print("pierwsza liczba ciagu to: ", pierwsza)          #1749


