import os
from class_data import StudentData , AverageRankings
      
data_dictionary = {}
end = False
while not end:
  student_name = input("Enter Student Name:")
  student_marks = input("Enter Marks seperated by comma \n:").split(",")
  student_marks_list = [int(i) for i in student_marks]
  data_dictionary[student_name] = student_marks_list
  student_data_object = StudentData(marks_dict=data_dictionary)
  average_details = AverageRankings(student_data_object)
  multiple = input("Are there more students?(Y/N):").lower()
  if multiple == "n":
    print(average_details.rankings())
    end = True
  else:
    os.system("cls")

# from fractions import Fraction
# j = ["1/2" , "1/3" , "3"]
# ifr = [Fraction(i) for i in j ]
# print(ifr)

# print(ifr[0] + ifr[1])
# print(ifr[2])

# def x(p):
#   y = p + 3
#   print("hello")
#   return y
  
# u = x(3)
# print(u)