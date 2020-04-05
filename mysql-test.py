import db_module

db = db_module.DbClass()
mydb = db.connect_db()

try:
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT id, order_id FROM transactional_sms LIMIT %(limit_min)s, %(limit_max)s;"
    query_parameters = {
        "limit_min": 0,
        "limit_max": 5
    }
    mycursor.execute(query,query_parameters)
except Exception as e:
    print(f"Query not processed: {e}")
else:
    myresults = mycursor.fetchall()
    print(myresults)
