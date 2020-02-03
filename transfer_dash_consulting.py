import transfer_dash_connect
import schedule
import time

# class to select, insert and organize schedule between databases.
class select_insert:
    def __init__(self):
        self.ConnectionsDB = transfer_dash_connect.ConnectionsDB()
        self.registrarLog = transfer_dash_connect.ConnectionsDB.registrarLog
        try:
            self.cursor_sql,   self.con_sql = transfer_dash_connect.ConnectionsDB.Sql_Connection()
        except:
            self.registrarLog("Error to declare Cursor_sql and con_sql, please verify the connections")
        pass
        try:
            self.cursor_mysql, self.con_mysql = transfer_dash_connect.ConnectionsDB.Mysql_Connection()
        except:
            self.registrarLog("Error to declare Cursor_mysql and con_mysql, please verify the connections")
        pass
        try:
            self.conf_get = transfer_dash_connect.ConnectionsDB.conf_get()
        except:
            self.registrarLog("Error to declare variables, please verify the connections")
        pass

    #select data from sql(select_sql_query_1)
    def select_sql_query_1(self):
        try:
            self.cursor_sql.execute(self.conf_get['databases_configs']['ssql']['queries']['query_1'])
            return self.cursor_sql.fetchall()
        except:
            self.registrarLog("Problem to query SQL, please verify the connections or queries")
            return False

    #function for insert values from sql(select_sql_query_1)
    def insert_mysql_query_1(self):
        if select_insert().select_sql_query_1() != False:
            try:
                self.cursor_mysql.executemany(self.conf_get['databases_configs']['mysql']['queries']['query_1']['query'],
                                          (select_insert().select_sql_query_1()))
                self.registrarLog("insert")
                return self.con_mysql.commit()
            except:
                self.registrarLog("Problem to insert MYSQL, please verify the connections or queries")
                return False
        else:
            self.registrarLog("Problem to query from sql, please verify the queries")
            return False

if __name__ == '__main__':
    insert_class = select_insert()
    if insert_class.insert_mysql_query_1!= False:
        #schedule to insert each rule mysql_1 (insert_mysql_query_1)
        schedule.every(insert_class.conf_get['databases_configs']['mysql']['queries']['query_1']['schedule']) \
                                                .seconds.do(insert_class.insert_mysql_query_1)
        insert_class.registrarLog("schedule for 60sec")
    else:
        insert_class.registrarLog("Error to schedule")
        pass

    while True:
        schedule.run_pending()
        time.sleep(1)
        continue