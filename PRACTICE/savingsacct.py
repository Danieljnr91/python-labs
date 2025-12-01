class SavingsAccount:
  def __init__(self , owner , balance):
    self.acct_name = owner
    self.principle = balance
  def deposit(self , deposit_amount):
    self.principle += deposit_amount
    return f"${deposit_amount} has been added to your account balance is now ${self.principle}"
  def withdrawal(self , withdrawn_amount):
    if withdrawn_amount > self.principle:
      return "Insufficient Balance!"
    else:
      self.principle -= withdrawn_amount 
      return f"${withdrawn_amount} has been taken from your account balance is now ${self.principle}"
    
class InterestRate(SavingsAccount):
  def __init__(self , parent_data , rate):
    super().__init__(parent_data.acct_name , parent_data.principle)
    self.interest_rate = rate
  
  def interest_calc(self , time):
    self.interest = self.principle*self.interest_rate*time/100
    return f"${self.interest} has been added to your account over a period of {time}years \n Account balance is now ${self.interest + self.principle}"
  
owner_name = input("Enter name of account:")  
acct_balance = float(input("Enter Account balance:"))
savings_details = SavingsAccount(owner=owner_name , balance=acct_balance)
while True:
  print("Enter \n1. To Deposit \n2. To Withdraw \n3.To check current interest \n4.To Exit")
  choice = int(input("Choose:"))
  if choice == 1:
    dep_amt = float(input("Enter amount to deposit:"))
    print(savings_details.deposit(dep_amt))
  elif choice == 2:
    with_amt = float(input("Enter amount to be withdrawn:"))
    print(savings_details.withdrawal(with_amt))
  elif choice == 3:
    time_money = float(input("Enter time your money has been at the bank:"))
    interest_details = InterestRate(parent_data= savings_details, rate=2.5 )
    print(interest_details.interest_calc(time_money))
  else:
    print("Alright, Exiting...")
    break