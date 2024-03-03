import ast
import argparse

from formula_compiler import Lexer, Parser, Node, compile_module


def create_module(tree: Node):
    """
    Helper function to generate the required boilerplate code for converting an ASTs
    into a module that can later be compiled.
    """
    return ast.Module(
        body=[
            ast.Import(names=[ast.alias(name="math")]),
            ast.FunctionDef(
                name="fun",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[
                        ast.arg(arg="x", annotation=ast.Name(id="int", ctx=ast.Load())),
                    ],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                ),
                body=[
                    ast.Return(value=tree),
                ],
                decorator_list=[],
                returns=ast.Name(id="float", ctx=ast.Load()),
            )
        ],
        type_ignores=[],
    )


def main(args: argparse.Namespace) -> None:
    lexer = Lexer(text=args.formula)
    parser = Parser(lexer=lexer)

    try:
        tree = parser.parse()
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
        return

    print("====================\nAbstract Syntax Tree\n====================")
    print(ast.dump(tree))

    if module := create_module(tree=tree):
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
