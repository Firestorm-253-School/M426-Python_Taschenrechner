def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    if b == 0:
        return None
    return a / b

def process(func, a, b, symbol):
    result = func(a, b)
    print(f"Das Ergebnis ist: {a} {symbol} {b} = {result}")

def main():
    print("Taschenrechner")
    print("+ fuer Addition")
    print("- fuer Subtraktion")
    print("* fuer Multiplikation")
    print("/ fuer Division")

    wahl = input("Wahl eingeben: ")
    if wahl not in ["+", "-", "*", "/"]:
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
        case "+":
            process(addieren, a, b, wahl)
        case "-":
            process(subtrahieren, a, b, wahl)
        case "*":
            process(multiplizieren, a, b, wahl)
        case "/":
            ergebnis = dividieren(a, b)
            if not ergebnis:
                print("Fehler: Division durch Null ist nicht erlaubt!")
            else:
                print(f"Das ergebnis ist {a} / {b} = {ergebnis}")
        case _:
            raise Exception("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
