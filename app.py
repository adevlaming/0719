# add your name to the print statement below
print("Hello, my name is " + "Adam")
class Person:
    def __init__ (self, personID, firstName, lastName, favoriteColor, age, isWorking):
        self.personid = personID
        self.firstname = firstName
        self.lastname = lastName
        self.favoritecolor = favoriteColor
        self.age = age
        self.isworking = isWorking
    def user(self):
        print(f"ID= {self.personid}")
        print(f"Your Name is {self.firstname} {self.lastname}")
        print(f"Your favorite color is {self.favoritecolor}")
        print(f"Your age is: {self.age}")
        print(f"Are you working? {self.isworking}")
        
    def changecolor(self):
        self.favoritecolor = print("Your actual favorite color is: White")
    def tenyearage(self):
        self.age = self.age + 10
        print(f"Your age in 10 years will be: {self.age}")

person = Person(1234, "Adam", "deVlaming", "blue", 12, "yes")
person.user()
person.changecolor()
person.tenyearage()

