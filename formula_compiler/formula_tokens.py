from typing import Union
from enum import Enum, auto

NumericType = Union[int, float]


class TokenType(Enum):
    # Numeric Values
    Integer = auto()
    Float = auto()

    # Simple Arithmetic Operators
    Add = auto()
    Sub = auto()
    Mul = auto()
    Div = auto()
    Pow = auto()

    # A variable
    X = auto()

    # Mathematical Operators
    Log = auto()
    Sqrt = auto()
    Exp = auto()
    Round = auto()

    # Structure
    LParen = auto()
    RParen = auto()
    EOF = auto()


class Token:
    __slots__ = ("type")

    def __init__(self, /, type: TokenType):
        self.type = type

    def __str__(self) -> str:
        return f"Token({self.type=})"


class NumericToken(Token):
    __slots__ = ("type", "value")

    def __init__(self, type: TokenType, value: NumericType):
        super().__init__(type)
        self.value = value

    def __str__(self) -> str:
        return f"NumericToken({self.type=}, {self.value=})"
