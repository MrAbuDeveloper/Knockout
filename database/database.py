import psycopg2
from data.config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database=DB_NAME,
            host=DB_HOST,
            password=DB_PASSWORD,
            user=DB_USER
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_users_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY,
            name VARCHAR(20),
            lastname VARCHAR(20),
            contact VARCHAR(15),
            birthdate DATE
        )'''
        self.manager(sql, commit=True)

    def insert_user_id_to_users(self, telegram_id):
        sql = '''INSERT INTO users(telegram_id)
        VALUES(%s)
        ON CONFLICT DO NOTHING'''
        self.manager(sql, (telegram_id, ), commit=True)

    def check_user_info(self, telegram_id):
        sql = '''SELECT name, lastname, contact, birthdate FROM users
        WHERE telegram_id = %s'''
        return self.manager(sql, telegram_id, fetchone=True)
    