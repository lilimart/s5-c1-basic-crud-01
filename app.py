from flask import Flask, render_template, redirect, url_for, request
from db import selectAllPersons, insertNewPerson
from Person import Person


app = Flask(__name__)


@app.route("/")
def home():
    personList = selectAllPersons()
    return render_template("home.html", persons=personList)


@app.route("/new")
def new_person():
    return render_template("new.html")


@app.route("/insert", methods=["POST"])
def insert_person():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        salary = request.form.get("salary")
        person = Person(name, age, salary)
        insertNewPerson(person)
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
