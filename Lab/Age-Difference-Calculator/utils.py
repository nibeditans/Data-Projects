def plural(value, singular, plural):
    """
    Return the correct singular or plural word.
    """
    return singular if value == 1 else plural


def format_result(result):
    """
    Convert the comparison result into a readable sentence.
    """

    if result["same_age"]:
        return (
            f"Hello, {result['name']}!\n\n"
            f"You and {result['other_name']} are exactly the same age. 🎉"
        )

    return (
        f"Hello, {result['name']}!\n\n"
        f"You're "
        f"{result['years']} {plural(result['years'], 'year', 'years')}, "
        f"{result['months']} {plural(result['months'], 'month', 'months')}, and "
        f"{result['days']} {plural(result['days'], 'day', 'days')} "
        f"{result['relation']} than {result['other_name']}. 🎉"
    )
