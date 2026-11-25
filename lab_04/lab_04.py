def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i].isdigit() or expr[i] == '.':
            num = ""
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            tokens.append(num)
        elif expr[i] in "+-*/^()":
            tokens.append(expr[i])
            i += 1
        else:
            i += 1
    return tokens


def to_rpn(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def eval_rpn(rpn_tokens):
    stack = []
    for token in rpn_tokens:
        if token.replace('.', '', 1).isdigit():
            val = float(token) if '.' in token else int(token)
            stack.append(val)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    res = stack[0]
    return int(res) if isinstance(res, float) and res.is_integer() else res


def main():
    expr = input("Введіть математичний вираз: ").strip()
    if not expr:
        expr = "3 + 4 * 2 / (1 - 5) ^ 2"
        print("Використовуємо тестовий вираз:", expr)

    tokens = tokenize(expr)
    rpn = to_rpn(tokens)
    result = eval_rpn(rpn)

    print("Зворотний польський запис (ЗПЗ):", " ".join(rpn))
    print("Результат обчислення:", result)


if __name__ == "__main__":
    main()