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
    a, b = (input("a: "), input("b: "))
    
    if not a.isnumeric():
        print(f"a: {a} is not a valid number!")
        return
    if not b.isnumeric():
        print(f"b: {b} is not a valid number!")
        return

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
            print(f"{a} * {b} = {a * b}")
        case "4":
            print(f"{a} / {b} = {a / b}")
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
