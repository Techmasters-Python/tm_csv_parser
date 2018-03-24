import csv


def get_csv_data(file_path='students.csv'):
    """
    Get the list of students along with organization.
    """
    with open(file_path) as csv_file:
        # this with thingy is called a "context manager"
        # google it up ;)
        return csv_file.read()


def get_lines(csv_data):
    """
    Split individual lines from a csv text
    """
    return csv_data.splitlines()


def get_people(csv_data):
    lines = get_lines(csv_data)
    reader = csv.reader(lines)
    return map(lambda x: {'name': x[0], 'org': x[1], 'is_student': x[2]}, reader)


def print_people(people):
    for person in people:
        print(f'"{person["name"]}" works at "{person["org"]}"')


def main():
    csv_data = get_csv_data()
    people = get_people(csv_data)
    print_people(people)


if __name__ == '__main__':
    main()
