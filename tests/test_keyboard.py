from src.keyboard import KeyBoard
import pytest


kb = KeyBoard('Dark Project KD87A', 9600, 5)


@pytest.fixture
def kb1():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_str(kb1):
    assert str(kb1) == 'Dark Project KD87A'


def test_str_language(kb1):
    assert str(kb1.language) == "EN"


def test_change_lang(kb1):
    kb1.change_lang()
    assert str(kb1.language) == "RU"
    kb1.change_lang().change_lang()
    assert str(kb1.language) == "RU"


def test_private_language(kb1):
    with pytest.raises(AttributeError, match="property 'language' of 'KeyBoard' object has no setter"):
        kb1.language = 'CH'
