from bank import value


def main():
    test_case_sence()
    test_correct_values()
    test_check_phrases()

def test_case_sense():

    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('hEllO') == 0


def test_correct_values():
    assert value('hello') == 0
    assert value('hi') == 20
    assert value('yo') == 100

def test_check_phrases():
    assert value("What's happening?") == 100
    assert value("How you doing?") == 20


if __name__ == "__main__":
    main()
