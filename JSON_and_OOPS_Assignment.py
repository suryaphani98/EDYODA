# Assignment 1

import json
f =  open("employee.json")
data = json.load(f)

for i in data["employee"]:
    print(i)
f.close()


# Assignment 1.2

import json
d = {"state_captials":[{"State": "Kerala", "Captials": "Thiruvananthapuram"},
               {"State": "Madhya Pradesh", "Captials": "Bhopal"},
               {"State": "Haryana ", "Captials": "Chandigarh"},
               {"State":"Himachal Pradesh","Captials":"Shimla"},
               {"State":"Jharkhand","Captials":"Ranchi"},
               {"State":"Karnataka","Captials":"Bangalore"},
               {"State":"Maharashtra","Captials":"Mumbai"}]} 
with open("dictionarys.json", "w") as f:
   json.dump(d, f, indent = 4)
   
 
# Assignment 2

class Dog:
    def __init__(self,name,age,coat_colour):
        self.name = name
        self.age = age
        self.coat_colour = coat_colour

    def description(self):
        print(self.name,self.age)

    def get_info(self):
        print(self.coat_colour)


class JackRussellTerrier(Dog):
    def bark(self):
        print("bow! bow!")

    def snore(self):
        print("Zeeeeeee.....")


class Bulldog(Dog):
    def bark(self):
        print("boowwww!")

    def snore(self):
        print("Zzzzzzzz...")


dog1 = Dog("Puppy", 4, "Brown")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Brownie",6,"Black")
dog2.bark()

dog3 = Bulldog("buddy",9,"white")
dog3.snore()