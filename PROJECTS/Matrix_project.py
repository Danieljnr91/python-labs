print("MATRIX CALCULATOR")


print("A. 2x2 \n B. 3x3")
print("which matrix are we working with today(A or B)?")
matrix=input(":").lower()

#Matrix choice

if matrix == "a":
    print("You have chosen to operate on a 2x2 matrix")
    print("Enter elements in the matrix seperated by comma")
    matrix_1 = input("First matrix:").split(",")
    matrix_2 = input("Second matrix:").split(",")
    matrix_1_list = [int(i.strip()) for i in matrix_1]
    matrix_2_list = [int(j.strip()) for j in matrix_2]
    
    #Operations
    print("A.Addition \n B.Subtraction \n C.Multiplication")
    operation = input("Choose Operation:").lower()
    if operation == "a":
        first_ans = matrix_1_list[0] + matrix_2_list[0]
        scnd_ans = matrix_1_list[1] + matrix_2_list[1]
        third_ans = matrix_1_list[2] + matrix_2_list[2]
        fourth_ans = matrix_1_list[3] + matrix_2_list[3]
        print(f"({first_ans}  {scnd_ans})")
        print(f"({third_ans}  {fourth_ans})")
    elif operation == "b":
        first_ans = matrix_1_list[0] - matrix_2_list[0]
        scnd_ans = matrix_1_list[1] - matrix_2_list[1]
        third_ans = matrix_1_list[2] - matrix_2_list[2]
        fourth_ans = matrix_1_list[3] - matrix_2_list[3]
        print(f"({first_ans}  {scnd_ans})")
        print(f"({third_ans}  {fourth_ans})")
    else:
        first_ans = matrix_1_list[0] * matrix_2_list[0] + matrix_1_list[1] * matrix_2_list[2]
        scnd_ans = matrix_1_list[0] * matrix_2_list[1] + matrix_1_list[1] * matrix_2_list[3]
        third_ans = matrix_1_list[2] * matrix_2_list[0] + matrix_1_list[3] * matrix_2_list[2]
        fourth_ans = matrix_1_list[2] * matrix_2_list[1] + matrix_1_list[3] * matrix_2_list[3]
        print(f"({first_ans}  {scnd_ans})")
        print(f"({third_ans}  {fourth_ans})")
else:
    print("You've chosen to operate on a 3x3 matrix")
    print("Enter matrix elements seperated by comma")
    matrix_1 = input("First matrix:").split(",")
    matrix_2 = input("Second matrix:").split(",")
    matrix_1_list = [int(i.strip()) for i in matrix_1]
    matrix_2_list = [int(j.strip()) for j in matrix_2]
    
 
    #operations  
    print("A.Addition \n B.Subtraction \n C.Multiplication")
    operation = input("Choose Operation:").lower()
    
    if operation == 'a':
        print("You've chosen to add 3x3 matrix")
        def addition(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
            first_ans = a + j
            second_ans = b + k
            third_ans = c + l
            fourth_ans = d + m
            fifth_ans = e + n 
            sixth_ans = f + o
            sevnth_ans = g + p
            eigth_ans = h + q
            ninth_ans = i + r 
            
            print(f"({first_ans} {second_ans} {third_ans})")
            print(f"({fourth_ans} {fifth_ans} {sixth_ans})")
            print(f"({sevnth_ans} {eigth_ans} {ninth_ans})")
            
        addition(matrix_1_list[0] , matrix_1_list[1] , matrix_1_list[2] , matrix_1_list[3] , matrix_1_list[4] , matrix_1_list[5] , matrix_1_list[6] , matrix_1_list[7] , matrix_1_list[8] , matrix_2_list[0] , matrix_2_list[1] , matrix_2_list[2] , matrix_2_list[3] , matrix_2_list[4] , matrix_2_list[5] , matrix_2_list[6] , matrix_2_list[7] , matrix_2_list[8])
        
        
    
       