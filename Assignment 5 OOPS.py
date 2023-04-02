# Challenge 1: Square Numbers and Return Their Sum

class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        print("The Sum of Square Numbers :", self.x**2 + self.y**2 + self.z**2)

sum = Point(1,3,9)
sum.sqSum()



# Challenge 2: Implement a Calculator Class

class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print(self.num1+self.num2)
    def subtract(self):
        print(self.num2-self.num1)
    def multiply(self):
        print(self.num1*self.num2)
    def divide(self):
        print(self.num2/self.num1)

cal = Calculator(10,94)
cal.add()
cal.subtract()
cal.multiply()
cal.divide()




# Challenge 3: Implement the Complete Student Class

class Student:

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name 
    def setRollNumber(self,rollnumber):
        self.__rollnumber = rollnumber
    def getRollNumber(self):
        return self.__rollnumber
    
s = Student()
s.setName("surya")
print(s.getName())
s.setRollNumber(140223)
print(s.getRollNumber())




# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self,title=None,account=0):
        self.title = title
        self.account = account
    def printof(self):
        print(self.title,self.account)

class SavingsAccount(Account):
    def __init__(self,title=None,account=0,IntrestRate=0):
        super().__init__(title,account)
        self.Intrest = IntrestRate
    def printof(self):
        print(self.title,self.account,self.Intrest)
        
x = SavingsAccount("Ashish",5000,5)
x.printof()



# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def deposit(self, amount):
        self.balance =self.balance+ amount
        print("The Amount deposited into account :",amount)
    
    def withdraw(self, amount):
            self.balance =self.balance - amount
            print("The Amount withdraw from account :",amount)
            
    def get_balance(self):
        print("Current balance is :", self.balance)

C = Account("Ashish",2000)
C.deposit(500)
C.get_balance()
c1 = Account("Ashish",2000)
c1.withdraw(500)
c1.get_balance()


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        intrest = (self.interestRate*self.balance)//100
        print(intrest)

demo1 = SavingsAccount("Ashish", 2000, 5) 
demo1.interestAmount()  
