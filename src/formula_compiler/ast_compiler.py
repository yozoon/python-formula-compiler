import ast
from typing import Callable

from .parser import FUNCTION_NAME


def compile_module(
    module: ast.Module,
    n_args: int = 1,
    strict: bool = True,
) -> Callable[..., float]:
    """
    Compiles a module into a callable that takes `n_args` numeric values as
    arguments and returns a single numeric value.
    """
    f_def = None
    for b in module.body:
        if isinstance(b, ast.FunctionDef):
            f_def = b
            break

    if not f_def:
        raise ValueError("Provided module does not compile a `FunctionDef`!")

    n_args_required = len(f_def.args.args)
    # If strict is True, we expect exactly the module must have `n_args`
    # arguments. If strict is False, we also accept modules with less than
    # `n_args` arguments.
    condition = (n_args_required != n_args if strict else n_args_required > n_args)
    if condition:
        raise ValueError(f"The provided module requires {n_args_required} arguments, but "
                         f"the compiler was instructed to expect {n_args}!")

    # In order for the callable to also reflect the behavior invoked with
    # strict=False, add dummy arguments, such that the compiled Callable does
    # not throw TypeErrors when the number of positional arguments provided is
    # more than what the module provided (but maximally n_args).
    if not strict:
        i = 0
        while len(f_def.args.args) < n_args:
            f_def.args.args.append(
                ast.arg(
                    arg=f"temporary_placeholder_argument_{i}",
                    annotation=ast.Name(id="float", ctx=ast.Load()),
                ))

    # Raises ValueError if e.g. body is empty.
    # Raises TypeError if no (return) statement is provided in body
    # Raises SyntaxError if module contains invalid syntax (e.g. return outside of
    # function)
    # Can also raise MemoryError and RecursionError
    code = compile(
        ast.fix_missing_locations(module),
        filename="tmp",
        mode="exec",
    )
    namespace = {}

    exec(code, namespace)

    return namespace.get(FUNCTION_NAME, None)
