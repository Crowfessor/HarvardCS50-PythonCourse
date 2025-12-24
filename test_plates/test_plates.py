from plates import is_valid


def main():
    test_plate0()
    test_plate1()
    test_plate2()
    test_plate3()
    test_plate4()


def test_plate0():
    assert is_valid("c")==False
def test_plate1():
    assert is_valid("hello, world")==False
def test_plate2():
    assert is_valid("cs.,32")==False
def test_plate2():
    assert is_valid("CS50")==True
def test_plate3():
    assert is_valid("23")==False
    assert is_valid("CS")==True
def test_plate4():
    assert is_valid("CS05")==False
    assert is_valid("CS50")==True
    assert is_valid("A2") == False
    assert is_valid("cs50p") == False
    assert is_valid("JEMAPELLE") == False
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()
