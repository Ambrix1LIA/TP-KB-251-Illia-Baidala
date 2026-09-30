def test_string_methods(text: str) -> None:
    print(f"Оригінал:     {repr(text)}")
    print(f"strip():      {repr(text.strip())}")
    print(f"capitalize(): {repr(text.strip().capitalize())}")
    print(f"title():      {repr(text.strip().title())}")
    print(f"upper():      {repr(text.upper())}")
    print(f"lower():      {repr(text.lower())}")
    print("-" * 50)


def main() -> None:
    default_text = "   ПрАкТиЧнА ТЕхнОлОгІї ПроГРаМуВаНнЯ   "
    test_string_methods(default_text)

    user_text = input("рядок: ")
    print("\nРезльтат:")
    test_string_methods(user_text)


if __name__ == "__main__":
    main()