#!/usr/bin/python
import os
import time
import psycopg2

print(os.environ['HOME'])
#from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    while True:
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(
                host="db",
                database=os.environ['POSTGRES_DB'],
                user=os.environ['POSTGRES_USER'],
                password=os.environ['POSTGRES_PASSWORD'])
            
            # create a cursor
            cur = conn.cursor()
            
        # execute a statement
            print('PostgreSQL table list:')
#            cur.execute('SELECT version()')
            cur.execute('SELECT table_name FROM information_schema.tables  where table_schema=\'public\' ;')

            # display the PostgreSQL database server version
            tbl_list = cur.fetchone()
            print(tbl_list)
        
        # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        else:
            print('db up')

            if tbl_list is None:
                print('Migrate PostgreSQL database...')
                os.system("/home/deploer/.local/bin/flask db upgrade")
            exec(open("./app.py").read())
#            sys.execfile("app.py", global_vars, local_vars) cur.execute('SELECT version()')
            break
            
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
        time.sleep(1)


if __name__ == '__main__':
    connect()
