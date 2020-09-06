import pytest

@pytest.mark.usefixtures('env_setup','driver')
class TestBase:
    pass