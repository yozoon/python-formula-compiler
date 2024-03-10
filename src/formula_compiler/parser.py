import ast
from typing import Union

from .lexer import Lexer, TokenType, ConstantToken, VariableToken

Node = Union[ast.Constant, ast.BinOp, ast.UnaryOp, ast.Name, ast.Call, ast.Attribute]

FUNCTION_NAME = "fun"


class Parser:

    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.variables: set[int] = set()

    def eat(self, token_type: TokenType):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if not self.current_token:
            raise SyntaxError()

        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        elif self.current_token.type == TokenType.EOF:
            raise SyntaxError("Did you forget to close parentheses?")
        else:
            raise SyntaxError(f"Token types do not match: {self.current_token.type} "
                              f"!= {token_type}")

    def factor(self) -> Node:
        """
        factor : (ADD | SUB) factor | MATH_OP factor | INTEGER | FLOAT | X
                    | PI LPAREN RPAREN | LPAREN expr RPAREN
        """
        token = self.current_token

        if token.type == TokenType.Add:
            self.eat(TokenType.Add)
            return ast.UnaryOp(op=ast.UAdd(), operand=self.factor())

        elif token.type == TokenType.Sub:
            self.eat(TokenType.Sub)
            return ast.UnaryOp(op=ast.USub(), operand=self.factor())

        # Constants
        elif token.type == TokenType.Pi:
            self.eat(TokenType.Pi)
            self.eat(TokenType.LParen)
            self.eat(TokenType.RParen)
            return ast.Attribute(
                value=ast.Name(id='math', ctx=ast.Load()),
                attr='pi',
                ctx=ast.Load(),
            )

        # Square Root
        elif token.type == TokenType.Sqrt:
            self.eat(TokenType.Sqrt)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='sqrt',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        # Logarithms and Exponential
        elif token.type == TokenType.Log:
            self.eat(TokenType.Log)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='log',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.Log10:
            self.eat(TokenType.Log10)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='log10',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.Exp:
            self.eat(TokenType.Exp)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='exp',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        # Trigonometric Functions
        elif token.type == TokenType.Sin:
            self.eat(TokenType.Sin)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='sin',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.Cos:
            self.eat(TokenType.Cos)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='cos',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.Tan:
            self.eat(TokenType.Tan)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='tan',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.ASin:
            self.eat(TokenType.ASin)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='asin',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.ACos:
            self.eat(TokenType.ACos)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='acos',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.ATan:
            self.eat(TokenType.ATan)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='atan',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        # Hyperbolic Functions
        elif token.type == TokenType.Sinh:
            self.eat(TokenType.Sinh)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='sinh',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.Cosh:
            self.eat(TokenType.Cosh)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='cosh',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.Tanh:
            self.eat(TokenType.Tanh)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='tanh',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.ASinh:
            self.eat(TokenType.ASinh)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='asinh',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.ACosh:
            self.eat(TokenType.ACosh)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='acosh',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        elif token.type == TokenType.ATanh:
            self.eat(TokenType.ATanh)
            return ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='math', ctx=ast.Load()),
                    attr='atanh',
                    ctx=ast.Load(),
                ),
                args=[self.factor()],
                keywords=[],
            )

        # Rounding
        elif token.type == TokenType.Round:
            self.eat(TokenType.Round)
            return ast.Call(
                func=ast.Name(id='round', ctx=ast.Load()),
                args=[self.factor()],
                keywords=[],
            )

        elif isinstance(token, ConstantToken):
            if token.type == TokenType.Integer:
                self.eat(TokenType.Integer)
                return ast.Constant(value=token.value)
            else:
                self.eat(TokenType.Float)
                return ast.Constant(value=token.value)

        elif token.type == TokenType.LParen:
            self.eat(TokenType.LParen)
            result = self.expr()
            self.eat(TokenType.RParen)
            return result

        elif isinstance(token, VariableToken):
            self.eat(TokenType.X)
            self.variables.add(token.index)
            return ast.Name(id=f"x{token.index}", ctx=ast.Load())

        elif token.type == TokenType.EOF:
            self.eat(TokenType.EOF)

        else:
            raise NotImplementedError(f"{token.type}")

    def pow(self) -> Node:
        """ exp : factor (POW factor)* """
        node = self.factor()

        while self.current_token.type == TokenType.Pow:
            self.eat(TokenType.Pow)
            node = ast.BinOp(left=node, op=ast.Pow(), right=self.factor())
        return node

    def term(self) -> Node:
        """ term : pow ((MUL | DIV) pow)* """
        node = self.pow()

        while self.current_token.type in (TokenType.Mul, TokenType.Div):
            token = self.current_token
            if token.type == TokenType.Mul:
                self.eat(TokenType.Mul)
                op = ast.Mult()
            elif token.type == TokenType.Div:
                self.eat(TokenType.Div)
                op = ast.Div()
            node = ast.BinOp(left=node, op=op, right=self.pow())
        return node

    def expr(self) -> Node:
        """
        factor : (ADD | SUB) factor | statement factor | INTEGER | FLOAT | X
                    | LPAREN expr RPAREN
        pow : factor (POW factor)*
        term : pow ((MUL | DIV) pow)*
        """

        node = self.term()

        while self.current_token.type in (TokenType.Add, TokenType.Sub):
            token = self.current_token
            if token.type == TokenType.Add:
                self.eat(TokenType.Add)
                op = ast.Add()
            else:
                self.eat(TokenType.Sub)
                op = ast.Sub()

            node = ast.BinOp(left=node, op=op, right=self.term())
        return node

    def parse(self) -> ast.Module:
        """
        Parses the formula and creates required boilerplate code for converting
        an AST into a module that can later be compiled.
        """
        result = self.expr()
        if self.current_token.type != TokenType.EOF:
            raise SyntaxError("Incomplete formula provided. Did you check if all "
                              "parentheses are matched?")

        args = [
            ast.arg(arg=f"x{i}", annotation=ast.Name(id="float", ctx=ast.Load()))
            for i in self.variables
        ]
        return ast.Module(
            body=[
                ast.Import(names=[ast.alias(name="math")]),
                ast.FunctionDef(
                    name="fun",
                    args=ast.arguments(
                        posonlyargs=[],
                        args=args,
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        ast.Return(value=result),
                    ],
                    decorator_list=[],
                    returns=ast.Name(id="float", ctx=ast.Load()),
                )
            ],
            type_ignores=[],
        )
