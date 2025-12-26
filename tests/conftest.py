import os.path

import pytest

TESTING_DIR = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def resource_path():
    """Fixture that returns a function to get paths to test resources."""
    def _get_resource_path(filename):
        # type: (str) -> str
        return os.path.join(TESTING_DIR, 'resources', filename)
    return _get_resource_path

