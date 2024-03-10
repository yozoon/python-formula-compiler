from .tokens import Token, ConstantToken, VariableToken, TokenType, RESERVED_KEYWORDS


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
            raise ValueError(f"Unknown keyword {result}")

    def number(self) -> ConstantToken:
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
            return ConstantToken(type=TokenType.Float, value=float(result))
        return ConstantToken(type=TokenType.Integer, value=int(result))

    def variable(self) -> VariableToken:
        self.advance()
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        if not result:
            return VariableToken(index=0)

        return VariableToken(index=int(result))

    def get_next_token(self) -> Token:
        while self.current_char is not None:
            if self.current_char == "x":
                return self.variable()

            elif self.current_char.isalpha():
                return self._id()

            elif self.current_char is not None and self.current_char.isdigit():
                return self.number()

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

            raise ValueError(f"Unhandled character '{self.current_char}'")

        return Token(type=TokenType.EOF)
