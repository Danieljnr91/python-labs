class BankAccount:
  def __init__(self , owner , acct_balance):
    self.owners_name = owner
    self.amt_in_acct = acct_balance
  def deposit(self , amt_deposit):
    self.amt_in_acct += amt_deposit
    return f"${amt_deposit} has been added to your account, remaining balance is ${self.amt_in_acct}"
  def withdraw(self , amt_withdrawn):
    if amt_withdrawn > self.amt_in_acct:
      print("Insufficient Balance!")
    else:
       self.amt_in_acct -= amt_withdrawn
       return f"${amt_withdrawn} has been taken from your account, remaining balance is ${self.amt_in_acct}"
  def balance(self):
    return f"Your Bank Balance is ${self.amt_in_acct}"  
     
owners_name = input("Enter name of Account:")
cash_in_acct = float(input("Enter Your Account Balance:"))     
owners_details = BankAccount(owners_name , cash_in_acct)


while True:
  print("Press... \n 1. to deposit \n 2. to withdraw \n 3. to check balance \n 4. to exit")
  operation = float(input("What do u wish to do?"))
  if operation ==  1:
    depo_amt = float(input("How much are you depositing?:"))
    print(owners_details.deposit(depo_amt))
  elif operation == 2:
    withdraw_amt = float(input("How much are you taking?:"))
    print(owners_details.withdraw(withdraw_amt))
  elif operation == 3:
    print(owners_details.balance())
  else:
    print("Exiting...")
    break
  
   
      
          

  
  
  
  