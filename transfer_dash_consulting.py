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
        self.get_connection_db.executemany(),

        return

    def select_sql_query_2(self):
        return

    def select_sql_query_3(self):
        return

    def select_sql_query_4(self):
        return

    def insert_mysql_query_1(self):
        var_insert = cursor.execute()
        head_rows = cursor.fetchall()
        cursor2.

        conn.commit()
        time.sleep(5)
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
    cursor2.executemany(

    conn.commit()
    time.sleep(5)









print
"Conectando ao banco..."

connection = pymssql.connect(host='10.219.192.20:1433', user='SSCRSP01', password='jQrVFmuc5', timeout=120,
                             login_timeout=120, database='GBWCD3')

conn = pymysql.connect(user='root', password='root', host='10.208.41.86:8080', database='relatorio_mensal')

# prepare a cursor object using cursor() method






cursor = connection.cursor()
print
"Pronto!"


print
head_rows

print
"Insercao mysql"

cursor2.executemany(
    """INSERT INTO RELATORIO_MENSAL_DISPOSITIVOS (FD_RECEPTION_DATE, TIPO, QTD ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
    (head_rows))

conn.commit()

print
"Insercao mysql"

connection.close()