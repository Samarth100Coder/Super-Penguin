class Bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Penguin(Bird):
    def __init__(self,name,age):
        super().__init__(name,age)
    def nameDisplay(self):
        print(self.name)
    def ageDisplay(self):
        print(self.age)
a=Penguin('Harry',15)
a.nameDisplay()
a.ageDisplay()