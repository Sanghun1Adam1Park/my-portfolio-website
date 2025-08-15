"""Tests for loggin.py"""

import asyncio
from unittest.mock import patch
import pytest
from src.log import log_call, log_async_call

# Test functions
@log_call
def add_sync(a: int, b: int):
    """Functions made for testing logger for functions."""
    return a + b

@log_async_call
async def add_async(a: int, b: int):
    """Functions made for testing logger for async functions."""
    await asyncio.sleep(0.01) 
    return a + b

# Corrected synchronous test
def test_sync_logs_and_returns_correctly():
    """Test that the add_sync function correctly logs its call and returns the correct value."""
    with patch('logging.info') as mock_log:
        result = add_sync(1, 2)

        assert result == 3

        # Assert the logger was called with the unformatted string and arguments
        # The first argument is the format string, the rest are the args
        expected_call = ("Calling '%s' with args: (%s)", 'add_sync', '1, 2')
        expected_return = ("'%s' returned: %s", 'add_sync', '3')
        
        assert mock_log.call_count == 2
        mock_log.assert_any_call(*expected_call)
        mock_log.assert_any_call(*expected_return)


# Corrected asynchronous test
@pytest.mark.asyncio
async def test_async_logs_and_returns_correctly():
    """Test that the add_async function correctly logs its call and returns the correct value."""
    with patch('logging.info') as mock_log:
        result = await add_async(1, 2)

        assert result == 3

        # Assert the logger was called with the unformatted string and arguments
        expected_call = ("Calling async function '%s' with args: (%s)", 'add_async', '1, 2')
        expected_return = ("Async function '%s' returned: %s", 'add_async', '3')
        
        assert mock_log.call_count == 2
        mock_log.assert_any_call(*expected_call)
        mock_log.assert_any_call(*expected_return)