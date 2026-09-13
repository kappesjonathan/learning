import random
import tkinter as tk
import winsound
from tkinter import ttk

random_num_max = 500
secret_number = 0
tries = 0
shake_job = None
shake_direction = 1
shake_offset = 0


def play_sound(sound):
    if sound == "start":
        winsound.Beep(600, 120)
    elif sound == "invalid":
        winsound.Beep(250, 180)
    elif sound == "far":
        winsound.Beep(350, 100)
    elif sound == "close":
        winsound.Beep(750, 120)
    elif sound == "win":
        winsound.Beep(700, 100)
        winsound.Beep(900, 100)
        winsound.Beep(1100, 180)


def stop_shake():
    global shake_job, shake_offset

    if shake_job is not None:
        window.after_cancel(shake_job)
        shake_job = None
    shake_offset = 0
    last_guess_label.place_configure(x=200, y=70)


def show_guess_animation(guess):
    global shake_job, shake_direction, shake_offset

    distance = abs(guess - secret_number)
    closeness = 1 - (distance / random_num_max)
    closeness = max(0, min(1, closeness))

    red = int(35 + (closeness * 220))
    green = int(110 - (closeness * 80))
    blue = int(245 - (closeness * 210))
    last_guess_label.config(fg=f"#{red:02x}{green:02x}{blue:02x}")

    if shake_job is not None:
        window.after_cancel(shake_job)
    shake_direction = 1
    shake_offset = 0
    shake_number(closeness)


def shake_number(closeness):
    global shake_job, shake_direction, shake_offset

    shake_offset += shake_direction * 8
    if shake_offset <= -8 or shake_offset >= 8:
        shake_direction *= -1
    last_guess_label.place_configure(x=200 + shake_offset)

    interval = int(180 - (closeness * 145))
    shake_job = window.after(interval, lambda: shake_number(closeness))


def start_game():
    global random_num_max, secret_number, tries

    stop_shake()
    difficulty = difficulty_choice.get()
    if difficulty == "Fácil":
        random_num_max = 100
    elif difficulty == "Normal":
        random_num_max = 500
    else:
        random_num_max = 1000

    secret_number = random.randint(1, random_num_max)
    tries = 0
    guess_entry.delete(0, tk.END)
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    result_label.config(text=f"Adivina un número entre 1 y {random_num_max}.")
    tries_label.config(text="Intentos: 0")
    last_guess_label.config(text="?", fg="#2474f5")
    play_sound("start")
    guess_entry.focus()


def check_guess():
    global tries

    guess = guess_entry.get()
    if not guess.isdigit():
        result_label.config(text="Escribe un número válido.")
        play_sound("invalid")
        return

    guess = int(guess)
    tries += 1
    tries_label.config(text=f"Intentos: {tries}")
    last_guess_label.config(text=str(guess))
    show_guess_animation(guess)

    distance = abs(guess - secret_number)
    if distance <= random_num_max / 4:
        play_sound("close")
    else:
        play_sound("far")

    if guess < secret_number:
        result_label.config(text="El número secreto es mayor.")
    elif guess > secret_number:
        result_label.config(text="El número secreto es menor.")
    else:
        stop_shake()
        play_sound("win")
        last_guess_label.config(fg="#20a05a")
        result_label.config(text=f"¡Correcto! Era el {secret_number}.")
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")


window = tk.Tk()
window.title("Adivina el número")
window.geometry("400x430")
window.resizable(False, False)

title_label = ttk.Label(window, text="ADIVINA EL NÚMERO", font=("Arial", 18, "bold"))
title_label.pack(pady=15)

difficulty_choice = tk.StringVar(value="Normal")
difficulty_menu = ttk.Combobox(
    window,
    textvariable=difficulty_choice,
    values=("Fácil", "Normal", "Difícil"),
    state="readonly",
)
difficulty_menu.pack()

start_button = ttk.Button(window, text="Nuevo juego", command=start_game)
start_button.pack(pady=10)

guess_display = tk.Frame(window, width=400, height=145)
guess_display.pack()
guess_display.pack_propagate(False)

last_guess_label = tk.Label(
    guess_display,
    text="?",
    font=("Arial", 72, "bold"),
    fg="#2474f5",
)
last_guess_label.place(x=200, y=70, anchor="center")

guess_entry = ttk.Entry(window, state="disabled")
guess_entry.pack()

guess_button = ttk.Button(window, text="Comprobar", command=check_guess, state="disabled")
guess_button.pack(pady=8)

result_label = ttk.Label(window, text="Pulsa «Nuevo juego» para empezar.")
result_label.pack(pady=5)

tries_label = ttk.Label(window, text="Intentos: 0")
tries_label.pack()

window.mainloop()