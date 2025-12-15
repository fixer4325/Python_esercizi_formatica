# ESEMPIO 1: Calcolatrice con menu
def menu():
    """Mostra il menu e restituisce la scelta."""
    print("\n=== CALCOLATRICE ===")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("0. Esci")
    return input("Scegli: ")

def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: divisione per zero!"
    return a / b

# Programma principale
def calcolatrice():
    while True:
        scelta = menu()
        
        if scelta == "0":
            print("Arrivederci!")
            break
        
        if scelta in ["1", "2", "3", "4"]:
            num1 = float(input("Primo numero: "))
            num2 = float(input("Secondo numero: "))
            
            if scelta == "1":
                print(f"Risultato: {somma(num1, num2)}")
            elif scelta == "2":
                print(f"Risultato: {sottrazione(num1, num2)}")
            elif scelta == "3":
                print(f"Risultato: {moltiplicazione(num1, num2)}")
            elif scelta == "4":
                print(f"Risultato: {divisione(num1, num2)}")
        else:
            print("Scelta non valida!")

# Esegui la calcolatrice
calcolatrice()  # Decommentare per provare