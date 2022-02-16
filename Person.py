class Person:
    def __init__(self, name, age, salary, id=0) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.age}, {self.salary}, {self.id})"
