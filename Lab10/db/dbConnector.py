import psycopg2
from Lab10.config.config import load_config
from Lab10.db.Phonebook import PhoneBook


class DBConnector:
    def __init__(self):
        self.config = load_config()

    def createTable(self):
        sql = '''
            CREATE SEQUENCE IF NOT EXISTS s;
            CREATE TABLE IF NOT EXISTS phone_nums (
                id INTEGER DEFAULT nextval('s') PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                phone VARCHAR(11) NOT NULL
        );
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                conn.commit()
        except Exception as e:
            print("Error on creating new table ", e)

    def add_phone(self, p1: PhoneBook):
        sql = "INSERT INTO phone_nums (first_name, last_name, phone) VALUES (%s, %s, %s)"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (p1.first_name, p1.last_name, p1.phone))
                conn.commit()
        except Exception as e:
            print("Error on inserting new user ", e)

    def update_phone_by_name(self, id, name):
        sql = '''
            UPDATE phone_nums 
            SET first_name=%s 
            WHERE id=%s 
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, id))
                conn.commit()
        except Exception as e:
            print("Error on updating new user ", e)

    def update_phone_by_phone(self, id, phone):
        sql = '''
                UPDATE phone_nums 
                SET phone=%s 
                WHERE id=%s 
                '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (phone, id))
                conn.commit()
        except Exception as e:
            print("Error on updating new user ", e)

    def delete_phone_by_id(self, id):
        sql = '''
            DELETE 
            FROM phone_nums 
            WHERE id=%s 
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (id))
                conn.commit()
        except Exception as e:
            print("Error on deleting user ", e)

    def get_all_users(self):
        sql = "SELECT * FROM phone_nums ORDER BY id ASC"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    rows = cur.fetchall()
                    return rows
        except Exception as e:
            print("Error on listing all users ", e)

    def createTableForRace(self):
        sql = '''
                    CREATE SEQUENCE IF NOT EXISTS s;
                    CREATE TABLE IF NOT EXISTS race_scores (
                        id INTEGER DEFAULT nextval('s') PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        level VARCHAR(11) NOT NULL
                );
                '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                conn.commit()
        except Exception as e:
            print("Error on creating new SCORE RACE table ", e)