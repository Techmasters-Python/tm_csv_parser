from io import StringIO

from csv_parser import get_people


def test_get_people():
    # What is StringIO? Google!
    with StringIO("name,org,is_student\na,b,c\nc,d,e\n") as data:
        # simulates a file object ;) we are mocking!
        output = list(get_people(data))
        expectation = [
            {'name': 'a', 'org': 'b', 'is_student': 'c'},
            {'name': 'c', 'org': 'd', 'is_student': 'e'},
        ]
        assert output == expectation
