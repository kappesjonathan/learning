import random

NUMMINIMO = 1
NUMMAXIMO = 1000
intentos = 0

numero_secreto = random.randint(NUMMINIMO, NUMMAXIMO)
print(numero_secreto)

while True:
    guess = int(input("Intenta adivinar mi número!"))
    intentos = intentos + 1

    if guess < numero_secreto:
        print("Más alto...")
    elif guess > numero_secreto:
        print("Más bajo...")
    else:
        print("¡Felicidades! ¡Lo adivinaste!")
        print(f"Mi número era: {numero_secreto}")
        print(f"Intentos realizados: {intentos}")
        break