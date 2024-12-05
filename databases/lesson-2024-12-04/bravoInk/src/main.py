from src import db


def main():
    # Fetch all employees
    # employees: list[rowFetchedData] = fetch_all()
    # print(employees)

    # Fetch by id
    # id_ = int(input("Enter an id: "))
    # employee = db.fetch_by_id(id_)
    # print(employee)

    # highly_paid_employee = db.fetch_highly_paid(2)
    # print(highly_paid_employee)

    # employee_without_gender = db.count_employee_without_gender()
    # print(employee_without_gender)

    highest_paid_emp_age = db.age_of_highest_paid_employee()
    print(highest_paid_emp_age)


if __name__ == "__main__":
    main()
