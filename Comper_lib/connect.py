import psycopg2
from Comper_lib.settings import DB, NAME, PWD, HST


def con():
    try:
        conn = psycopg2.connect(
            database=DB,
            user=NAME,
            password=PWD,
            host=HST)

    except Exception as e:
        print(e)
        exit(0)
    if conn is not None:
        print('Connected to PostgreSQL')

        cur = conn.cursor()

        cur.execute("SELECT * FROM sampledata")
        rows = cur.fetchall()

        if not len(rows):
            print("Empty")
        else:
            for row in rows:
                print(row)

        cur.close()
        conn.close()
    else:
        print('Not connected to PostgreSQL')
