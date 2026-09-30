def reverse_string(text: str) -> str:
    """Обертає переданий рядок у зворотному порядку."""
    return text[::-1]


def main() -> None:
    original_text = input("Введіть рядок для обертання: ")
    reversed_text = reverse_string(original_text)

    print(f"Початковий рядок: {original_text}")
    print(f"Обернений рядок:  {reversed_text}")


if __name__ == "__main__":
    main()