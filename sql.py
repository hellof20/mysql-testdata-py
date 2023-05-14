import pymysql
import os
from loguru import logger
import sys

class Database:
    """Database connection class."""
    def __init__(self):
        self.host = os.environ.get('host')
        self.username = os.environ.get('user')
        self.password = os.environ.get('password')
        self.port = 3306
        self.dbname = os.environ.get('db')
        self.conn = None

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(
                    host=self.host,
                    user=self.username,
                    passwd=self.password,
                    db=self.dbname,
                    connect_timeout=5,
                    charset='utf8mb4'
                )
        except pymysql.MySQLError as e:
            logger.error(e)
            sys.exit()
        finally:
            logger.info('Connection opened successfully.')

    def run_query(self, query):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                if 'select' in query:
                    records = []
                    cur.execute(query)
                    result = cur.fetchall()
                    for row in result:
                        records.append(row)
                    cur.close()
                    return records
                result = cur.execute(query)
                self.conn.commit()
                affected = f"{cur.rowcount} rows affected."
                cur.close()
                return affected
        except pymysql.MySQLError as e:
            logger(e)
            sys.exit()
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logger.info('Database connection closed.')
