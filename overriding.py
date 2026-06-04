class Animal: #---------> PARENT CLASS-
    def speak(self):
        print("anmal sound") #OVERRIDES PARENT CLASSS

class Dog(Animal):
    def speak(self):
        super().speak() #-----> first parent sound and then dog
        print("wofff")
class Cat(Animal):
    def speak(self):
        print("meow")

class cow(Animal):
    def speak(self):
        print("moo")

a = Animal()
d = Dog()
c= Cat()
cc= cow()

a.speak()
d.speak()
c.speak()
cc.speak()
