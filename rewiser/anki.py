import logging
from datetime import datetime, timedelta
from typing import List

from rewiser.utils import file_commit_date

EF = 2.5


def fib_seq(n) -> list[int]:
    fib = [0, 1]
    # create a fibonacci sequence
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


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

    result = []
    for file in filenames:
        d = datetime.strptime(file_commit_date(file), "%Y-%m-%d").date()

        revision_date = d + timedelta(days=1)
        delta = 1
        revision_dates = [revision_date.strftime("%Y-%m-%d")]
        while revision_date <= current_date:
            new_date = revision_date + timedelta(days=delta * EF)
            revision_dates.append(new_date.strftime("%Y-%m-%d"))
            delta = (new_date - revision_date).days
            revision_date = new_date
        if current_date.strftime("%Y-%m-%d") in revision_dates:
            result.append(file)
    logging.info(f"files selected: {result}")
    return result
