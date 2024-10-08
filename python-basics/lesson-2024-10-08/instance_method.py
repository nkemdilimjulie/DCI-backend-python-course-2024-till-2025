from datetime import date


class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        # Initialization

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_names(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        full_names = self.get_names()
        return f"Hi there, I am {full_names}, and I am {self.age} years old"

    def get_born_year(self):
        # TODO: Your code goes here.
        # Hint: Subtract age from current year
        # Hint: How do you get current year in Python????
        current_year = date.today().year
        birth_year = current_year - self.age

        return birth_year


if __name__ == "__main__":
    person = Person("Eyong", "Kevin", 30)
    person.get_names()  # 'Eyong Kevin'
