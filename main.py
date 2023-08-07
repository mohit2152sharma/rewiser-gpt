#!/usr/local/bin/python

import logging

from rewiser.anki import pseudo_anki
from rewiser.email import Emailer
from rewiser.files import concat_files, sort_files


def main() -> None:
    # read files
    files = sort_files()
    # select files
    selected_files = pseudo_anki(filenames=files)
    logging.info(f"selected files: {selected_files}")
    # concatenate files
    content = concat_files(filepaths=selected_files)

    # send email
    if content:
        emailer = Emailer(body=content)
        emailer.send_email()
        logging.info(f"Email send successfully to: {emailer.to} from: {emailer.frm}")
    else:
        logging.info("Content is empty, no email to send")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
