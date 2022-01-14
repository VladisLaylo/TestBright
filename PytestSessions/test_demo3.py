def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "Test failed"
    assert a == b, "Test failed as a is not equal to b"


def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"


def test_m3():
    assert True


def test_login():
    assert "admin" == "admin"
