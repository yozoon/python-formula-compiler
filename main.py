import ast
import argparse

from formula_parser import Lexer, Parser
from ast_compiler import compile_module


def main(args: argparse.Namespace) -> None:
    lexer = Lexer(text=args.formula)
    parser = Parser(lexer=lexer)

    try:
        module = parser.parse()
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
        return

    print("====================\nAbstract Syntax Tree\n====================")
    print(ast.dump(module))

    if fun := compile_module(module=module):
        print("\n=================\nEvaluation Result\n=================")
        print(f"f({args.x}) = {fun(args.x)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--formula",
        default="ROUND(2^1 + 2^3 + EXP(5*LN(x)))",
        type=str,
        help="The Excel formula to be compiled.",
    )
    parser.add_argument(
        "-x",
        type=float,
        default=2.0,
        help="The value to call the compiled function with.",
    )
    main(args=parser.parse_args())
