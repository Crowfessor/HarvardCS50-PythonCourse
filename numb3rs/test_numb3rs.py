from numb3rs import validate


def main():
    test_if_ip_true()
    test_if_ip_false()


def test_if_ip_true():
    assert validate("123.123.123.213") == True
    assert validate("124.123.123.213") == True
    assert validate("125.123.123.213") == True

def test_if_ip_false():
    assert validate("12333.123.1234.123") == False
    assert validate("cat") == False
    assert validate("123.1234.122.245") == False

if __name__ == "__main__":
    main()
