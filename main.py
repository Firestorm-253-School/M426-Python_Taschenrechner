def main():
    
    def addieren(a, b):
        return a + b
    
    def subtrahieren(a, b):
        return a - b
    
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    match wahl:
        case "1":
            num1 = float(input("Erste Zahl eingeben: "))
            num2 = float(input("Zweite Zahl eingeben: "))
            ergebnis = addieren(num1, num2)
            print(f"Das ergebnis ist {num1} + {num2} = {ergebnis}")
        case "2":
            num1 = float(input("Erste Zahl eingeben: "))
            num2 = float(input("Zweite Zahl eingeben: "))
            ergebnis = subtrahieren(num1, num2)
            print(f"Das ergebnis ist {num1} - {num2} = {ergebnis}")
        case "3":
            print("Gruppenmitglied 2 kann hier die Multiplikation implementieren.")
            # Hier die Funktion für die Multiplikation einfügen
        case "4":
            print("Gruppenmitglied 2 kann hier die Division implementieren.")
            # Hier die Funktion für die Division einfügen
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()