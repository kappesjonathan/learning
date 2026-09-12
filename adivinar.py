import random
import os

def menu():
    while True:
        os.system("cls")
        print("=================")
        print("ADIVINA EL NUMERO")
        print("=================")
        print("1. Juego rápido")
        print("2. Cambiar dificultad")
        print("3. Salir")
        choice = int(input("Elige una opción: "))

        if choice == 1:
            guessgame()
        elif choice == 2:
            difficult_menu()
        elif choice == 3:
            print("=================")
            print("====BYE! BYE!====")
            print("=================")
            break
        
def difficult_menu():
    global random_num_max
    while True:
        print("=================")
        print("====DIFFICULT====")
        print("=================")
        print("1. Easy")
        print("2. Hard")
        print("3. Salir")
        difficult = int(input("¿What difficult you want?: "))
        if difficult == 1:
            random_num_max = 100
            break
        elif difficult == 2:
            random_num_max = 500
            break
        elif difficult == 3:
            random_num_max = 1000
            break

def guessgame():
    random_num_min = 1
    secret_number = random.randint(random_num_min, random_num_max)
    tries = 0

    while True:
        guess = input(f"Guess my number! [1;{random_num_max}]: ")
        tries += 1

        if guess < secret_number:
            print("Más alto...")
        elif guess > secret_number:
            print("Más bajo...")
        else:
            print("¡Felicidades! ¡Lo adivinaste!")
            print(f"Mi número era: {secret_number}")
            print(f"Intentos realizados: {tries}")
            break

random_num_max = 500
menu()