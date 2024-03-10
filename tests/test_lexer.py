import pytest
from formula_compiler.lexer import Lexer, Token, TokenType
from formula_compiler.tokens import ConstantToken, VariableToken


def test_int():
    lexer = Lexer(text="1")
    assert lexer.get_next_token() == ConstantToken(type=TokenType.Integer, value=1)


def test_float():
    lexer = Lexer(text="1.2")
    assert lexer.get_next_token() == ConstantToken(type=TokenType.Float, value=1.2)


def test_unknown_keyword():
    lexer = Lexer(text="ASDFJHLK")
    with pytest.raises(ValueError):
        lexer.get_next_token()


def test_special_char():
    lexer = Lexer(text="%")
    with pytest.raises(ValueError):
        lexer.get_next_token()


def test_log():
    lexer = Lexer(text="LN")
    assert lexer.get_next_token() == Token(type=TokenType.Log)


def test_scientific():
    lexer = Lexer(text="1e-4")
    assert lexer.get_next_token() == ConstantToken(type=TokenType.Float, value=1e-4)


def test_x():
    lexer = Lexer(text="X")
    assert lexer.get_next_token() == VariableToken(index=0)


def test_x3():
    lexer = Lexer(text="X3")
    assert lexer.get_next_token() == VariableToken(index=3)
