"""Module for utility methods like creating files/directories"""

import os
import asyncio
from src.log import log_call, log_async_call


@log_call
def dir_exists(base_dir: str, target_dir: str) -> bool:
    """Check if the directory exists

    Args:
        base_dir (str): path to base directory
        target_dir (str): path to target directory under base dir

    Returns:
        bool: true if exists, else false
    """
    destiation_path = os.path.join(base_dir, target_dir)
    return os.path.isdir(destiation_path)


@log_async_call
async def create_dir(base_dir: str, dir_name: str):
    """Creates directory asnychrnously

    Args:
        base_dir (str): path to base directory
        dir_name (str): name of directory to be created
    """
    await asyncio.to_thread(os.mkdir, os.path.join(base_dir, dir_name))


@log_async_call
async def delete_dir(base_dir: str, dir_name: str):
    """Removes directory asnychrnously

    Args:
        base_dir (str): path to base directory
        dir_name (str): name of directory to be removed
    """
    await asyncio.to_thread(os.rmdir, os.path.join(base_dir, dir_name))
