'''
This is a test file!
'''

'''
class user():

    planet = "earth"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def future_age(self,years):
        return self.age+years

    def __str__(self):
        return f"User is {self.name} - Age is {self.age} - Lives on {self.planet}"

user1 = user("Zaid",30)
print(user1)

future_years = 7
user_future_age = user1.future_age(future_years)
print(f"{user1.name} will be {user_future_age} in {future_years}")
'''


import db_module

db = db_module.DbClass()
mydb = db.connect_db()
results = db.query_db(mydb,"select","select id, order_id from transactional_sms limit 5")
print(results)

'''
f = open("test-file.txt","r")
content = f.read()
#f.write("okok")
print(content)
'''
