class Account:
    def __init__(self,balance,acc):
        self.balance = balance
        self.account_no = acc

    def debit(self,amount):
        if amount > self.get_bal():
            print("only rs", self.balance,"rs",amount , "isnt present in account")
        else:
         self.balance -= amount
         print("rs",amount,"debited")
         print("total balance", self.balance)    

    def credit(self,amount):
        self.balance += amount
        print("rs",amount,"credited")    
        print("total balance", self.get_bal())

    def get_bal(self):
        return self.balance

a1 = Account(10000,123)
a1.credit(5000)
a1.debit(30)
