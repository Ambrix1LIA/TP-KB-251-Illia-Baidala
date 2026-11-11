import random


def play_game():
    choices = ["камінь", "ножиці", "папір"]

    user_choice = input("Введіть ваш вибір (камінь, ножиці, папір): ").strip().lower()

    if user_choice not in choices:
        print("Помилка: некоректний вибір! Введіть: камінь, ножиці або папір.")
        return

    comp_choice = random.choice(choices)
    print(f"Комп'ютер обрав: {comp_choice}")

    if user_choice == comp_choice:
        print("Нічия!")
    elif (
        (user_choice == "камінь" and comp_choice == "ножиці")
        or (user_choice == "ножиці" and comp_choice == "папір")
        or (user_choice == "папір" and comp_choice == "камінь")
    ):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")


if __name__ == "__main__":
    play_game()