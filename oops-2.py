

class Calculator:
    def add(self, *args):
        return sum(args)
    
    def mul(self,*args):
        result = 1
        for n in args:    
            result *= n
        return result
calc = Calculator()
print(calc.add(2,4,3))

print(calc.mul(2,4,3))

