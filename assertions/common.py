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


def validate_floats(
        given: int | float,
        expected: int | float,
        error_message: str,
        success_message: str,
) -> None:
    if isclose(given, expected, rel_tol=1e-5):
        print(success_message)
        return
    print(error_message)
