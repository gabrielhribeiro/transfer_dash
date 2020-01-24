import transfer_dash_connect


class select_insert:
    def __init__(self):
        self.get_connection_db()
        self.select_sql_query_1()
        self.insert_mysql_query_1()
        self.cursor_sql = None
        self.cursor_mysql = None

    def get_connection_db(self):
        self.cursor_sql = transfer_dash_connect.ConnectionsDB.Sql_Connection()
        self.cursor_mysql = transfer_dash_connect.ConnectionsDB.Mysql_Connection()
        return self.cursor_sql, self.cursor_mysql

    def select_sql_query_1(self):
        cursor_sql = self.cursor_sql
        cursor_sql.executemany(transfer_dash_connect.ConnectionsDB.conf_get()['databases_configs']['ssql']
                               ['queries']['query_1'])
        return cursor_sql.fetchall()

    def insert_mysql_query_1(self):
        cursor_mysql = self.cursor_mysql
        cursor_mysql.executemany("INSERT INTO TABLE (VALUE1, VALUE2) VALUES (%s,%s)", (self.select_sql_query_1()))
        return cursor_mysql.commit()


if __name__ == '__main__':
    select_insert()
