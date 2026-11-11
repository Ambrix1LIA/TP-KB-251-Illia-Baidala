def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть число!")


def get_operation():
    while True:
        op = input("Введіть операцію (+, -, *, /): ").strip()
        if op in ["+", "-", "*", "/"]:
            return op
        print("Помилка: невідома дія! Оберіть +, -, * або /.")