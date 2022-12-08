def Przypisanie_Alfabetu_Do_Liczb():
    x = 0
    Slownik_Alfabetu = {}
    for i in range(65,90):
        litera = chr(i)
        x += 1
        Slownik_Alfabetu[x] = litera.lower()
        # x += 1 
        # Slownik_Alfabetu[x] = litera
    return Slownik_Alfabetu

def Zamina_Na_Liczby(tekst):
    alfabet = Przypisanie_Alfabetu_Do_Liczb()
    zamienione = []
    klucz = list(alfabet.keys())
    wartosci = list(alfabet.values())
    for x in tekst:    
        for i in range(len(alfabet)):
            if x == wartosci[i]:
                zamienione.append(klucz[i])
    return zamienione

def Zamina_Na_Znak(tekst):
    zamienione = []
    alfabet = Przypisanie_Alfabetu_Do_Liczb()
    klucz = list(alfabet.keys())
    wartosci = list(alfabet.values())
    for x in tekst:    
        for i in range(len(alfabet)):
            if x == klucz[i]:
                zamienione.append(wartosci[i])
    return zamienione

def Szyfrowanie(tekst):
    Zaszyfrowany_Tekst = ''
    tekst = Zamina_Na_Liczby(tekst)
    n = 13 # połowa znakow w alfabecie
    tekst = [(x+n)%23 for x in tekst]
    tekst = Zamina_Na_Znak(tekst)
    for x in tekst:
        Zaszyfrowany_Tekst += x   
    return Zaszyfrowany_Tekst

def Odszyfrowanie(tekst):
    Odszyfrowanie_Tekst = ''
    tekst = Zamina_Na_Liczby(tekst)
    n = 13 # połowa znakow w alfabecie
    tekst = [(x-n)%23 for x in tekst]
    tekst = Zamina_Na_Znak(tekst)
    for x in tekst:
        Odszyfrowanie_Tekst += x   
    return Odszyfrowanie_Tekst

tekst = input("Podaj tekst do zaszyfrowania: \n")
tekst = [x for x in tekst]
Zaszyfrowany_Tekst = Szyfrowanie(tekst) 
print('Zaszyfrowana Wiadomość: \n'+ Zaszyfrowany_Tekst)
#aby rozszyfrować wystarczy 2 razy uruchomić szyfrowanie
print('Odszyfrowane: \n' + Odszyfrowanie(Zaszyfrowany_Tekst))
