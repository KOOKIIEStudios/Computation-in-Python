import assertions.common as common


def check_assignment(amount: int | float) -> None:
    common.validate_floats(
        amount,
        210,
        "I don't think that's the right answer...",
        f"Your answer was ${amount:.2f}! Good job!",
    )
