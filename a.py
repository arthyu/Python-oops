class Student:

    college = "lotus"
   
    def __init__(self,fullname,age):
        self.name = fullname
        self.age = age
    def welcome(self):
        print("welcome ",  self.name )
    def get_age(self):
        return self.age 

s1= Student("ajju",1)
#print(s1.name,s1.age)

#s2 = Student("dojo",s2)
#print(s2.name)
#print(s2.age)
#print(s2.college)
s1.welcome()
print(s1.get_age())