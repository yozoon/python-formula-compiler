import ast

from ast_compiler import compile_module


def create_module(value):
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
                    ast.Return(value=value),
                ],
                decorator_list=[],
                returns=ast.Name(id="float", ctx=ast.Load()),
            )
        ],
        type_ignores=[],
    )


def test_compile():
    module = create_module(value=ast.Constant(2))
    callable = compile_module(module=module)
    assert callable is not None
    assert callable(0) == 2
