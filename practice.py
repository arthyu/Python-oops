class Student:
    def __init__(self,name,marks):
        self.name =name
        self.marks =marks 

    def average_mark(self):
        sum = 0
        for n in self.marks:
            sum += n
        return sum/3

s1 = Student("rahul",[99,98,97])
print(s1.average_mark())

        