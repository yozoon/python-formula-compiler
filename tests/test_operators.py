import math
from typing import Callable

from formula_parser.parser import Parser
from formula_parser.lexer import Lexer
from ast_compiler import compile_module


def create_callable(text: str) -> Callable:
    lexer = Lexer(text=text)
    parser = Parser(lexer=lexer)
    module = parser.parse()
    module = compile_module(module=module)
    assert module is not None
    return module


def test_x():
    callable = create_callable("X")
    assert callable(1) == 1


def test_negative():
    callable = create_callable("-1")
    assert callable(0) == -1


def test_positive():
    callable = create_callable("+1")
    assert callable(0) == 1


def test_plus():
    callable = create_callable("1+1")
    assert callable(0) == 2


def test_minus():
    callable = create_callable("1-1")
    assert callable(0) == 0


def test_mult():
    callable = create_callable("10*10")
    assert callable(0) == 100


def test_div():
    callable = create_callable("1/2")
    assert callable(0) == 1 / 2


def test_pow():
    callable = create_callable("2^2")
    assert callable(0) == 4


def test_round():
    callable = create_callable("round(4.2)")
    assert callable(0) == round(4.2)


def test_sqrt():
    callable = create_callable("sqrt(2)")
    assert callable(0) == math.sqrt(2)


def test_log():
    callable = create_callable("LN(2)")
    assert callable(0) == math.log(2)


def test_log10():
    callable = create_callable("LOG10(100)")
    assert callable(0) == math.log10(100)


def test_exp():
    callable = create_callable("EXP(1)")
    assert callable(0) == math.exp(1)


def test_pi():
    callable = create_callable("PI()")
    assert callable(0) == math.pi


def test_sin():
    callable = create_callable("SIN(1/2)")
    assert callable(0) == math.sin(1 / 2)


def test_cos():
    callable = create_callable("COS(1/2)")
    assert callable(0) == math.cos(1 / 2)


def test_tan():
    callable = create_callable("TAN(1/2)")
    assert callable(0) == math.tan(1 / 2)


def test_asin():
    callable = create_callable("ASIN(1/2)")
    assert callable(0) == math.asin(1 / 2)


def test_acos():
    callable = create_callable("ACOS(1/2)")
    assert callable(0) == math.acos(1 / 2)


def test_atan():
    callable = create_callable("ATAN(1/2)")
    assert callable(0) == math.atan(1 / 2)


def test_sinh():
    callable = create_callable("SINH(1/2)")
    assert callable(0) == math.sinh(1 / 2)


def test_cosh():
    callable = create_callable("COSH(2)")
    assert callable(0) == math.cosh(2)


def test_tanh():
    callable = create_callable("TANH(2)")
    assert callable(0) == math.tanh(2)


def test_asinh():
    callable = create_callable("ASINH(2)")
    assert callable(0) == math.asinh(2)


def test_acosh():
    callable = create_callable("ACOSH(2)")
    assert callable(0) == math.acosh(2)


def test_atanh():
    callable = create_callable("ATANH(0.5)")
    assert callable(0) == math.atanh(0.5)
