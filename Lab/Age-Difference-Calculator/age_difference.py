from datetime import date
from dateutil.relativedelta import relativedelta
from utils import format_result

def compare_ages(name1, dob1, name2, dob2):
    """
    Compare the ages of two people.

    Parameters
    ----------
    name1 : str
        First person's name.
    dob1 : date
        First person's date of birth.
    name2 : str
        Second person's name.
    dob2 : date
        Second person's date of birth.

    Returns
    -------
    dict
        Dictionary containing the comparison result.
    """

    # Same birthday
    if dob1 == dob2:
        return {
            "name": name1,
            "other_name": name2,
            "same_age": True
        }

    # Determine who is older
    if dob1 < dob2:
        relation = "older"
        other_name = name2
        difference = relativedelta(dob2, dob1)
    else:
        relation = "younger"
        other_name = name2
        difference = relativedelta(dob1, dob2)

    return {
        "name": name1,
        "other_name": other_name,
        "same_age": False,
        "relation": relation,
        "years": difference.years,
        "months": difference.months,
        "days": difference.days
    }
