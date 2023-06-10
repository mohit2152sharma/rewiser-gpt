#!/usr/local/bin/python

from rewiser.files import concat_files, sort_files
import logging
from rewiser.anki import pseudo_anki
from rewiser.email import Emailer


def main() -> None:
    # read files
    files = sort_files()

    # select files
    selected_files = pseudo_anki(filenames=files)
    logging.info(f"selected files: {selected_files}")
    print(f"selected files: {selected_files}")
    # concatenate files
    content = concat_files(filepaths=selected_files)

    # send email
    emailer = Emailer(body=content)
    emailer.send_email()
    logging.info(f"Email send successfully to: {emailer.to} from: {emailer.frm}")
    print("email send")


if __name__ == "__name__":
    logging.basicConfig(level=logging.INFO)
    main()
