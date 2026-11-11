def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: потрібно ввести число, а не текст!")


def get_operation():
    while True:
        op = input("Введіть операцію (+, -, *, /): ").strip()
        if op in ["+", "-", "*", "/"]:
            return op
        print("Помилка: невідома операція! Оберіть +, -, * або /.")