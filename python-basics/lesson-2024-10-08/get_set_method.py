from datetime import date


class Person:
    def __init__(self, first_name: str, age: int):
        # Initialization

        self.first_name = first_name
        self.__last_name = ""  # private
        self.age = age

    def get_last_name(self):  # get_<attribute>
        if len(self.__last_name) == 0:
            raise ValueError("The last name has not been set yet")
        return self.__last_name

    def set_last_name(self, value):  # set_<attribute>
        if len(value) > 2:
            self.__last_name = value
        else:
            raise ValueError("The last name must be greater than 2 characters")

    def get_names(self):
        return f"{self.first_name} {self.get_last_name()}"

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

        age = cls.year_difference(date.today().year, birth_year)
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

        age = cls.year_difference(date.today().year, person_birth_year)
        return cls(first_name, last_name, age)

        # return cls.from_birth_year(first_name, last_name, person_birth_year)

    @staticmethod
    def year_difference(year_1, year_2):
        return abs(year_1 - year_2)


if __name__ == "__main__":
    man6 = Person("Kevin", 50)
    man6.get_info()  # Exception raised: last_name is not yet set
    man6.set_last_name("h")  # Exception raised: last_name must be > 2

    man6.set_last_name("Eyong")
    print(man6.get_info())  # 'Hi there, I am Kevin Eyong, and I am 50 years old'
