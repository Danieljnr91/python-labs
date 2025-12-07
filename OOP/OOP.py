# class Car:
#   def __init__(self , brand , model , year):
#     self.car_brand = brand
#     self.car_model = model
#     self.car_year = year
    
# car_details = Car("ROLLS ROYCE" , "RR321" , "2035")
    
# print(car_details.car_brand)
# print(car_details.car_model)
# print(car_details.car_year)


# class Food:
# def __init__(self , water_content , salt_content , sugar_content):
#     self.water_level = water_content
#     self.salt_level = salt_content
#     self.sugar_level = sugar_content
    
# food_stats = Food("45%" , "40%" , "15%")
# print(f"water content is about {food_stats.water_level}")
# print(f"salt content is about {food_stats.salt_level}")
# print(f"Sugar content is about {food_stats.sugar_level}")
  
  
# class Student:
#   def __init__(self , name , age):
#     self.student_name = name 
#     self.student_age = age
    
# student_details = Student("Lartey Daniel" , "18")

# print(f"My name is {student_details.student_name} , but you can call me Lad, i am {student_details.student_age} years. Great to meet you all!")



# class BankAccount:
#   def __init__(self , owner , acct_balance):
#     self.owners_name = owner
#     self.amt_in_acct = acct_balance
#   def deposit(self , amt_deposit):
#     self.amt_in_acct += amt_deposit
#     return f"${amt_deposit} has been added to your account, remaining balance is ${self.amt_in_acct}"
#   def withdraw(self , amt_withdrawn):
#     if amt_withdrawn > self.amt_in_acct:
#       print("Insufficient Balance!")
#     else:
#        self.amt_in_acct -= amt_withdrawn
#        return f"${amt_withdrawn} has been taken from your account, remaining balance is ${self.amt_in_acct}"
     
     
# owners_name = input("Enter name of Account:")
# cash_in_acct = int(input("Enter Your Account Balance:"))     
# owners_details = BankAccount(owners_name , cash_in_acct)

# print("Press... \n 1. to deposit \n 2. to withdraw \n 3. to check balance")
# operation = int(input("What do u wish to do?"))
# if operation ==  1:
#   depo_amt = int(input("How much are you depositing?:"))
#   print(owners_details.deposit(depo_amt))
# elif operation == 2:
#   withdraw_amt = int(input("How much are you taking?:"))
#   print(owners_details.withdraw(withdraw_amt))
   
      
          

#  class Computations:
#   def __init__(self , radius):
#      self.rad = radius
#    def circle_area(self):
#        area = 3.145 * self.rad ** 2
#     return f"Area of the circle = {area} sq.units"
#   def circ_circumfernce(self):  
#     circumference = 3.145 * 2 * self.rad
#     return f"Cicumference of the circle = {circumference}sq.units"

  
# circ_rad = float(input("Whats the radius of your circle?:"))
# cicle_details = Computations(circ_rad)

# print(cicle_details.circle_area())
# print(cicle_details.circ_circumfernce())




# class TemperatureConverter:
#   def __init__(self , celcius):
#     self.celcius_temp = celcius
#   def Kelvin(self):
#     kev_temp = self.celcius_temp + 273.15
#     return f"{self.celcius_temp}°C= {round(kev_temp , 2)}K"
#   def Farenheit(self):
#     far_temp = self.celcius_temp * 9/5 + 32
#     return f"{self.celcius_temp}°C = {round(far_temp , 2)}°F"
  

# temp_in_celcius = int(input("Enter temperature in °C:")) 
# calc_details = TemperatureConverter(temp_in_celcius)
    
# print(calc_details.Kelvin())
# print(calc_details.Farenheit())    
  
  
  
x = ['j' , 'k' , 'l' , 'm' ,'n']

y = ['m' , 'n']

p = [i for i in x if i not in y ]
  
  
print(x)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
