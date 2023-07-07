import os
from typing import List, Dict
import re
import json

from langchain import PromptTemplate

from rewiser.utils import module_dir


def split_numbered_lines(text: str) -> List[str]:
    """splits the given text into a list of texts. The text is assumed to be a numbered
    list and is split on each numbered item.

    Args:
        text: a string which is a numbere list

    Returns:
        List of strings where each element corresponds to the line item
    """
    pattern = "^\d+. |\n +\d+."
    splits = re.split(pattern=pattern, string=text)
    result = [x.strip() for x in splits if x]
    return result


def read_templates() -> Dict[str, str]:
    dir = module_dir()
    file_path = os.path.join(dir, "gpt", "templates.json")
    with open(file_path, "r") as file:
        configs = json.load(file)
    return configs


def create_prompt_template(
    template_name: str, templates: Dict | None = None
) -> PromptTemplate:
    if not templates:
        templates = read_templates()
    template = templates[template_name]
    return PromptTemplate(
        template=template["prompt_text"], input_variables=template["input_variables"]  # type: ignore
    )
