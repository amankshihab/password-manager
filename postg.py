import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
U_NAME = os.getenv('U_NAME')
P_WORD = os.getenv('P_WORD')
debug = True


def connect():

    result = False

    try:
        conn = psycopg2.connect(database=U_NAME, user=U_NAME,
                                password=P_WORD, host=DATABASE_URL, port="5432")
        result = True
    except Exception as e:
        print(e)
        result = False

    return conn, conn.cursor(), result


def fetchLogin(username):

    _, cur, result = connect()

    if result:
        cur.execute(f"SELECT * FROM usertable WHERE name='{username}';")

        to_return = cur.fetchone()
        # cur.close()

        return to_return

    else:
        return None


def fetchPassword(userid):

    _, cur, result = connect()

    if result:
        cur.execute(f'SELECT * FROM passtable WHERE id=\'{userid}\';')

        return cur.fetchall()
    else:
        return None


def makeUser(username, password):

    conn, cur, result = connect()

    print(
        f'INSERT INTO usertable(name, pass) VALUES (\'{username}\', \'{password}\');')

    if result:
        cur.execute(
            f'INSERT INTO usertable(name, pass) VALUES (\'{username}\', \'{password}\');')
        conn.commit()
    else:
        print("asdasd")
