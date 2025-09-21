#!/usr/bin/env python3
"""
Игра "Угадай число".
Компьютер загадывает случайное число, а игрок пытается его отгадать.
"""

import random

def guess_number():
    print("🎲 Добро пожаловать в игру 'Угадай число'!")
    low, high = 1, 100
    secret = random.randint(low, high)
    attempts = 0

    print(f"Я загадал число от {low} до {high}. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Твоё предположение: "))
        except ValueError:
            print("Введите число, а не текст!")
            continue

        attempts += 1

        if guess < secret:
            print("Моё число больше 📈")
        elif guess > secret:
            print("Моё число меньше 📉")
        else:
            print(f"🎉 Правильно! Я загадал {secret}. Ты справился за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_number()
