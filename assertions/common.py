from math import isclose


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
        expected: int | float | list[int | float],
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
