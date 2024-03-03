import ast
import logging
from typing import Optional, Callable, Union

from formula_parser.parser import FUNCTION_NAME


def compile_module(
        module: ast.Module) -> Optional[Callable[[Union[int, float]], Union[int, float]]]:
    """
    Compiles a module into a callable that takes one numeric value as an argument and
    returns a transformed one.
    """
    code = compile(ast.fix_missing_locations(module), filename="tmp", mode="exec")
    namespace = {}

    try:
        exec(code, namespace)
    except SyntaxError as e:
        logging.warning(e)
        return

    return namespace.get(FUNCTION_NAME, None)
