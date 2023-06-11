from functools import wraps
import os
import logging
import markdown
import inspect
from datetime import datetime
from typing import Any, Callable


def read_env_var(var: str, default: Any = None, raise_error: bool = True) -> str:
    """Reads a given environment variable from environment.

    Args:
        var: environment variable to read
        default: default value of environment variable if it is not in environment
        raise_error: if True raises error if the environment variable is not found and default value is `None`

    Raises:
        ValueError: when environment variable is not found and default value is `None`

    Returns:
        environment variable's value
    """
    # if running in github pipeline, append INPUT_ word to environment variable
    if os.getenv("GITHUB_ACTIONS") == "true":
        var = f"INPUT_{var}"
        logging.info("Code is running in github action pipeline, appending INPUT_")

    result = os.getenv(var, default)
    if result is None and raise_error:
        raise ValueError(
            f"The environment variable: {var} is not defined in environment"
        )
    return result


def env_var(var: str, default: Any = None, raise_error: bool = True) -> Callable:
    """A decorator function to read environment variable and pass it on to a function. The decorated function must have a parameter named and lowercased `var`.

    Args:
        var: environment variable to read
        default: default value of environment variable if it is not in environment
        raise_error: if True raises error if the environment variable is not found and default value is `None`

    Returns:
        Decorated function
    """

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # read the parameter space of function
            if os.getenv("GITHUB_ACTIONS") == "true":
                func_var = var.replace("INPUT_", "").lower()
            else:
                func_var = var.lower()

            func_args = inspect.getfullargspec(func).args
            arg_index = func_args.index(func_var)

            # if parameter is not passed as key word argument
            # check the positional indexes, if args[arg_index]
            # throws an error that means the parameter was also
            # not passed as positional argument, then pass the
            # environment variable

            if func_var not in kwargs:
                try:
                    if args[arg_index]:
                        pass
                except:
                    rs = read_env_var(var=var, default=default, raise_error=raise_error)
                    kwargs[func_var] = rs
                    print(f"modified kwargs: {kwargs}")
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorate


def check_val(val: Any, env_var: str) -> Any:
    return val if val else read_env_var(env_var)


def md_to_html(
    content: str,
    style="material",
    cssstyles="padding: 10px 10px 10px 20px; border-radius: 6px",
) -> str:
    html = markdown.markdown(
        content,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.codehilite",
        ],
        extension_configs={
            "markdown.extensions.codehilite": {
                "pygments_style": style,
                "noclasses": True,
                "cssstyles": cssstyles,
            },
        },
    )
    return html


def file_created_date(file: str):
    t = os.path.getctime(file)
    d = datetime.fromtimestamp(t).date()
    print(f"file created date for file: {file} is {d}")
    return d
