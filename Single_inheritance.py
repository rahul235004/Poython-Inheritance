                                                      #single inheritance
class Man:
    def __init__(self,no_of_legs):
        self.name="rahul"             #instance variable
        self.no_of_legs=no_of_legs   #instance variable
    def eat(self):
        print("Eating food")
    def sleep(self):
        print("Sleeping in man")
        print(self.no_of_legs)

class Child(Man):
    def __init__(self,name,no_of_hands):
        super().__init__(no_of_hands) ##super() is used to call the parent class constructor
        self.no_of_eyes=2
    def sleep(self):
        super().sleep()    #super() is used to call the parent class method
           #overriding
        print("Sleeping like a child")
child_1=Child("rahul",54)
child_1.sleep()
print(child_1.no_of_eyes)
