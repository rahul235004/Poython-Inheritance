                                                        #mutiple inheritance



class Human:
    def __init__(self,name):
        print("Human constructor")
        self.name=name
        self.age=21
    def work(self):
        print("I can work")
    def eat(self):
        print("Eating food")
    def sleep(self):
        print("Sleeping")
class Male:
    def __init__(self):
        print("Male constructor")
        self.usn= "3BR22EE083"
    def work(self):
        print("I can code")
    
class Boy(Human,Male):
    def __init__(self,naam,branch):         #constructor overriding
        print("Boy constructor")
        Human.__init__(self,naam)
        Male.__init__(self)
        self.branch=branch
    def sleep(self):
        print("Sleeping boy")
    def work(self):                          #method overriding
        print("I can test")
    def display(self):
        print(f"i am {self.name} and i am from {self.branch} .My usn is {self.usn} and my age is {self.age}")           
        boy_1.sleep()       #method resolution
        boy_1.work()      
        Male.work(boy_1)            #method resolution
        Human.work(boy_1)
        Human.eat(boy_1)
        Human.sleep(boy_1)            

boy_1=Boy("rahul","EEE")
#Human.work(boy_1)
#ale.work(boy_1)
boy_1.display()
