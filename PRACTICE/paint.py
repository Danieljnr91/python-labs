def paint_number(length , width):
    area = length * width
    no_paints = area / 7
    nos_paint = round(no_paints)
    print(f"You'll need about {nos_paint} paints to paint this wall of area {area} sq. m")
    
parameters = input("Length and width seperated by comma:").split(",")

int_para =[]
for i in parameters:
    int_para.append(int(i.strip()))

paint_number(int_para[0] , int_para[1])