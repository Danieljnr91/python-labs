import os 

class StudentData:
  def __init__(self , marks_dict):
    self.student_dict = marks_dict
  def student_averages(self):
    self.mark_averages = {}
    self.mark_avg_list = []
    for self.names in self.student_dict:
      key_list = self.student_dict[self.names]
      self.total_sum = sum(key_list)
      self.averages = self.total_sum/len(key_list)
      self.mark_averages[self.names] = self.averages
      self.mark_avg_list.append(self.averages)
    
class AverageRankings(StudentData):
  def __init__(self , parent_info):
    super().__init__(parent_info.student_dict)
  def rankings(self):
    self.student_averages()
    self.highest_average = self.mark_avg_list[0]
    for average in self.mark_avg_list:
      if average > self.highest_average:
        self.highest_average = average
    for names in self.mark_averages:
        if self.mark_averages[names] == self.highest_average:
          return f"{names} topped the class with {self.highest_average} marks \n {self.mark_averages}"
      
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
  else:
    os.system("cls")
  

