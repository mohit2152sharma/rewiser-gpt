from typing import List

from rewiser.utils import file_commit_date
from datetime import datetime, timedelta


def pseudo_anki(filenames: List[str]) -> List[str]:
    """Given a the sorted list of files, decides which one to include to send.

    Args:
        filenames: list of sorted file names

    Returns:
        filtered filenames based on anki
    """
    # the start date should be the minimum of rewiser data date
    # from the start date to current date, we can create a sequence of
    # dates at regular intervals
    # let start date be s
    # date sequence = s, s+2, s+2^2, s+2^3......current date
    # select files matching the date s

    current_date = datetime.utcnow().date()
    first_file = filenames[-1]

    min_date = file_commit_date(first_file)
    min_date = datetime.strptime(min_date, "%Y-%m-%d").date()

    dates_to_send = []
    date_variable = current_date
    i = 0
    while current_date - timedelta(2**i) > min_date:
        date_variable = current_date - timedelta(2**i)
        dates_to_send.append(date_variable)
        i += 1

    result = [f for f in filenames if file_commit_date(f) in dates_to_send]
    return result
