import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")