import yaml
import mysql.connector

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
        cnx = mysql.connector.connect(host=self.conf_get()['mysql']['host'], user=self.conf_get()['mysql']['user'],
                                      password=self.conf_get()['mysql']['passwd'], database=self.conf_get()['mysql']['db'],
                                      port=self.conf_get()['mysql']['port'])

        return print(cnx.is_connected())

    def Sql_Connection(self):
        cnx = mysql.connector.connect(host=self.conf_get()['ssql']['host'], user=self.conf_get()['ssql']['user'],
                                      password=self.conf_get()['ssql']['passwd'], database=self.conf_get()['ssql']['db'],
                                      port=self.conf_get()['ssql']['port'])

        return print(cnx.is_connected())

if __name__ == '__main__':
    ConnectionsDB()
    teste