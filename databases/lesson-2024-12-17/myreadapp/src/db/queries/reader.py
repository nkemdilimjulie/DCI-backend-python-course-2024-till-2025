from src.db.database import Database


def insert_data(username, title, first_name, last_name):
    CONN = Database()

    query = """
        INSERT INTO project.reader(
            username,
            title,
            first_name,
            last_name
        )VALUES (%s, %s, %s, %s) RETURNING *;
    """

    with CONN.cursor() as cursor:
        cursor.execute(query, (username, title, first_name, last_name))
        inserted_reader = cursor.fetchone()
        CONN.commit()
        return inserted_reader  # (id, username, title, first_name, last_name)
