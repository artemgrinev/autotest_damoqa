from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    departament: str = None


@dataclass
class Date:
    date: str = None
    day: str = None
    month: str = None
    year: str = None
    time: str = None
