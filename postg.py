import psycopg2
import os
from dotenv import load_dotenv
import time


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
U_NAME = os.getenv('U_NAME')
P_WORD = os.getenv('P_WORD')
debug = True


def fetcher(conn, cur, cmd="SELECT * FROM usertable;", cond='one'):
    try:
        # SELECT cmd here
        cur.execute(cmd)
        print('--success',cur.rowcount)
        if cond == 'one':
            data = cur.fetchone()
        else:
            data = cur.fetchall()
        return data

        # for row in data:
        #     print(row)
        #     print("Id = ", row[0], )
        #     print("name = ", row[1])
        #     print("pass  = ", row[2], "\n")
        
        # l = [x for x in data]
        # print(l)

    except Exception as e:
        print('--error')
        return None


def pg(cmd="SELECT * FROM usertable;",cond='one'):
    if debug:
        # while True:
        print("connecting to DB")
        conn = psycopg2.connect(DATABASE_URL, user=U_NAME, password=P_WORD)
        cur = conn.cursor()
        print("Loading function")
        data = fetcher(conn, cur, cmd, cond)
        print("Closing DB")
        cur.close()
        conn.close()
        print("pg exit")
        
    return data
