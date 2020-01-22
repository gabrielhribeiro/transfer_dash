import yaml
import mysql.connector
import pymssql

# tool to help connection between databases.

class ConnectionsDB:
    def __init__(self):
        self.conf_path = 'config.yaml'
        self.conf_get()
        self.dataMap = []
        self.sec = []
        self.Mysql_Connection()
        self.Sql_Connection()

    def conf_get(self):
        with open(self.conf_path, 'r') as self.dataMap:
            try:
                self.sec = yaml.safe_load(self.dataMap)
            except yaml.YAMLError as exc:
                print(exc)
        return self.sec

    def Mysql_Connection(self):
        mysql.connector.connect(host=self.conf_get()['databases_configs']['mysql']['connection']['host'],
                                user=self.conf_get()['databases_configs']['mysql']['connection']['user'],
                                password=self.conf_get()['databases_configs']['mysql']['connection']['passwd'],
                                database=self.conf_get()['databases_configs']['mysql']['connection']['db'],
                                port=self.conf_get()['databases_configs']['mysql']['connection']['port'])

    def Sql_Connection(self):
        pymssql.connect(host=self.conf_get()['databases_configs']['ssql']['connection']['host'],
                        user=self.conf_get()['databases_configs']['ssql']['connection']['user'],
                        password=self.conf_get()['databases_configs']['ssql']['connection']['passwd'],
                        database=self.conf_get()['databases_configs']['ssql']['connection']['db'],
                        port=self.conf_get()['databases_configs']['ssql']['connection']['port'],
                        as_dict=self.conf_get()['databases_configs']['ssql']['connection']['as_dict'],
                        login_timeout=self.conf_get()['databases_configs']['ssql']['connection']['login_timeout'])

if __name__ == '__main__':
    ConnectionsDB()