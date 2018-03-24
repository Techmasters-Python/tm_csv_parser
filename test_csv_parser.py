from csv_parser import get_lines, get_people


def test_get_lines():
    assert get_lines('a\nb') == ['a', 'b']


def test_get_people():
    data = "name,org,is_student\na,b,c\nc,d,e\n"
    output = list(get_people(data))
    expectation = [
        {'name': 'a', 'org': 'b', 'is_student': 'c'},
        {'name': 'c', 'org': 'd', 'is_student': 'e'},
    ]
    assert output == expectation
