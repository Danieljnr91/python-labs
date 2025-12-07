
class Shape:
  def __init__(self , length , breadth):
    self.shape_len = length
    self.shape_width = breadth
    
  
class Rectangle(Shape):
  def __init__(self , length , breadth):
    super().__init__(length , breadth)
  def area(self):
    rect_area =self.shape_len * self.shape_width
    rect_peri = 2 * self.shape_len + 2 * self.shape_width
    return f"Area = {rect_area}cm² \nPerimter = {rect_peri}cm"

class Square(Shape):
  def __init__(self , length):
    super().__init__(length , length)
  def area(self):
    sq_area = self.shape_len ** 2
    sq_peri = self.shape_len * 4
    return f"Area = {sq_area}cm² \nPerimeter = {sq_peri}cm"
  



shape = int(input("What shape are you working with? \n 1.Square \n 2.Rectangle \n:"))
if shape == 1:
  length_input = int(input("Enter Length:"))
  shape_parameters = Square(length_input)
  print(shape_parameters.area())
elif shape == 2:
  length_input = int(input("Enter Length:"))
  breadth_input = int(input("Enter Breadth:"))
  shape_parameters = Rectangle(length_input , breadth_input)
  print(shape_parameters.area())
else:
  print("invalid Entry!")  
