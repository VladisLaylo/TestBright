import pytest


def test_m4():  # test 4 must fail
    assert False


def test_m5():
    assert 100 == 100


def test_m6():
    assert "vladis" == "VLADIS"


def test_login():
    assert "admin" == "admin"

