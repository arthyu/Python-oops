class Microwave:
    def __init__(self, brand: str, power_rating: str) :
        self.brand = brand
        self.power_rating =power_rating
        self.turned_on =False

    def turn_on(self):
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on')
           



    def turn_off(self):
        if self.turned_on:
              self.turned_on = False
              print(f'Microwave ({self.brand}) is now turned oFF')
        else:
           
            print(f'Microwave ({self.brand}) is already turned of')


    def run(self,seconds:int):
        if self.turned_on:
         print(f'Rnning ({self.brand}) for {seconds} seconds')
        else:
         print(f'Turn on your mcrowave first')

    def __add__(self,other):
        return f'{self.brand}+{other.brand}'

    def __mul__(self,other):
        return f'{self.brand}*{other.brand}'

    def __str__(self):
        return f'{self.brand} (rating:{self.power_rating})'


smeg:Microwave = Microwave(brand='smeg',power_rating='er')

cod:Microwave = Microwave(brand='code',power_rating= 'v')

print(smeg)