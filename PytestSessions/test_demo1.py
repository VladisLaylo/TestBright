def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "Test failed"
    assert a == b, "Test failed as a is not equal to b"


test_m1()  # test a and b not c not d
# change made on master
"""this changed on branch2"""
"""changed on master"""
"""changes made on new-branch"""


def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"


def test_m3():
    assert True


def test_m4():
    assert False


def test_m5():
    assert 100 == 100


def test_m6():
    assert "vladis" == "VLADIS"


def test_login():
    assert "admin" == "admin"
