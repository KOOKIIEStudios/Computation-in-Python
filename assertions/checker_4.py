import assertions.common as common


def get_electricity_bill() -> float:
    WATTAGE = 300
    RATE = 25  # in cents per kWh

    hours_per_month = 30 * 24
    wattage_in_kW = WATTAGE / 1000

    return RATE * wattage_in_kW * hours_per_month / 100


def get_gross_margin() -> float:
    PROFIT = 69

    electricity_bill = get_electricity_bill()
    return electricity_bill + 69


def get_bill() -> float:
    USER_COUNT = 15
    return get_gross_margin() / 15


def get_bill_permutations():
    # if we're only going for either 2dp or left unrounded (i.e. only one of these),
    # then the validate_floats() would have handled it gracefully
    #
    # in this case, i want both to be considered correct, so i'll just use the helper functions
    # even though this happens to be a case of true division evaluating to `8.2` nicely
    # just so that i can copy-paste this logic easily in future potentially
    # messier situations
    return common.get_2dp_rounding_permutations(get_bill()).append(get_bill())


def check_price(amount: int | float) -> None:
    common.validate_floats(
        amount,
        get_bill_permutations(),
        "I don't think that's the right answer...",
        "That's right! Sheeeeeesh!",
    )
