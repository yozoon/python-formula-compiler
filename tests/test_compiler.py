from formula_compiler.compiler import compile_formula


def test_compiler():
    fun = compile_formula(formula="X", n_args=1, strict=True)
    assert fun is not None
    assert fun(42) == 42
