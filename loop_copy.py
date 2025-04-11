# for i in range (5,20,2):
#     print (i)

# i=0
# while True:
#     i+=1
#     if (i == 3):
#      continue
#     else:
#         print(i) 
#     if(i == 100):
#         break

while True:
      user_input= input("type something .(type quit to close)")
      if user_input.strip().lower() == "quit":    
          break
      print("you entered", user_input )    
