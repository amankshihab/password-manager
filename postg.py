import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
U_NAME = os.getenv('U_NAME')
P_WORD = os.getenv('P_WORD')
debug = True


def fetcher(conn, cur, cmd="SELECT * FROM usertable;", cond='one'):
    try:
  
        if cmd[0] == 'I':   # INSERT cmd here
            cur.execute(cmd)
            conn.commit()
            return "Inserted"
        else:               # SELECT cmd here
            cur.execute(cmd)
            print('--success',cur.rowcount)
            if cond == 'one':
                data = cur.fetchone()
            else:
                data = cur.fetchall()
            return data

    except Exception as e:
        print('--error')
        return None


def pg(cmd="SELECT * FROM usertable;",cond='one'):
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

# print(pg(cmd="INSERT INTO usertable VALUES(5,'Hack','hack');"))
# print(pg(cond='all'))