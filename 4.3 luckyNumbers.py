def czyPierwsza(n):             #funkcja zwracająca informację czy liczba jest liczbą pierwszą czy nie
    if n < 2:
        return False
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True


def luckyNumbers(n, lucktab):   #funkcja zwracająca informację czy liczba jest liczbą szczęśliwą czy nie(przeszukujemy listę luckyTab)
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
    count = 0                                         #zeruję zmienną count, która będzie liczyła ilość liczb spełniających warunek

    for line in file:
        if luckyNumbers(int(line), luckyTab) == True and czyPierwsza(int(line)) == True:   #sprawdzam każdą liczbę osobno czy jest pierwsza i szczęśliwa jednocześnie
            count += 1


    print("liczb, które są jednocześnie szczęśliwe i pierwsze jest: ", count)              #wyświetlam wynik (który jest równy 56) :D
