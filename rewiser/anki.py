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
    # first_file = filenames[-1]
    #
    # min_date = file_commit_date(first_file)
    # min_date = datetime.strptime(min_date, "%Y-%m-%d").date()
    #
    # dates_to_send = []
    # date_variable = current_date
    # i = 0
    # while current_date - timedelta(2 * i) > min_date:
    #     date_variable = current_date - timedelta(2 * i)
    #     dates_to_send.append(date_variable.strftime("%Y-%m-%d"))
    #     i += 1
    # result = [f for f in filenames if file_commit_date(f) in dates_to_send]
    # logging.info(f"files selected: {result}")
    # return result

    result = []
    for file in filenames:
        d = datetime.strptime(file_commit_date(file), "%Y-%m-%d").date()

        revision_date = d + timedelta(days=1)
        delta = 1
        revision_dates = [revision_date.strftime("%Y-%m-%d")]
        while revision_date <= current_date:
            new_date = revision_date + timedelta(days=2**delta)
            revision_dates.append(new_date.strftime("%Y-%m-%d"))
            # delta = (new_date - revision_date).days
            delta += 1
            revision_date = new_date
        if current_date.strftime("%Y-%m-%d") in revision_dates:
            result.append(file)
    logging.info(f"files selected: {result}")
    return result


# def find_revision_date(init_date):
#     d = datetime.strptime(init_date, "%Y-%m-%d").date()
#     current_date = datetime.now().date()
#     revision_date = d + timedelta(days=1)
#     delta = 1
#
#     revision_dates = [revision_date.strftime("%Y-%m-%d")]
#     i = 1
#     while revision_date <= current_date:
#         new_date = revision_date + timedelta(days=2**i)
#         revision_dates.append(new_date.strftime("%Y-%m-%d"))
#         # delta = (new_date - revision_date).days
#         i += 1
#         revision_date = new_date
#     return revision_dates
#
#
# d = find_revision_date("2023-05-30")
# print(d)
