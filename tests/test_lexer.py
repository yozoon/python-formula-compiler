from formula_compiler.lexer import Lexer, NumericToken, Token, TokenType


def test_int():
    lexer = Lexer(text="1")
    assert lexer.get_next_token() == NumericToken(type=TokenType.Integer, value=1)


def test_float():
    lexer = Lexer(text="1.2")
    assert lexer.get_next_token() == NumericToken(type=TokenType.Float, value=1.2)


def test_scientific():
    lexer = Lexer(text="1e-4")
    assert lexer.get_next_token() == NumericToken(type=TokenType.Float, value=1e-4)


def test_x():
    lexer = Lexer(text="x")
    assert lexer.get_next_token() == Token(type=TokenType.X)
