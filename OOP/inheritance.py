# class Animal:
#   def __init__(self , name):
#     self.animal_name = name
#   def speak(self):
#     return f"{self.animal_name} makes a sound"
  
# class Dog(Animal):
#   def speak(self):
#     return f"{self.animal_name} makes woof sound"
  
# sound = Dog("Jimmy")
# print(sound.speak())


# class Vehicle:
#   def __init__(self , brand , year):
#      self.car_type = brand
#      self.mod_year = year
#   def info(self):
#     return f'{self.car_type} was manufactured in the year {self.mod_year}'
  
# class Car(Vehicle):
#   def __init__(self , model , brand , year):
#     super().__init__(brand , year)
#     self.car_model = model
#   def info(self):
#     return f"{self.car_type} model {self.car_model} was manufactured in the year {self.mod_year}"
  

# car_details = Car("RR321" , "Rolls Royce" , "2035")
# print(car_details.info())



# class Person:
#   def __init__(self , name , age):
#     self.person_name = name
#     self.person_age = age
#   def introduce(self):
#     pass
  
# class Student(Person):
#   def __init__(self , ID , name , age):
#     super().__init__(name , age)
#     self.student_ID = ID
#   def school_intro(self):
#     return f"{self.person_name} is my name and i am {self.person_age} years old. My student ID is {self.student_ID}"
  
# Person_details = Student(name = 'Will Byers' , age = "21" , ID = "KNUST33245144") 
# print(Person_details.school_intro())
# cm²


# class Employee:
#   def __init__(self , name , salary):
#     self.emp_name = name
#     self.emp_salary = salary
#   def details(self):
#     return f"This Employee {self.emp_name} is paid ${self.emp_salary}"

# class TeamSize(Employee):
#   def __init__(self , team_size , y):
#     super().__init__(y.emp_name , y.emp_salary)
#     self.size = team_size
#   def details(self):
#     return f"This Employee {self.emp_name} is paid ${self.emp_salary} and is part of the team with size {self.size} "

# employee = Employee(name = "Daniel" , salary="20000")
# employee_details = TeamSize( y = employee ,team_size = 32)
# print(employee_details.details())
# print(employee.details())


# # class Volume:
#   def __init__(self , radius , height):
#     self.cyl_vol = 3.145 * radius ** 2 * height
#   def x(self):
#     return f"Original answer = {self.cyl_vol}"
    
# class Result(Volume):
#   def __init__(self , p , t ):
#     super().__init__(p , t )
#     self.q = t
#   def y(self):
#     self.modified = self.cyl_vol + self.q
#     return f"modified answer = {self.modified}"
  
# vol_ans = Volume(2 , 3)
# mod_ans = Result(4 , 4)

# print(vol_ans.x())
# print(mod_ans.y())

  
  
  
  
  
  