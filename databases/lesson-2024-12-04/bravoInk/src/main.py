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

    # highest_paid_emp_age = db.age_of_highest_paid_employee()
    # print(highest_paid_emp_age)

    data = []  # user input to be inserted
    for field, state in [
        ("first_name", "r"),
        ("date_of_birth", "r"),
        ("last_name", "o"),
        ("email", "r"),
        ("gender", "o"),
        ("salary", "o"),
    ]:
        input_data = input(f"{field} {'(Default None)' if state=='o' else ''}")
        if len(input_data) == 0 and state == "o":
            input_data = None
        data.append(input_data)

    result = db.insert_data(data)
    print(result)


if __name__ == "__main__":
    main()
