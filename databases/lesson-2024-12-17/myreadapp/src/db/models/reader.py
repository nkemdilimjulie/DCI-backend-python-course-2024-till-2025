from src.db.queries import reader as reader_queries


class Reader:
    def __init__(self, username, title, first_name, last_name):
        self.username = username
        self.title = title
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def insert_data(cls, username, title, first_name, last_name):
        reader = reader_queries.insert_data(username, title, first_name, last_name)

        return cls(*reader) if reader else None
