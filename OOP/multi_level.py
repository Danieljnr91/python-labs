# class Person:
#   def identify(self):
#     print("I am a person")
    
# class Parent(Person):
#   def role(self):
#     print("I am a parent")
    
# class Child(Parent):
#   def school(self):
#     print("I go to school")
    
# info = Child()
# info.identify()
# info.role()
# info.school()



class Vehicle:
  def __init__(self , max_speed):
    self.speed = max_speed
    
class Car(Vehicle):
  def __init__(self, vehicle_info , brand):
    super().__init__(vehicle_info.speed)
    self.car_brand = brand
    
class ElectricCar(Car):
  def __init__(self, car_info ,battery_capacity):
    super().__init__(Vehicle(car_info.speed) , car_info.car_brand)
    self.battery = battery_capacity
  def output(self):
    return f"{self.car_brand} has max speed of {self.speed} and battery capacity {self.battery}mH"
  
veh_details = Vehicle("300Kmh")
car_details = Car(veh_details , "RR321")
ele_details = ElectricCar(car_details , 30000)

print(ele_details.output())

# With this one, if you want to use the dot attribute, like with this, 
# if it was the single inheritance, I don't really need to call the class again. But this one, I call the vehicle class inside the car class
# because the electrical class is accessing the car class,
# there's no access in the vehicle class. So I have to call the electric car class so I can access its speed, which we don't need, so I enter.

