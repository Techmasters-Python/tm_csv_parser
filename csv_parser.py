import csv


def get_people(csv_file):
    return csv.DictReader(csv_file)


def print_people(people):
    for person in people:
        print(f'"{person["name"]}" works at "{person["org"]}"')


def main():
    with open('students.csv') as csv_file:
        people = get_people(csv_file)
        print_people(people)


if __name__ == '__main__':
    main()
