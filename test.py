'''
This is a test file!
'''

class user():

    planet = "earth"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User is {self.name} - Age is {self.age} - Lives on {self.planet}"

user1 = user("Zaid",30)
print(user1)
