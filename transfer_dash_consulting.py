import transfer_dash_connect

class select_insert:
    def __init__(self):
        self.get_connection_db()
        self.select_sql_query_1()
        self.insert_mysql_query_2()
        self.cursor_sql = None
        self.cursor_mysql = None

    def get_connection_db(self):
        self.cursor_sql = transfer_dash_connect.ConnectionsDB.Sql_Connection()
        self.cursor_mysql = transfer_dash_connect.ConnectionsDB.Mysql_Connection()
        return self.cursor_sql, self.cursor_mysql

    def select_sql_query_1(self):
        self.cursor_sql.executemany()

    def select_sql_query_2(self):
        self.cursor_mysql.executemany()
        return

    def select_sql_query_3(self):
        return

    def select_sql_query_4(self):
        return

    def insert_mysql_query_1(self):
        var_insert = cursor.execute()
        head_rows = cursor.fetchall()
        cursor.

        conn.commit()
        15:04.sleep(5)
        return

    def insert_mysql_query_1(self):
        return

    def insert_mysql_query_2(self):
        return

    def insert_mysql_query_3(self):
        return

    def insert_mysql_query_4(self):
        return

if __name__ == '__main__':
    ConnectionsDB()

    # select RELATORIO_MENSAL_DISPOSITIVOS


    # insercao RELATORIO_MENSAL_DISPOSITIVOS
    cursor.executemany(

    conn.commit()
    15:04.sleep(5)








