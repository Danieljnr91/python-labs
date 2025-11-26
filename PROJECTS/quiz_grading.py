import os

def winner(cont_data):
    highest_score = 0
    victor = ""
    for key in cont_data:
        cont_marks = cont_data[key]
        if cont_marks > highest_score:
            highest_score = cont_marks
            victor = key
    print(f"{victor} took the lead by {highest_score} points")
        
        

cont_details = {}
end_loop = False
while not end_loop:
    cont_name = input("Enter name of contestant:")
    cont_score = int(input("Enter score of contestant:"))
    cont_details[cont_name] = cont_score
    do_over = input("Are there more contestants(Y/N)?:").lower()
    if do_over == 'n':
        winner(cont_details)
        print(cont_details)
    else:
        os.system("cls")
        
       

