from flask import Flask, render_template, redirect, url_for, request
from db import selectAllPersons, insertNewPerson, selectPersonBy, deletePersonBy, updatePerson
from Person import Person


app = Flask(__name__)


@app.route("/")
def home():
    personList = selectAllPersons()
    return render_template("home.html", persons=personList)


@app.route("/new", methods=["GET", "POST"])
def new_person():
    if request.method == "GET":
        return render_template("new.html")
    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        salary = request.form.get("salary")
        person = Person(name, age, salary)
        insertNewPerson(person)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/show/<int:id>")
def show_person(id):
    person = selectPersonBy(id)
    return render_template("show.html", person=person)


@app.route("/delete/<int:id>")
def delete_person(id):
    deletePersonBy(id)
    return redirect(url_for("home"))


"""
update
    en el get -> update.html con el form y
    los datos del registro que quiero cambiar
    en el update.html -> quiero ir a la ruta update con metodo post
    y cambiar en la bd el registro
"""


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_person(id):
    if request.method == "GET":
        person = selectPersonBy(id)
        return render_template("update.html", person=person)
    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        salary = request.form.get("salary")
        person = Person(name, age, salary, id)
        updatePerson(person)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route("/card/<nameAuth>/<int:idAuth>", methods=["GET", "POST"])
def card(nameAuth, idAuth):
    if request.method == "GET":
        print(nameAuth, idAuth)
        return render_template("card.html", nameAuth=nameAuth, idAuth=idAuth)
    elif request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        return f"{name} {phone} hey que cool gracias por el post, buena onda {nameAuth} {idAuth}"


if __name__ == "__main__":
    app.run(debug=True)
