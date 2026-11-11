def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка: ділення на нуль неможливе!")
        return None


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: потрібно ввести число, а не текст!")


def main():
    while True:
        a = get_number("Введіть перше число: ")
        op = input("Введіть операцію (+, -, *, /): ").strip()
        b = get_number("Введіть друге число: ")

        match op:
            case "+":
                print("Результат:", add(a, b))
            case "-":
                print("Результат:", sub(a, b))
            case "*":
                print("Результат:", mult(a, b))
            case "/":
                res = div(a, b)
                if res is not None:
                    print("Результат:", res)
            case _:
                print("Помилка: невідома операція!")

        choice = input("\nБажаєте продовжити? ('q' для виходу, Enter — продовжити): ").strip()
        if choice.lower() == "q":
            print("Роботу завершено.")
            break


if __name__ == "__main__":
    main()