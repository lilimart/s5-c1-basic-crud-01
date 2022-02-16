from flask import Flask, render_template
from db import selectAllPersons


app = Flask(__name__)


@app.route("/")
def home():
    personList = selectAllPersons()
    return render_template("home.html", persons=personList)


@app.route("/new")
def new_person():
    return render_template("new.html")


@app.route("/insert")
def insert_person():
    insertNewPerson()


if __name__ == "__main__":
    app.run(debug=True)
