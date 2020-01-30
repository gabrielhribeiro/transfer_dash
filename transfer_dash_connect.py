import yaml
import pymysql
import pymssql

# tool to help connection between databases.

class ConnectionsDB:
    def __init__(self):
        self.conf_path = 'config.yaml'
        self.conf_get()
        ConnectionsDB.connect_mysql = ''
        ConnectionsDB.connect_sql = ''
        self.dataMap = []
        self.sec = []


    def conf_get(self):
        with open(self.conf_path, 'r') as self.dataMap:
            try:
                self.sec = yaml.safe_load(self.dataMap)
            except yaml.YAMLError as exc:
                print(exc)
        return self.sec

    def Mysql_Connection(self):
        try:
            self.connect_mysql = pymysql.connect(
                                        host=self.conf_get()['databases_configs']['mysql']['connection']['host'],
                                        user=self.conf_get()['databases_configs']['mysql']['connection']['user'],
                                        password=self.conf_get()['databases_configs']['mysql']['connection']['passwd'],
                                        db=self.conf_get()['databases_configs']['mysql']['connection']['db'],
                                        port=self.conf_get()['databases_configs']['mysql']['connection']['port'])
            return self.connect_mysql.cursor(), self.connect_mysql
        except:
            print("Problem to connect MYSQL")
            return False

    def Sql_Connection(self):
        try:
            self.connect_sql = pymssql.connect(host=self.conf_get()['databases_configs']['ssql']['connection']['host'],
                                      user=self.conf_get()['databases_configs']['ssql']['connection']['user'],
                                      password=self.conf_get()['databases_configs']['ssql']['connection']['passwd'],
                                      database=self.conf_get()['databases_configs']['ssql']['connection']['db'],
                                      port=self.conf_get()['databases_configs']['ssql']['connection']['port'],
                                      as_dict=self.conf_get()['databases_configs']['ssql']['connection']['as_dict'],
                                      login_timeout=self.conf_get()['databases_configs']['ssql']['connection'][
                                          'login_timeout'])
            return self.connect_sql.cursor(as_dict=False), self.connect_sql
        except:
            print("Problem to connect SQL")
            return False

if __name__ == '__main__':
    ConnectionsDB().Sql_Connection()
    ConnectionsDB().Mysql_Connection()