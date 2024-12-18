"""Connect to the database"""

import environs
import psycopg as pg
from src.utils import ROOT_DIR

# Set up the environment variable
## Instantiate the environ
env = environs.Env()

# Provide path to the .env file
env.read_env(str(ROOT_DIR / ".env"))  # operator overloading


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
            # Consume secret info from the environment variable.
            dbname=env.str("dbname"),
            user=env.str("user"),
            password=env.str("password"),
            # host,
            # port
        )
