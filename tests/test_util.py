import os
import pytest
from src.util import dir_exists, create_dir, delete_dir 

def test_directory_exists(tmp_path):
    """Test that dirExists returns True for an existing directory."""
    base_dir = tmp_path
    target_dir = "test_dir"
    os.mkdir(os.path.join(base_dir, target_dir))
    assert dir_exists(str(base_dir), target_dir) is True

def test_directory_does_not_exist(tmp_path):
    """Test that dirExists returns False for a non-existent directory."""
    base_dir = tmp_path
    target_dir = "non_existent_dir"
    assert dir_exists(str(base_dir), target_dir) is False

def test_path_is_a_file(tmp_path):
    """Test that dirExists returns False when the path is a file."""
    base_dir = tmp_path
    target_file = "test_file.txt"
    with open(os.path.join(base_dir, target_file), "w") as f:
        f.write("test content")
    assert dir_exists(str(base_dir), target_file) is False

@pytest.mark.asyncio
async def test_create_dir_async(tmp_path):
    """
    Test that the async function successfully creates a directory.
    `tmp_path` is a pytest fixture that provides a temporary directory for the test.
    """
    base_dir = tmp_path
    dir_name = "test_async_dir"
    full_path = os.path.join(base_dir, dir_name)

    assert not os.path.exists(full_path)

    await create_dir(base_dir, dir_name)

    assert os.path.exists(full_path)
    assert os.path.isdir(full_path)

@pytest.mark.asyncio
async def test_create_dir_already_exists(tmp_path):
    """
    Test that the function raises a FileExistsError if the directory already exists.
    """
    base_dir = tmp_path
    dir_name = "existing_dir"
    os.mkdir(os.path.join(base_dir, dir_name))

    with pytest.raises(FileExistsError):
        await create_dir(base_dir, dir_name)

@pytest.mark.asyncio
async def test_remove_dir_async(tmp_path):
    """
    Test that the async function successfully removes an existing directory.
    """
    base_dir = tmp_path
    dir_name = "test_dir_to_remove"
    full_path = os.path.join(base_dir, dir_name)
    os.mkdir(full_path)

    assert os.path.exists(full_path)

    await delete_dir(str(base_dir), dir_name)

    assert not os.path.exists(full_path)
    assert not os.path.isdir(full_path)

@pytest.mark.asyncio
async def test_remove_non_existent_dir(tmp_path):
    """
    Test that the function raises a FileNotFoundError if the directory
    to be removed does not exist.
    """
    base_dir = tmp_path
    dir_name = "non_existent_dir"
    full_path = os.path.join(base_dir, dir_name)

    assert not os.path.exists(full_path)

    with pytest.raises(FileNotFoundError):
        await delete_dir(str(base_dir), dir_name)