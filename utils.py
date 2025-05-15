def process_summa(number_1: int, number_2: int) -> int:
    result = number_1 + number_2
    return result


def process_devision(dividend: int, *, divisor: int) -> float:
    if not divisor:
        raise ValueError("zero as divisor was provided")
    # return 0.0
    quotient = dividend / divisor
    return quotient


def process_substraction(*, subtrahend: int, minuend: int) -> int:
    difference = subtrahend - minuend
    return difference


def process_mult(number_1: int, number_2: int) -> int:
    result = number_1 * number_2
    return result
