class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def checkName(self):
        print(f"Your name is {self.name}")
    

studnet = Student("Mikasa", 17)
studnet.checkName()
        