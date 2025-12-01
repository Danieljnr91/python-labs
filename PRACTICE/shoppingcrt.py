class ShoppingCart:
  def __init__(self , items):
    self.shopping_list = items.copy()
    self.initial_list = items.copy()
  def restore_point(self):
    return self.initial_list
  def add_itmes(self , new_items):
    self.shopping_list.extend(new_items)
    new_list = self.shopping_list
    return new_list
  def remove_items(self , ex_items):
    for i in ex_items:
     self.shopping_list.remove(i)
     old_items = self.shopping_list
    return old_items
  




def recursing():
  initial_shopping_items = input("Enter items seperted by comma \n:").split(",")
  initial_shopping_list = [i.strip() for i in initial_shopping_items]
  shopping_details = ShoppingCart(initial_shopping_list)

  while True:
    print("Enter \n 1. To add new items \n 2. To remove new items \n 3. To restore initial list \n 4. To enter new list \n 5. To exit   ")
    operations = int(input("Choose number:"))
    if operations == 1:
      new_items = input("Enter items to add seperated by comma \n:").split(",")
      new_items_list = [i for i in new_items]
      print(shopping_details.add_itmes(new_items_list))
    elif operations == 2:
      ex_items = input("Enter items to be removed seperated by comma \n:").split(",")
      ex_items_list = [i for i in ex_items]
      for j in ex_items_list:
       pass
      if j not in initial_shopping_list:
        print("One or more items are not in your initial list")
      else:
        print(shopping_details.remove_items(ex_items_list))
    elif operations == 3:
        print(shopping_details.restore_point())
    elif operations == 4:
      recursing()
      break
    else:
      print("Alright, Exiting...")
      break
recursing()   

  