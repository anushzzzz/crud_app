from sqlalchemy import create_engine, text

from urllib.parse import quote_plus

import pandas as pd


class MySQLInstance:
    def __init__(self):
        username='root'
        password='anusha'
        database='python_db'
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@localhost:3306/python_db')

    def get_engine(self):
        return self.engine
    


def insert_data(c_name, c_desc, c_dur):
    mysql= MySQLInstance()
    engine=mysql.get_engine()
    insert_sql=text('insert into course (cname,description,duration) values(:name,:desc,:dur)')
    
    try:
        conn=engine.connect()
        result=conn.execute(insert_sql,{'name':c_name, 'desc':c_desc, 'dur':c_dur})
        print(f'insert successful!\nNo. of rows affected={result.rowcount}')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def view_data():
    mysql= MySQLInstance()
    engine=mysql.get_engine()
    select_sql='select * from course'
    
    try:
        conn = engine.connect()
        data = pd.read_sql(select_sql,conn)

        print(data)
        conn.close()
    except Exception as e:
        print(e)

# to get by course id

def get_by_cid(c_id):
    mysql= MySQLInstance()
    engine=mysql.get_engine()
    get_sql=f'select * from course where id={c_id}'
    
    try:
        conn = engine.connect()
        data = pd.read_sql(get_sql,conn)

        if (data.empty):
            print(f'Course with id= {c_id} not found!')
            return False
        else:

            print(data)
            return True
        conn.close()
    except Exception as e:
        print(e)

def update_data(cid, c_name, c_desc, c_dur ):
    mysql=MySQLInstance()
    engine=mysql.get_engine()

    
    update_sql=text("update course set cname=:name, description=:desc, duration=:dur where id=:c")

    try:
        conn=engine.connect()
        result=conn.execute(update_sql, {'name':c_name,'desc':c_desc,'dur':c_dur,'c':cid})
        print(f'update successfull and num of rows affected are {result.rowcount}')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def delete_data(cid ):
    mysql=MySQLInstance()
    engine=mysql.get_engine()

    
    delete_sql=text("delete from course where id=:c")

    try:
        conn=engine.connect()
        result=conn.execute(delete_sql, {'c':cid})
        print(f'delete successfull and num of rows affected are {result.rowcount}')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

                         


