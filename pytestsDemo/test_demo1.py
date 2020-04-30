# Any pytest file should start with test_
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("hello")


@pytest.mark.xfail
def test_secondCreditCard(setup):
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)



