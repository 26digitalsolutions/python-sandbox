import mysql.connector

class DbClass():

    '''
    Connect, Select from, Insert into, Update and Delete from the mysql database
    '''

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

    ''' query the db (select, update, insert, delete) '''
    def query_db(self,mydb,query_type,query):
        try:
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(query)
        except Exception as e:
            print(e)
        else:
            if query_type == "select":
                myresults = mycursor.fetchall()
                return myresults
            elif query_type == "update" or query_type == "delete" or query_type == "insert":
                return f"Rows affected: {mycursor.rowcount}"

    ''' close the db '''
    def close_db(self,mydb):
        mydb.close()
