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

    @classmethod
    def from_birth_year(cls, first_name: str, last_name: str, birth_year: int):

        age = date.today().year - birth_year
        return cls(first_name, last_name, age)  # Person(first_name, last_name, age)

    @classmethod
    def from_father_birth_info(
        cls, first_name, last_name, father_birth_year, father_person_age_diff
    ):
        """Create a Person's object

        Params
        --------
        cls (Person): The class
        first_name (str): The first name
        last_name (str): The last name
        father_birth_year (int) The father's year of birth
        father_person_age_diff (int): The age difference between the person and the father.

        Return
        --------
        (Person): Object of the Person

        """
        # TODO: Your code goes here.
        person_birth_year = father_birth_year + father_person_age_diff

        age = date.today().year - person_birth_year
        return cls(first_name, last_name, age)

        # return cls.from_birth_year(first_name, last_name, person_birth_year)


if __name__ == "__main__":
    man = Person.from_birth_year("ora", "lora", 1994)
    print(man.age)  # 30
    print(man.get_info())  # 'Hi there, I am ora lora, and I am 30 years old'

    man1 = Person.from_father_birth_info("kenz", "gat", 1990, 10)

    print(man1.get_info())  # 'Hi there, I am kenz gat, and I am 24 years old'
