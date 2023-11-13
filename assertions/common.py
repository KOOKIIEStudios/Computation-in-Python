from decimal import *
from math import isclose


# Pure-Python assertions -------------------------------------------------------
def validate_condition(
        condition: bool,
        error_message: str,
        success_message: str,
) -> None:
    if condition:
        print(success_message)
        return
    print(error_message)


def validate_float(
        given: int | float,
        expected: int | float,
) -> bool:
    if isclose(given, expected, rel_tol=1e-5):
        return True
    return False


def validate_floats(
        given: int | float,
        expected: int | float | Decimal | list[int | float | Decimal],
        error_message: str,
        success_message: str,
) -> None:
    """Checks if the given value is close to the expected value
    
    Expected value can either be a single value or a list of values.
    If a list is provided, any single element of the list being a match
    will qualify as matching, and cause the success message to be printed.
    """
    is_correct = False

    if isinstance(expected, list):    
        for element in expected:
            if validate_float(element):
                is_correct = True
    else:
        is_correct = validate_float(expected)

    if is_correct:
        print(success_message)
        return
    print(error_message)


# Math-related convenience functions  ------------------------------------------
# Different languages/applications/calculators use different rounding strategies
# Python 2 uses the simple round 0.5 to up; Python 3 uses banker's rounding
# Rounding permutation getters will generate all plausible rounding strategy
#   results from a single number, and return them as a list
def get_rounding_permutations(target: int | float, dp: Decimal) -> list[Decimal]:
    raw = Decimal(target)
    buffer = []
    # buffer.append(raw.quantize(dp, rounding=ROUND_CEILING))
    # buffer.append(raw.quantize(dp, rounding=ROUND_FLOOR))
    # buffer.append(raw.quantize(dp, rounding=ROUND_UP))
    # buffer.append(raw.quantize(dp, rounding=ROUND_DOWN))
    buffer.append(raw.quantize(dp, rounding=ROUND_HALF_DOWN))
    buffer.append(raw.quantize(dp, rounding=ROUND_HALF_EVEN))
    buffer.append(raw.quantize(dp, rounding=ROUND_HALF_UP))
    buffer.append(raw.quantize(dp, rounding=ROUND_05UP))
    return buffer


def get_2dp_rounding_permutations(target: int | float) -> list[Decimal]:
    return get_rounding_permutations(target, Decimal(.01))


def get_1dp_rounding_permutations(target: int | float) -> list[Decimal]:
    return get_rounding_permutations(target, Decimal(.1))


def get_int_rounding_permutations(target: int | float) -> list[Decimal]:
    return get_rounding_permutations(target, Decimal(1.))
