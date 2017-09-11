import sqlite3
import pandas as pd

class sqlite:
    def __init__(self, Database, Table, Column):
        self.conn = sqlite3.connect(Database)
        self.cur = self.conn.cursor()
        self.table = Table
        self.column = Column

    def create_table(self,Table,Column):
        sql = """create table %s %s;"""%(self.table, self.column)
        self.cur.execute(sql)
        self.conn.commit()

    def insert(self,Table,Column,Values):
        sql = """insert into %s %s values %s;"""%(self.table, self.column, Values)
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.conn.close()

    def table4df(self):
        df = pd.io.sql.read_sql_query("select * from {table}".format(table=self.table), self.conn)
        return df