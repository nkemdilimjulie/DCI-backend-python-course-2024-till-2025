from datetime import date
from decimal import Decimal

import psycopg as pg

CONN = pg.connect(dbname="dci", user="postgres", password="postgres")

# Data types
rowFetchedData = tuple[int, str, date, str, str, str, Decimal]


# TODO: SELECT
def fetch_all():
    """Fetch all employee"""
    # define our query
    query = "SELECT * FROM company.employee;"

    # create a cursor: -> permits us to run queries in our database
    with CONN.cursor() as cursor:
        # execute the query
        cursor.execute(query)
        # Fetch the info and return
        employees = cursor.fetchall()
        return employees


def fetch_by_id(id_):
    """Fetch employee by id"""

    # query -- SQL injection
    query = """
        SELECT *
        FROM company.employee
        WHERE id=%s;
    """
    # execute the query
    with CONN.cursor() as cursor:
        # best way to prevent sql injection with psycopg
        cursor.execute(query, (id_,))

        # Fetch the row and return
        employee = cursor.fetchone()
        return employee


def fetch_highly_paid(limit):
    """Fetch a limited number of highly paid employees"""
    # 1. query
    query = """
        SELECT * 
        FROM company.employee 
        WHERE 
            salary IS NOT NULL 
        ORDER BY salary DESC 
        LIMIT %s;
    """

    # 2. execute
    with CONN.cursor() as cursor:
        # execute query
        cursor.execute(query, (limit,))
        employees = cursor.fetchall()
        return employees


def count_employee_without_gender():
    """count the number of employee who didn't provide their gender"""
    # query
    query = """
        SELECT id
        FROM company.employee
        WHERE gender IS NULL;
    """
    # 2. execute
    with CONN.cursor() as cursor:
        # execute query
        cursor.execute(query)
        employees = cursor.fetchall()
        return len(employees)


def age_of_highest_paid_employee():
    """get the age of one of the highest paid employee"""
    # query = """
    #     SELECT EXTRACT(YEAR FROM NOW()) - EXTRACT(YEAR FROM date_of_birth)
    #     FROM company.employee
    #     ORDER BY salary DESC
    #     LIMIT 1;
    # """

    query = """
        SELECT EXTRACT(YEAR FROM age(date_of_birth))::INT
        FROM company.employee
        ORDER BY salary DESC
        LIMIT 1;
    """
    with CONN.cursor() as cursor:
        # execute query
        cursor.execute(query)
        employee_age = cursor.fetchone()
        return employee_age[0] if employee_age else None


# TODO: INSERT
def insert_data(data: tuple[str, str, str, str, str, str]):
    query = """
        INSERT INTO company.employee
        VALUES(DEFAULT, %s, %s, %s, %s, %s, %s)
        RETURNING *;
    """

    with CONN.cursor() as cursor:
        cursor.execute(query, data)

        inserted_employee = cursor.fetchone()
        # Any thing that will modify the state of your database needs to be committed
        # insert
        # update
        # delete , truncate
        CONN.commit()
        return inserted_employee


# TODO: UPDATE
def update_first_name(id_, new_first_name):
    query = """
    UPDATE company.employee
    SET first_name = %s
    WHERE id=%s
    RETURNING id, first_name;
    """

    with CONN.cursor() as cursor:
        cursor.execute(query, (id_, new_first_name))
        updated_values = cursor.fetchone()
        CONN.commit()
        return updated_values


# TODO: UPDATE last_name
# TODO: UPDATE email


# TODO: DELETE
# TODO: Delete by id
def delete_by_id(id_):
    query = """
        DELETE FROM company.employee 
        WHERE id=%s
        RETURNING id;
    """
    with CONN.cursor() as cursor:
        cursor.execute(query, (id_,))
        deleted_id = cursor.fetchone()
        CONN.commit()
        return deleted_id


# TODO: DELETE many items.
## TODO: DELETE using BETWEEN
## TODO: DELETE using IN
