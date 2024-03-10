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

    # Constants
    Pi = auto()

    # A Variable
    X = auto()

    # Square Root
    Sqrt = auto()

    # Logarithm and Exponential
    Log = auto()
    Log10 = auto()
    Exp = auto()

    # Rounding
    Round = auto()

    # Trigonometric Functions
    Sin = auto()
    Cos = auto()
    Tan = auto()
    ASin = auto()
    ACos = auto()
    ATan = auto()

    # Hyperbolic Functions
    Sinh = auto()
    Cosh = auto()
    Tanh = auto()
    ASinh = auto()
    ACosh = auto()
    ATanh = auto()

    # Structure
    LParen = auto()
    RParen = auto()
    EOF = auto()


class Token:
    __slots__ = ("type")

    def __init__(self, /, type: TokenType):
        self.type = type

    def __eq__(self, other: "Token") -> bool:
        return self.type == other.type

    def __str__(self) -> str:
        return f"Token({self.type=})"


class ConstantToken(Token):
    __slots__ = ("type", "value")

    def __init__(self, type: TokenType, value: NumericType):
        super().__init__(type)
        self.value = value

    def __eq__(self, other: "ConstantToken") -> bool:
        return super().__eq__(other) and self.value == other.value

    def __str__(self) -> str:
        return f"ConstantToken({self.type=}, {self.value=})"


class VariableToken(Token):
    __slots__ = ("type", "index")

    def __init__(self, index: int):
        super().__init__(TokenType.X)
        self.index = index

    def __eq__(self, other: "VariableToken") -> bool:
        return super().__eq__(other) and self.index == other.index

    def __str__(self) -> str:
        return f"VariableToken({self.type=}, {self.index=})"


RESERVED_KEYWORDS = {
    # Constants
    "pi": Token(type=TokenType.Pi),
    # Square Root
    "sqrt": Token(type=TokenType.Sqrt),
    # Logarithms and Exponential
    "ln": Token(type=TokenType.Log),
    "exp": Token(type=TokenType.Exp),
    "log10": Token(type=TokenType.Log10),
    # Rounding
    "round": Token(type=TokenType.Round),
    # Trigonometric Functions
    "sin": Token(type=TokenType.Sin),
    "cos": Token(type=TokenType.Cos),
    "tan": Token(type=TokenType.Tan),
    "asin": Token(type=TokenType.ASin),
    "acos": Token(type=TokenType.ACos),
    "atan": Token(type=TokenType.ATan),
    # Hyperbolic Functions
    "sinh": Token(type=TokenType.Sinh),
    "cosh": Token(type=TokenType.Cosh),
    "tanh": Token(type=TokenType.Tanh),
    "asinh": Token(type=TokenType.ASinh),
    "acosh": Token(type=TokenType.ACosh),
    "atanh": Token(type=TokenType.ATanh),
}
