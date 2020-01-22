import yaml
import mysql.connector
import pymssql


#tool to help connection between databases.

class ConnectionsDB:
    def __init__(self):
        self.conf_path = 'config.yaml'
        self.conf_get()
        self.dataMap = []
        self.sec = []
        self.conf_print()
        self.Mysql_Connection()
        self.Sql_Connection()

    def conf_get(self):
        with open(self.conf_path, 'r') as self.dataMap:
            try:
                self.sec = yaml.safe_load(self.dataMap)
            except yaml.YAMLError as exc:
                print(exc)
        return self.sec

    def conf_print(self):
        return print(self.conf_get()['mysql']['host'])

    def Mysql_Connection(self):
        mysql.connector.connect(host=self.conf_get()['mysql']['host'], user=self.conf_get()['mysql']['user'],
                                password=self.conf_get()['mysql']['passwd'], database=self.conf_get()['mysql']['db'],
                                port=self.conf_get()['mysql']['port'])

    def Sql_Connection(self):
        pymssql.connect(host=self.conf_get()['ssql']['host'], user=self.conf_get()['ssql']['user'],
                        password=self.conf_get()['ssql']['passwd'], database=self.conf_get()['ssql']['db'],
                        port=self.conf_get()['ssql']['port'], as_dict=self.conf_get()['ssql']['as_dict'],
                        login_timeout=self.conf_get()['ssql']['login_timeout'])

if __name__ == '__main__':
    ConnectionsDB()