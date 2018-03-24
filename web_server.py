from flask import Flask, json

from csv_parser import get_people

app = Flask(__name__)


@app.route('/')
def list_people():
    with open('students.csv') as csv_file:
        people = list(get_people(csv_file))
        return json.dumps(people)
