# def info ():
#    print("hello")
# info()
# info()
# info()   

# def greet (name ):
#     print(f"hello{name}")
# greet("nishu")
# greet("isha")    


# def info(name,city,age):
#     print(f"hello{name} , from {city},your're {age} years oid")
# info("name " , "city")


# def studentInfo(name,marks, college="SSGT"):
#     print(f"hello{name}, you're{marks}, you're from{college}")
# studentInfo("name" , 200, "MIT")
# studentInfo("name" , 300)

            
# def sum(a , b ):
#     return a + b
# res = sum (4,5)
# print(res) 
            
# def info():
#    return "nishu", 17           
# name,age = info () 
# print(name, age)
# res = lambda a,b: a+b
# print(res(4,6))
# x=20
# def abc(): 
#  print(x)  
# abc()      

# def factorial(n):
#     if n== 0 or n==1:
#       return 1
#     return n * factorial(n-1)   
           

# def sum (a, b):
#     return a + b

# def mul (a , b):
#     return a * b

# def sub (a , b):
#     return a - b

# def div (a , b):
#     return a / b

# def calc (fn, a, b):
#     return fn(a, b)

# print (calc(sum, 5, 3))
# print (calc(mul, 5, 8))
# print (calc (div, 6, ))

# def rec_sum(n):
#     if n == 0:
#         return 0
#     return (n % 10) + rec_sum(n // 10)
# print(rec_sum())

# number = [1, 2, 3, 4, 5]
# fruits = ["apple", "banana"]
# mixed = [10, "hello", 3.14]
# print(number)
# print(mixed)
# print(fruits)
# print(number[1])
# fruits[1] = "mango"
# print(fruits[1])

# from functools import reduce 
# nums = [1, 2, 3, 4, 5]
# res = reduce (lambda x, y: x / y, nums)
# print(res) 

# nums =(1, 2, 3, 4, 5,)
# print (nums)
# print (nums[1])
# print (nums [-1])
# print (nums[1:4])
# nums = (1, 2)
# a,b = nums 
# print (a,b)       

nums =( 1, 2, 3, 4, 5, )
res =[]
for n in nums :
    res. append (n*n)
print (res)

# nums = (1, 2, )
# nums [1] = 20 
# print (nums)