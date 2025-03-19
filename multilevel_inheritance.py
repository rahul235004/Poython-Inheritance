class Human:
    def __init__(self,name,age):
        print("Human constructor")
        print(f"Name:{name} and Age:{age}") 
        self.name=name
        self.age=age    

    def eat(self):
        print("Human is eating")
    def sleep(self):        
        print("Human is sleeping")

class Male(Human):
    def __init__(self,name,age):
        print("Male consturctor")
        Human.__init__(self,name,age)


    def work(self):
        print("male can work")
    def sleep(self):
        print("i am sleeping")

class Child(Male):
    def __init__(self,name,age):
        print("Child constructor")
        super().__init__(name,age)
    def play(self):
        print("Child is playing")
    def sleep(self):
        print("Child is sleeping")
        Male.sleep(self)
        Human.sleep(self)
        super().sleep()

child_1=Child("rahul",21)
print(Child.mro())
child_1.sleep()
print(child_1.name)
print(child_1.age)
child_1.play()  
child_1.eat()