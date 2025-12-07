#FUNCTIONS
def addition(a,b):
   return a + b
def subtraction(a,b):
   return a - b
def multiply(a,b):
   return a * b
def division(a , b):
   return a / b

#DICTIONARY
operation_dict ={
   "+" : addition,
   "-" : subtraction,
   "x" : multiply,
   "/" : division
}


def reset():
   first_num = int(input("Enter first number:"))
   for i in operation_dict:
      print(i)

   end_calc = True

   while end_calc:
     operation = input("Enter operation:")
     scnd_num = int(input("Enter second number:"))
     calculator_ops = operation_dict[operation]
     result = calculator_ops(first_num , scnd_num)
     print(f"{first_num} {operation} {scnd_num} = {result} ")

   #conditions
     print("Enter 1. to continue calculation, 2. To start new calculation 3. To exit")
     user_ops = int(input("What's Next?:"))
     if user_ops == 1:
      first_num = result           
     elif user_ops == 2:
      end_calc = False
      reset()
     else:
      end_calc = False
      print("Alright, Exiting...")
      
reset()  
   

   


