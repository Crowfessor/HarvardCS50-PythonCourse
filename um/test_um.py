from um import count

def main():
    test_a()
    test_b()
    test_c()


def test_a():
    assert count("um") == 1

def test_b():
    assert count("um, um. yummy") == 2

def test_c():
    assert count("Um, hello babe") == 1
    assert count("asdfghsad") == 0
