import math
from typing import Callable

from formula_compiler.parser import Parser
from formula_compiler.lexer import Lexer
from formula_compiler.compiler import compile_module


def create_callable(text: str, n_args: int = 0) -> Callable:
    lexer = Lexer(text=text)
    parser = Parser(lexer=lexer)
    module = parser.parse()
    module = compile_module(module=module, n_args=n_args)
    assert module is not None
    return module


def test_x():
    callable = create_callable("X", n_args=1)
    assert callable(1) == 1


def test_negative():
    callable = create_callable("-1")
    assert callable() == -1


def test_positive():
    callable = create_callable("+1")
    assert callable() == 1


def test_plus():
    callable = create_callable("1+1")
    assert callable() == 2


def test_minus():
    callable = create_callable("1-1")
    assert callable() == 0


def test_mult():
    callable = create_callable("10*10")
    assert callable() == 100


def test_div():
    callable = create_callable("1/2")
    assert callable() == 1 / 2


def test_pow():
    callable = create_callable("2^2")
    assert callable() == 4


def test_round():
    callable = create_callable("round(4.2)")
    assert callable() == round(4.2)


def test_sqrt():
    callable = create_callable("sqrt(2)")
    assert callable() == math.sqrt(2)


def test_log():
    callable = create_callable("LN(2)")
    assert callable() == math.log(2)


def test_log10():
    callable = create_callable("LOG10(100)")
    assert callable() == math.log10(100)


def test_exp():
    callable = create_callable("EXP(1)")
    assert callable() == math.exp(1)


def test_pi():
    callable = create_callable("PI()")
    assert callable() == math.pi


def test_sin():
    callable = create_callable("SIN(1/2)")
    assert callable() == math.sin(1 / 2)


def test_cos():
    callable = create_callable("COS(1/2)")
    assert callable() == math.cos(1 / 2)


def test_tan():
    callable = create_callable("TAN(1/2)")
    assert callable() == math.tan(1 / 2)


def test_asin():
    callable = create_callable("ASIN(1/2)")
    assert callable() == math.asin(1 / 2)


def test_acos():
    callable = create_callable("ACOS(1/2)")
    assert callable() == math.acos(1 / 2)


def test_atan():
    callable = create_callable("ATAN(1/2)")
    assert callable() == math.atan(1 / 2)


def test_sinh():
    callable = create_callable("SINH(1/2)")
    assert callable() == math.sinh(1 / 2)


def test_cosh():
    callable = create_callable("COSH(2)")
    assert callable() == math.cosh(2)


def test_tanh():
    callable = create_callable("TANH(2)")
    assert callable() == math.tanh(2)


def test_asinh():
    callable = create_callable("ASINH(2)")
    assert callable() == math.asinh(2)


def test_acosh():
    callable = create_callable("ACOSH(2)")
    assert callable() == math.acosh(2)


def test_atanh():
    callable = create_callable("ATANH(0.5)")
    assert callable() == math.atanh(0.5)
