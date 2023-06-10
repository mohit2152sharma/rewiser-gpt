import os
from typing import List

from rewiser.utils import env_var


@env_var(var="DOC_DIRECTORY")
def list_files(
    doc_directory: str | None = None, return_style: str = "filepath"
) -> List[str]:
    """List files in the given directory

    Args:
        doc_directory: directory path where all the documents are kept. The directory
        path is relative to project's or repository's root folder
        return_style: either `'filepath'` or `'filename'`, if it is equal to
        `'filepath'`, returns the filepath by appending `doc_directory`. If it is
        `'filename'` returns just the filenames

    Returns:
        List of file names
    """
    if return_style == "filepath":
        return [os.path.join(doc_directory, f) for f in os.listdir(doc_directory)]  # type: ignore
    elif return_style == "filename":
        return list(os.listdir(doc_directory))
    else:
        raise ValueError(
            f"The return style: {return_style} provided is invalid. Valid values are `filepath` and `filename`"
        )


@env_var(var="DOC_DIRECTORY")
def sort_files(doc_directory: str | None = None) -> List[str]:
    files = list_files(doc_directory=doc_directory, return_style="filepath")
    rs = sorted(files, key=lambda x: os.path.getctime(x), reverse=True)
    return rs


def read_file(filepath: str) -> str:
    with open(filepath, "r") as file:
        content = file.read()

    return content


def extract_filename(filepath: str) -> str:
    return os.path.splitext(os.path.split(filepath)[-1])[1]


def concat_files(filepaths: List[str]) -> str:
    result = ""
    for file in filepaths:
        content = read_file(file)
        heading = extract_filename(file).capitalize()
        result += f"# {heading}\n{content}\n\n"

    return result


# print(sort_files(files=relative_file_path(list_files("tests"), "tests")))
