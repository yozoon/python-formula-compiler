# Excel Formula Compiler

This repository provides a parser for a subset of Excel formula operations. The parsed formula can then be compiled into a Python callable and used like a native Python function. Currently, only single valued formulae are supported.

It is based on a simplified version of the Pascal parser written by Ruslan Spivak.

## Supported Operations

* +, -, *, /, ^, (, )
* LN
* EXP
* SQRT
* ROUND
* X (placeholder for the numeric input, e.g. ROUND(X))
