from typing import Optional, Callable

from .lexer import Lexer
from .parser import Parser
from .ast_compiler import compile_module


def compile_formula(
    formula: str,
    n_args: int = 1,
    strict: bool = True,
) -> Optional[Callable[..., float]]:
    lexer = Lexer(text=formula)
    parser = Parser(lexer=lexer)
    module = parser.parse()

    return compile_module(module=module, n_args=n_args, strict=strict)


if __name__ == "__main__":
    import argparse
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

    args = parser.parse_args()

    if fun := compile_formula(formula=args.formula, n_args=1, strict=False):
        print("\n=================\nEvaluation Result\n=================")
        print(f"f({args.x}) = {fun(args.x)}")
