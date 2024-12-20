from src.db.database import Database


def insert_data(
    isbn,
    title,
    edition,
    description,
    page_count,
    category,
    published_date,
    publisher,
    authors,
    lang,
    format,
):
    CONN = Database()

    query = """
        INSERT INTO project.book(
            isbn,
            title,
            edition,
            description,
            page_count,
            category,
            published_date,
            publisher,
            authors,
            lang,
            format
        )VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s,%s,%s) RETURNING *;
    """

    with CONN.cursor() as cursor:
        cursor.execute(
            query,
            (
                isbn,
                title,
                edition,
                description,
                page_count,
                category,
                published_date,
                publisher,
                authors,
                lang,
                format,
            ),
        )
        inserted_book = cursor.fetchone()
        CONN.commit()
        return inserted_book
