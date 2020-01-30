import transfer_dash_connect
import schedule
import time

class select_insert:
    def __init__(self):
        self.cursor_sql,   self.con_sql = transfer_dash_connect.ConnectionsDB().Sql_Connection()
        self.cursor_mysql, self.con_mysql = transfer_dash_connect.ConnectionsDB().Mysql_Connection()
        self.insert_mysql_query_1()

    def select_sql_query_1(self):
        try:
            self.cursor_sql.execute(transfer_dash_connect.ConnectionsDB().conf_get()['databases_configs']['ssql']
                           ['queries']['query_1'])
            return self.cursor_sql.fetchall()
        except:
            print("Problem to query sql_1")
            return False

    def insert_mysql_query_1(self):
        try:
            self.cursor_mysql.executemany(transfer_dash_connect.ConnectionsDB().conf_get()['databases_configs']['mysql']
                           ['queries']['query_1'], (select_insert().select_sql_query_1()))
            print("insert")
            return self.con_mysql.commit()
        except:
            print("Problem to query Mysql_1")
            return False


if __name__ == '__main__':
    x = select_insert()
    y = x.insert_mysql_query_1()
    schedule.every(10).seconds.do(y)

    while True:
        schedule.run_pending()
        time.sleep(1)
