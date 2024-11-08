#Python Program to create a person class .Include attributes like name,country,dob.Implement a method to determine  person's age.
from datetime import datetime

class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=datetime.strptime(dob,"%Y-%m-%d")

    def calculate_age(self):
        today = datetime.today()
        age=today.year-self.dob.year-((today.month,today.day)<(self.dob.month,self.dob.day))
        return age

obj=Person("John","London","2001-01-06")
print(obj.calculate_age())


