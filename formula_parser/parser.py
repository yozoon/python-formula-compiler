import ast
from typing import Union

from .lexer import Lexer, TokenType, NumericToken

Node = Union[ast.Constant, ast.BinOp, ast.UnaryOp, ast.Name, ast.Call]


class Parser:

    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

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
            raise SyntaxError(
                f"Token types do not match: {self.current_token.type} != {token_type}")

    def factor(self) -> Node:
        """
        factor : (ADD | SUB) factor | statement factor | INTEGER | FLOAT | X
                    | LPAREN expr RPAREN
        """
        token = self.current_token

        if token.type == TokenType.Add:
            self.eat(TokenType.Add)
            return ast.UnaryOp(op=ast.UAdd(), operand=self.factor())

        elif token.type == TokenType.Sub:
            self.eat(TokenType.Sub)
            return ast.UnaryOp(op=ast.USub(), operand=self.factor())

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

        elif token.type == TokenType.Round:
            self.eat(TokenType.Round)
            return ast.Call(
                func=ast.Name(id='round', ctx=ast.Load()),
                args=[self.factor()],
                keywords=[],
            )

        elif isinstance(token, NumericToken):
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

        elif token.type == TokenType.X:
            self.eat(TokenType.X)
            return ast.Name(id='x', ctx=ast.Load())

        else:
            raise SyntaxError(f"Unimplemented token: {token.type}")

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
        Parses the formula and creates required boilerplate code for converting an AST
        into a module that can later be compiled.
        """
        result = self.expr()
        if self.current_token.type != TokenType.EOF:
            raise SyntaxError(
                "Incomplete formula provided. Did you check if all parentheses are "
                "matched?")

        return ast.Module(
            body=[
                ast.Import(names=[ast.alias(name="math")]),
                ast.FunctionDef(
                    name="fun",
                    args=ast.arguments(
                        posonlyargs=[],
                        args=[
                            ast.arg(arg="x",
                                    annotation=ast.Name(id="int", ctx=ast.Load())),
                        ],
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
