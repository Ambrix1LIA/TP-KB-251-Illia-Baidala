import requests


def convert_currency():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)

    if response.status_code != 200:
        print("Помилка підключення до сервісу банку!")
        return

    rates = response.json()

    currency = input("Введіть валюту (USD, EUR, PLN): ").strip().upper()
    if currency not in ["USD", "EUR", "PLN"]:
        print("Помилка: підтримуються тільки USD, EUR або PLN!")
        return

    try:
        amount = float(input(f"Введіть суму в {currency}: "))
    except ValueError:
        print("Помилка: потрібно ввести числове значення!")
        return

    current_rate = None
    for item in rates:
        if item["cc"] == currency:
            current_rate = item["rate"]
            break

    if current_rate:
        result = amount * current_rate
        print(f"Офіційний курс {currency}: {current_rate:.2f} грн")
        print(f"Результат: {amount} {currency} = {result:.2f} грн")
    else:
        print("Не вдалося отримати курс для цієї валюти.")


if __name__ == "__main__":
    convert_currency()