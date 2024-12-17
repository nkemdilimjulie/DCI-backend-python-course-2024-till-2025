"""Connect to the database"""

import psycopg as pg

# CREATE CONNECTION
## Singleton class.


class Database(object):
    """Create connection to the database.

    This class is made singleton so that only one instance exists at any point in time.
    """

    _instance = None

    def __new__(cls):  # instantiating the class
        if Database._instance is None:
            Database._instance = super().__new__(cls)
            Database._instance.__init__()

        return Database._instance._conn

    def __init__(self):
        self._conn = pg.connect(
            dbname="dci",
            user="postgres",
            password="postgres",
            # host,
            # port
        )
