from .formula_tokens import Token, NumericToken, TokenType, NumericType

RESERVED_KEYWORDS = {
    "x": Token(type=TokenType.X),
    "ln": Token(type=TokenType.Log),
    "sqrt": Token(type=TokenType.Sqrt),
    "exp": Token(type=TokenType.Exp),
    "round": Token(type=TokenType.Round),
}


class Lexer:

    def __init__(self, text: str):
        # All lower case
        self.text = text.lower()

        # String cleanup
        self.text = self.text.replace(" ", "")
        self.text = self.text.replace("\n", "")
        self.text = self.text.replace("\r", "")
        self.text = self.text.replace("\t", "")

        self.pos = 0
        self.previous_char = ""
        self.current_char = self.text[self.pos]

    def advance(self) -> None:
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.previous_char = self.current_char
            self.current_char = None  # Indicates end of input
        else:
            self.previous_char = self.current_char
            self.current_char = self.text[self.pos]

    def _id(self) -> Token:
        """Handle identifiers and reserved keywords"""
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        if token := RESERVED_KEYWORDS.get(result, None):
            return token
        else:
            raise SyntaxError(f"Unknown keyword {result}")

    def number(self) -> NumericType:
        """Return a (multidigit) integer or float consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        # Handle decimal places (we treat . and , the same)
        if self.current_char in (".", ","):
            result += "."
            self.advance()

            while (self.current_char is not None and self.current_char.isdigit()):
                result += self.current_char
                self.advance()

        # Handle exponents
        if self.current_char == "e":
            result += self.current_char
            self.advance()
            if self.current_char in ["+", "-"]:
                result += self.current_char
                self.advance()

            while (self.current_char is not None and self.current_char.isdigit()):
                result += self.current_char
                self.advance()

        # Check if the number is floating point or integer and cast to corresponding type
        if any(i in result for i in (".", "e")):
            return float(result)
        return int(result)

    def get_next_token(self) -> Token:
        while self.current_char is not None:

            if self.current_char.isalpha():
                return self._id()

            if self.current_char is not None and self.current_char.isdigit():
                num = self.number()
                if isinstance(num, int):
                    tt = TokenType.Integer
                else:
                    tt = TokenType.Float
                return NumericToken(type=tt, value=num)

            elif self.current_char == "+":
                self.advance()
                return Token(type=TokenType.Add)

            elif self.current_char == "-":
                self.advance()
                return Token(type=TokenType.Sub)

            elif self.current_char == "*":
                self.advance()
                return Token(type=TokenType.Mul)

            elif self.current_char == "/":
                self.advance()
                return Token(type=TokenType.Div)

            elif self.current_char == "^":
                self.advance()
                return Token(type=TokenType.Pow)

            elif self.current_char == "(":
                self.advance()
                return Token(type=TokenType.LParen)

            elif self.current_char == ")":
                self.advance()
                return Token(type=TokenType.RParen)

            self.advance()

        return Token(type=TokenType.EOF)
