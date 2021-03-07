# Zad 1.Napisz skrypt, w którym tworzysz listę z ulubionymi filmami, a następnie odwróć całą listę.
# Po odwróceniu listy dodaj kilka pozycji
# (dodane pozycje mają zostać dodane od 5 indeksu, cała lista mam zawierać 10 pozycji)

liststa_ulub = ["Film1", "Film2", "Film3", "lin1", "lin2", "lin3"]
print(liststa_ulub)

liststa_ulub.reverse()
print(liststa_ulub)

liststa_ulub.insert(4, "dodany film 1")
liststa_ulub.insert(5, "d f2")
liststa_ulub.insert(6, "d f 3")
liststa_ulub.insert(7, "d f 4")
print(liststa_ulub)

# Zad 2. Stwórz skrypt, w którym utworzysz słownik z filmami z zadania 1. Pomyśl co może być kluczem
slownik = {1: "Film1", 2: "Film2", 3: "Film3", 4: "lin1", 5: "lin2", 6: "lin3", 7: "dodany film 1", 8: "d f2",
           9: "d f 3", 10: "d f 4"}
for l in slownik.values():
    print(l)

# Zad 3. Stwórz skrypt, gdzie utworzysz słownik z nazwami przedmiotów z obecnego semestru oraz ich skrótami.
# Policz liczbę elementów w słownik
slownik = {1: "Komputerowe wspomaganie programowe", 2: "CAD", 3: "Wizualizacja danych", 4: "WD",
           5: "Przedmioty ogólnouczelniane", 6: "PO", 7: "Język Angielski", 8: "J.A"}
print(len(slownik))

# Zad 4. Napisz skrypt gdzie wczytasz liczbę dowolnego typu i podnieś ją do tej samej potęgi. Użyj funkcji input.
a = input("Podaj liczbe którą chcesz podniesc do tej samej potegi")
print(float(a) ** float(a))

# Zad 5. Napisz skrypt gdzie wczytasz dowolny ciąg znaków, i policzysz wystąpienie litery a. Użyj instrukcji readline() i write()).
a = input("Podaj napis")
print(a.count("a"))

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź czy liczba a jest parzysta oraz czy jednocześnie b>c
a = input("Podaj liczbe calkowita a: ")
b = input("Podaj liczbe calkowita b: ")
c = input("Podaj liczbe calkowita c: ")
if int(a) % 2 == 0 and int(b) > int(c):
    print("Podane liczby spełniają warunek że a jest parzyste i b>c")
else:
    print("Jeden lub oba warunki nie zotały spełnione")