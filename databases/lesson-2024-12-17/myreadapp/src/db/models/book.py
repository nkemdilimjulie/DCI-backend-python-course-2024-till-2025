from src.db.queries import book as book_queries


class Book:
    def __init__(
        self,
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
        read_estimated_time_in_minutes=None,
    ):
        self.isbn = isbn
        self.title = title
        self.edition = edition
        self.description = description
        self.page_count = page_count
        self.category = category
        self.published_date = published_date
        self.publisher = publisher
        self.authors = authors
        self.lang = lang
        self.format = format
        self.read_estimated_time_in_minutes = read_estimated_time_in_minutes

    @classmethod
    def insert_data(
        cls,
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
        book = book_queries.insert_data(
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
        )
        return cls(*book) if book else None
