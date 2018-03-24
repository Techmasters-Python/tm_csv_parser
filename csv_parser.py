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


def get_students(csv_data):
    lines = get_lines(csv_data)
    return csv.reader(lines)


def print_students(students):
    for name, org, is_student in students:
        print(f'"{name}" works at "{org}"')


def main():
    csv_data = get_csv_data()
    students = get_students(csv_data)
    print_students(students)


if __name__ == '__main__':
    main()
