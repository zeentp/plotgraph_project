import matplotlib.pyplot as plt 
while True:
    x_min = int(input("Enter x min : "))
    x_max = int(input("Enter x max : "))
    y_min = int(input("Enter y min : "))
    y_max = int(input("Enter y max : "))
    if(x_max > x_min and y_max > y_min):
        break
    elif(x_max <= x_min and y_max <= y_min):
        print("Both max value must more than min value")
    elif(x_max <= x_min):
        print("x_max must more than x_min")
    elif(y_max <= y_min):
        print("y_max must more than y_min")
    else:
        print("*** Error: Invalid value ***")
rand_x = ((x_max - x_min)/100)*10
rand_y = ((y_max - y_min)/100)*10
print("-----------------------------------------------------------------------")
while True:
    print("BVA[1]\nWorst Case[2]\nRobustness[3]\nWorst Case Robustness[4]")
    print("-----------------------------------------------------------------------")

    str_choice = int(input("Select Your Choice [1-4]: "))
    if(str_choice != 1 and str_choice != 2 and str_choice != 3 and str_choice != 4):
        print("*** Erorr: Please Enter [1-4] ***")
    else:
        break

def BVA (x_max,x_min,y_max,y_min):
    x=[x_min,x_min+rand_x,(x_min+x_max)/2,x_max-rand_x,x_max,
        (x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2]
    y=[(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,
        y_max,y_max-rand_y,y_min+rand_y,y_min]
    plt.xlabel('X',color="blue") 
    plt.ylabel('                                                                                              Y',color="blue")
    plt.scatter(x,y,color=["green","green","red","green","green","red","red","red","red"])
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    plt.title('BVA graph!') 
    plt.show()

def Robustness (x_max,x_min,y_max,y_min):
    x=[x_min,x_min+rand_x,(x_min+x_max)/2,x_max-rand_x,x_max,
        (x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,
        x_min-rand_x,x_max+rand_x,(x_min+x_max)/2,(x_min+x_max)/2]
    y=[(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,
        y_max,y_max-rand_y,y_min+rand_y,y_min,
        (y_max+y_min)/2,(y_max+y_min)/2,y_max+rand_y,y_min-rand_y]
    plt.xlabel('X',color="blue") 
    plt.ylabel('                                                                                              Y',color="blue")
    plt.scatter(x,y,color=["green","green","red","green","green","red","red","red","red","green","green","red","red"])
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    plt.title('Robustness graph!') 
    plt.show()

def Worst_Case (x_max,x_min,y_max,y_min):
    x=[x_min,x_min+rand_x,(x_min+x_max)/2,x_max-rand_x,x_max,
        (x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2
        ,x_min,x_min+rand_x,x_min,x_min+rand_x,x_min,x_min+rand_x,x_min,x_min+rand_x,
        x_max-rand_x,x_max,x_max-rand_x,x_max,x_max-rand_x,x_max,x_max-rand_x,x_max]
    y=[(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,
        y_max,y_max-rand_y,y_min+rand_y,y_min,
        y_max,y_max,y_max-rand_y,y_max-rand_y,y_min+rand_y,y_min+rand_y,y_min,y_min,
        y_max,y_max,y_max-rand_y,y_max-rand_y,y_min+rand_y,y_min+rand_y,y_min,y_min]
    plt.xlabel('X',color="blue") 
    plt.ylabel('                                                                                              Y',color="blue")      
    plt.scatter(x,y,color=["green","green","red","green","green","red","red","red","red","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green"])
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    plt.title('Worst Case graph!') 
    plt.show()

def Worst_Case_Robustness(x_max,x_min,y_max,y_min):
    x=[x_min,x_min+rand_x,(x_min+x_max)/2,x_max-rand_x,x_max,
        (x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2
        ,x_min,x_min+rand_x,x_min,x_min+rand_x,x_min,x_min+rand_x,x_min,x_min+rand_x,
        x_max-rand_x,x_max,x_max-rand_x,x_max,x_max-rand_x,x_max,x_max-rand_x,x_max,
        x_min-rand_x,x_max+rand_x,(x_min+x_max)/2,(x_min+x_max)/2,
        x_min-rand_x,x_min-rand_x,x_min-rand_x,x_min-rand_x,x_min-rand_x,x_min-rand_x,
        x_min,x_min,x_min+rand_x,x_min+rand_x,x_max-rand_x,x_max-rand_x,x_max,x_max,
        x_max+rand_x,x_max+rand_x,x_max+rand_x,x_max+rand_x,x_max+rand_x,x_max+rand_x]
    y=[(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,
        y_max,y_max-rand_y,y_min+rand_y,y_min,
        y_max,y_max,y_max-rand_y,y_max-rand_y,y_min+rand_y,y_min+rand_y,y_min,y_min,
        y_max,y_max,y_max-rand_y,y_max-rand_y,y_min+rand_y,y_min+rand_y,y_min,y_min,
        (y_max+y_min)/2,(y_max+y_min)/2,y_max+rand_y,y_min-rand_y,
        y_max+rand_y,y_max,y_max-rand_y,y_min+rand_y,y_min,y_min-rand_y,
        y_max+rand_y,y_min-rand_y,y_max+rand_y,y_min-rand_y,y_max+rand_y,y_min-rand_y,y_max+rand_y,y_min-rand_y,
        y_max+rand_y,y_max,y_max-rand_y,y_min+rand_y,y_min,y_min-rand_y,
        ]
    plt.xlabel('X',color="blue") 
    plt.ylabel('                                                                                              Y',color="blue")      
    plt.scatter(x,y,color=["green","green","red","green","green","red","red","red","red","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green",
    "green","green","red","red","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green","green"])
    plt.title('Worst Case Robustness graph!') 
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    plt.show()

if(str_choice==1):
    BVA(x_max,x_min,y_max,y_min)
elif(str_choice==2):
    Worst_Case(x_max,x_min,y_max,y_min)
elif(str_choice==3):
    Robustness(x_max,x_min,y_max,y_min)
elif(str_choice==4):
    Worst_Case_Robustness(x_max,x_min,y_max,y_min)
else:
    print("*** Erorr: Please Enter [1-4] ***")