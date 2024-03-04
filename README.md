# Python Formula Compiler

This repository provides a parser for a subset of Excel formula operations. The parsed formula can then be compiled into a Python callable and used like a native Python function. Currently, only single valued formulae are supported.

The implementation is based on a simplified version of the Pascal parser written by Ruslan Spivak ([link](https://github.com/rspivak/lsbasi/)).

## Installation

```sh
git clone https://github.com/yozoon/python-formula-compiler.git
cd python-formula-compiler/
pip install .
```

## Supported Operations

* +, -, *, /, ^, (, )
* ROUND
* X (placeholder for numeric input)
* LN
* LOG10
* EXP
* SQRT
* Trigonometric Functions:
  * SIN
  * COS
  * TAN
  * ASIN
  * ACOS
  * ATAN
* Hyperbolic Functions:
  * SINH
  * COSH
  * TANH
  * ASINH
  * ACOSH
  * ATANH
