"""Contain tests for our database"""

import unittest

from src.db.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = Database()

    def test_singleton(self):
        # Arrange
        conn2 = Database()

        ## Assert
        self.assertEqual(self.conn, conn2)

    def test_postgres_version(self):
        # Arrange
        pg_version = "PostgreSQL 14.13"

        # Act
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()[0]  # ('.....',)

            # Assert
            self.assertTrue(db_version.startswith(pg_version))
