import numpy


def hello(n: int) -> str:
    """Greet the sum from 0 to n (exclusive end)."""
    sum_n = numpy.arange(n).sum()
    return f"Hello {sum_n}!"
