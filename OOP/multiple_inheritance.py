# class A:
#   def greet(self):
#     return "hello"
  
# class B:
#   def say_bye(self):
#     return "See you later!"
  
# class C(A,B):
#   pass

# greetings = C()
# print(greetings.greet())
# print(greetings.say_bye())



# class X:
#   def __init__(self , A=80):
#     self.a=A
  
# class Y:
#   def __init__(self , B=20):
#     self.b=B

# class Z(X,Y):
#   def summation(self):
#     Y.__init__(self, B=20)
#     return f"{self.a + self.b}"
  
# sum_obj = Z()
# print(sum_obj.summation())

# class Engine:
#   def __init__(self ,size , **kwargs):
#     super().__init__(**kwargs)
#     self.car_size = size

# class Wheels:
#   def __init__(self ,model , **kwargs):
#     super().__init__(**kwargs)
#     self.car_model = model
    
# class Cars(Engine,Wheels):
#   def __init__(self , sizes , models ,power):
#     super().__init__(size = sizes , model = models)
#     self.hp=power
#   def X(self):
#     return f"{self.car_model} is off size {self.car_size}m and power of {self.hp}horse power"

# car = Cars(sizes = 300 , power = 30000 , models = "RR321")
# print(car.X())  

# the attributes in the Cars class are given the values of
# the attibutes in the parent classes due to the mro 
# so size = sizes gives sizes a value for the child class to use

# Engine only accepts one parameter size, but if the code runs, model and
# power also send their values so python raises an error 
# the kwargs prepares the Engine class for more Atrributes than it has
  