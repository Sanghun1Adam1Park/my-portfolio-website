"""Module for logging"""

import functools
import logging


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_call(func):
    """A decorator that logs a function call with its arguments.

    Args:
        func (non-asnyc): function to be looged

    Returns:
        _type_: wrapped function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_string = ', '.join(
            [repr(arg) for arg in args] +
            [f"{key}={repr(value)}" for key, value in kwargs.items()]
        )
        logging.info("Calling '%s' with args: (%s)", func.__name__, arg_string)
        result = func(*args, **kwargs)
        logging.info("'%s' returned: %s", func.__name__, repr(result))
        return result
    return wrapper


def log_async_call(func):
    """An async decorator that logs an async function call with its arguments.

    Args:
        func (async): function to be logged

    Returns:
        _type_: wrapped function
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        arg_string = ', '.join(
            [repr(arg) for arg in args] +
            [f"{key}={repr(value)}" for key, value in kwargs.items()]
        )
        logging.info("Calling async function '%s' with args: (%s)",
                     func.__name__, arg_string)
        result = await func(*args, **kwargs)
        logging.info("Async function '%s' returned: %s",
                     func.__name__, repr(result))
        return result
    return wrapper
