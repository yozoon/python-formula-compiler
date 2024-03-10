import ast
import pytest

from formula_compiler.ast_compiler import compile_module


def create_module(value):
    return ast.Module(
        body=[
            ast.FunctionDef(
                name="fun",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[
                        ast.arg(
                            arg="x",
                            annotation=ast.Name(id="float", ctx=ast.Load()),
                        ),
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


def test_compile_module():
    module = create_module(value=ast.Constant(2))
    callable = compile_module(module=module)
    assert callable(0) == 2


def test_functiondef():
    """ Raises ValueError if module contains no FunctionDef"""
    module = ast.Module(
        body=[ast.Import(names=[ast.alias(name="math")])],
        type_ignores=[],
    )
    with pytest.raises(ValueError) as e:
        _ = compile_module(module=module)


def test_strict():
    """ Raises Value Error if strict and not enough arguments available """
    module = create_module(value=ast.Constant(2))
    with pytest.raises(ValueError) as e:
        _ = compile_module(module=module, n_args=2, strict=True)


def test_non_strict():
    """ If strict is False, compile module generates placeholder arguments to satisfy
    n_args"""
    module = create_module(value=ast.Constant(2))
    callable = compile_module(module=module, n_args=2, strict=False)
    assert callable(0, 0) == 2


def test_empty_body():
    module = ast.Module(
        body=[
            ast.FunctionDef(
                name="fun",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[
                        ast.arg(
                            arg="x",
                            annotation=ast.Name(id="float", ctx=ast.Load()),
                        ),
                    ],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                ),
                body=[
                    
                ],
                decorator_list=[],
                returns=ast.Name(id="float", ctx=ast.Load()),
            )
        ],
        type_ignores=[],
    )
    with pytest.raises(ValueError) as e:
        _ = compile_module(module=module)


def test_syntax_error():
    module = ast.Module(
        body=[
            ast.Return(value=ast.Constant(value=42)),
            ast.FunctionDef(
                name="tmp",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                ),
                body=[ast.Return(value=ast.Constant(value=0))],
                decorator_list=[],
                returns=ast.Name(id="float", ctx=ast.Load()),
            )
        ],
        type_ignores=[],
    )
    with pytest.raises(SyntaxError) as e:
        _ = compile_module(module=module, strict=False)
