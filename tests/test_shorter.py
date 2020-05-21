import pytest
from src.shorter import Shorter

def test_create_object():
    shorter = Shorter(code='0001')
    assert shorter.code == '0001'

def test_get_url():
    shorter = Shorter(code='0002')
    assert shorter.url == ''
