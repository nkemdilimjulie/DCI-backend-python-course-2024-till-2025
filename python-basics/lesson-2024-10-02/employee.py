from datetime import date


class Employee:  # class Employee(object)

    def __init__(
        self, first_name: str, last_name: str, hired_date: date, rate_per_hour: float
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hired_date = hired_date
        self.rate_per_hour = rate_per_hour

    def get_names(self):
        return f"{self.first_name} {self.last_name}"

    def get_pay_per_year(self):
        # 52 weeks * 5 days * 8 hours a day
        pay = 52 * 5 * 8 * self.rate_per_hour
        return pay


class Manager(Employee):  # Single
    def __init__(
        self, first_name, last_name, hired_date, rate_per_hour, travel_perk=True
    ):
        # Initialize the child class
        self.travel_perk = travel_perk
        self.reports = []

        # Initialize the parent class
        super().__init__(first_name, last_name, hired_date, rate_per_hour)

    def get_report(self):
        return self.reports

    def request_report(self, report):
        self.reports.append(report)

    def travel(self):
        if self.travel_perk:
            print("Travel request granted")
        else:
            print("Not enough travel perk to travel")

    def get_pay_per_year(self, bonus=True):
        # Method Overriding

        pay = super().get_pay_per_year()  # call parent's method
        if bonus:
            # 10% of his pay
            return pay + (0.1 * pay)
        return pay


class SoftwareEngineer(Employee):  # Single
    # TODO: Replace 'pass' with your code
    pass
