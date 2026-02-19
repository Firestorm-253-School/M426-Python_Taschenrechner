def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    if b == 0:
        print("Fehler: Division durch Null ist nicht erlaubt!")
        return None
    return a / b

def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")
    if wahl not in ["1", "2", "3", "4"]:
        print("Falsche Auswahl, das Programm wird beendet.")
        return
    
    a, b = (input("a: "), input("b: "))
    
    if not a.isnumeric():
        print(f"a: {a} is not a valid number!")
        return
    if not b.isnumeric():
        print(f"b: {b} is not a valid number!")
        return

    a = float(a)
    b = float(b)

    match wahl:
        case "1":
            ergebnis = addieren(a, b)
            print(f"Das ergebnis ist {a} + {b} = {ergebnis}")
        case "2":
            ergebnis = subtrahieren(a, b)
            print(f"Das ergebnis ist {a} - {b} = {ergebnis}")
        case "3":
            ergebnis = multiplizieren(a, b)
            print(f"Das ergebnis ist {a} * {b} = {ergebnis}")
        case "4":
            ergebnis = dividieren(a, b)
            if ergebnis is not None:
                print(f"Das ergebnis ist {a} / {b} = {ergebnis}")
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
