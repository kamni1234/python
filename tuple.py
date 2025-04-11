# list = [1, 2, 3, 4, ]
# tup =(1, 2, 3, )
# dis = {"key": "value"}
# stu = {"name": "kamni" , "age": 17}

# print (stu["name"])
# print(stu.get("age"))
# # print(stu.get("xyz", "404")) 
# stu ["age "]=24 
# print (stu)
# # del stu ["age"]
# print (stu)

# print (stu. keys())
# print (stu.values())
# print (stu.items())
# for k, v in stu.items ():
#     print (k, v)

# nums = [1, 2, 3, 4, 5, 90]
# even_sum = sum (num for num in nums if num%2==0)
# print ("sum of even numbers :",even_sum)

class bank:
    def __init__(self , name  , account , balance=0):
        self. name = name 
        self.account = account
        self.balance = balance

    def getinfo(self):
        print(f"name: {self.name}, account:{self.account}, balance: {self.balance}")

    def deposite(self,amount):
        print("amount deposite", amount)

    def withdraw(self,amount):
        self.balance>=amount
        self.balance = self.balance - amount
        print("your withdraw", amount)

c1= bank("nishu", 123456789) 
c2= bank("kamni", 987654321)

c1.getinfo()
c2.getinfo()
c1.deposite(2000)
c1.withdraw(1000)
  

