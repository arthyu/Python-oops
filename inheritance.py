#class car:
 #   def _brand(self):
        #print("OYOTA")
  #  @staticmethod
   # def start():
        #print("car started")
    #@staticmethod
    #def stop():
        #print("car stopped")
    
#class toyota(car):
 #   def brand(self,model):
  #      print("4x4")
   #     super().brand()
       

#f1 = toyota("corolla")

#f1.brand
#print(f1.brand)







class complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumbers(self):
        print(self.real,'i +',self.img,"j")
    
    def __add__(self,num2):
        realPart = self.real + num2.real
        imagePart = self.img +num2.img
        return complex(realPart,imagePart)

    def __sub__(self,num2):
        realPart = self.real - num2.real
        imagePart = self.img -num2.img
        return complex(realPart,imagePart)    

c1 = complex(2,3)
c1.showNumbers()

c2 = complex(3,2)
c2.showNumbers()

c3 = c1 - c2
c3.showNumbers()