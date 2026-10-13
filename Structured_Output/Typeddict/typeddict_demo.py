from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {
    "name": "Debabrata Bhowmik",
    "age": 20,
    "email": "debabrata.bhowmik@example.com"
}

print(new_person)