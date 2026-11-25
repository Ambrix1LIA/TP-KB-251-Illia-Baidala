from lab_04 import tokenize, to_rpn, eval_rpn


def test_tokenize():
    expr = "3 + 4 * 2"
    tokens = tokenize(expr)
    assert tokens == ['3', '+', '4', '*', '2']


def test_to_rpn_simple():
    tokens = ['2', '+', '2']
    rpn = to_rpn(tokens)
    assert rpn == ['2', '2', '+']


def test_to_rpn_order():
    tokens = ['2', '+', '2', '*', '2']
    rpn = to_rpn(tokens)
    assert rpn == ['2', '2', '2', '*', '+']


def test_eval_simple():
    assert eval_rpn(['3', '4', '+']) == 7
    assert eval_rpn(['10', '2', '/']) == 5
    assert eval_rpn(['2', '3', '^']) == 8


def test_full_example_from_lab():
    expr = "3 + 4 * 2 / (1 - 5) ^ 2"
    tokens = tokenize(expr)
    rpn = to_rpn(tokens)
    assert " ".join(rpn) == "3 4 2 * 1 5 - 2 ^ / +"
    result = eval_rpn(rpn)
    assert result == 3.5