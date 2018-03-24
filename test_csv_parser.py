from csv_parser import get_lines, get_students


def test_get_lines():
    assert get_lines('a\nb') == ['a', 'b']


def test_get_students():
    data = "a,b\nc,d"
    output = list(get_students(data))
    expectation = [['a', 'b'], ['c', 'd']]
    assert output == expectation
