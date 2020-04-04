import db_module

db = db_module.DbClass()
mydb = db.connect_db()
results = db.query_db(mydb,"select","select id, order_id from transactional_sms limit 5")

if results:
    print(results)
    for result in results:
        print(result['id'])
        print(result['order_id'])
