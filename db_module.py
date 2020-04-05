import mysql.connector

class DbClass():

    '''
    Connect and close db mysql
    '''

    def __init__(self):
        pass

    ''' connect '''
    def connect_db(self):
        try:
            mydb = mysql.connector.connect(
              user='root',
              password='',
              host='localhost',
              database='dataprojects'
            )
        except Exception as e:
            print(e)
        else:
            return mydb

    ''' close the db '''
    def close_db(self, mydb):
        try:
            mydb.close()
        except Exception as e:
            print(e)
