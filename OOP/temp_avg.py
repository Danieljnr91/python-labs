import os

class CityTemperatureAvg:
  def __init__(self , temp_dict):
    self.temperature = temp_dict
    self.avg_temp_dict = {}
    self.avg_temp_list = []
  def average(self):
    for temp_keys in self.temperature:
      temp = self.temperature[temp_keys]
      temp_sum = sum(temp)
      temp_avg = round(temp_sum/len(temp) , 2)
      self.avg_temp_dict[temp_keys] = temp_avg
      self.avg_temp_list.append(temp_avg)
      
      
class TemperatureConverter(CityTemperatureAvg):
  def __init__(self, cityavg_info):
    super().__init__(cityavg_info.temperature)
    self.kelvin_dict = {}
    self.farenheit_dict = {}
  def temp_coversion(self):
    for conversion in self.avg_temp_list:
      kelvin = 273 + conversion
      farenheit = conversion*9/5+32
    for name in self.temperature:
      self.kelvin_dict[name] = kelvin
      self.farenheit_dict[name] = farenheit
    
    
class AvgRankings(TemperatureConverter):
  def __init__(self, relative_data):
    super().__init__(relative_data)
    self.average()
    self.temp_coversion()
  def rankings(self):
    highest = self.avg_temp_list[0]
    for i in self.avg_temp_list:
      if i > highest:
        highest = i 
    for name in self.avg_temp_dict:
      if self.avg_temp_dict[name] == highest:
        return f"{name} had the highest temperature through out the year with an avearge of {highest}°C \nother cities \n{self.avg_temp_dict} \ntemperatures in farenheit are \n{self.farenheit_dict}°F \nand in Kelvin \n{self.kelvin_dict}K"

x = CityTemperatureAvg({"y":[34,30,40] , "b":[56,54,76]})
n = AvgRankings(x)
print(n.rankings())
    
  
      
   