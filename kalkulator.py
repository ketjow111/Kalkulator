#!/usr/bin/env python3

def kalkulator():
    print("Prosty Kalkulator")
    print("Dostępne operacje:")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnożenie (*)")
    print("4. Dzielenie (/)")
    print("5. Wyjście")

    while True:
        wybor = input("\nWybierz operację (1/2/3/4/5): ")
        
        if wybor == '5':
            print("Do widzenia!")
            break

        if wybor not in ['1', '2', '3', '4']:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            continue

        try:
            liczba1 = float(input("Wprowadź pierwszą liczbę: "))
            liczba2 = float(input("Wprowadź drugą liczbę: "))
        except ValueError:
            print("Nieprawidłowe dane. Wprowadź liczby.")
            continue

        if wybor == '1':
            wynik = liczba1 + liczba2
            print(f"Wynik: {liczba1} + {liczba2} = {wynik}")
        elif wybor == '2':
            wynik = liczba1 - liczba2
            print(f"Wynik: {liczba1} - {liczba2} = {wynik}")
        elif wybor == '3':
            wynik = liczba1 * liczba2
            print(f"Wynik: {liczba1} * {liczba2} = {wynik}")
        elif wybor == '4':
            if liczba2 == 0:
                print("Błąd: Dzielenie przez zero!")
            else:
                wynik = liczba1 / liczba2
                print(f"Wynik: {liczba1} / {liczba2} = {wynik}")

if __name__ == "__main__":
    kalkulator()
