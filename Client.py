from socket import *
import matplotlib.pyplot as plt
import pickle
def plotGraph(x,y,choice):
    if choice == "1":
        plt.xlabel('X',color="blue") 
        plt.ylabel('                                                                                              Y',color="blue")
        plt.scatter(x,y)
        for i_x, i_y in zip(x, y):
            plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
        plt.title('BVA graph!') 
        plt.show()
    elif choice == "3":
        plt.xlabel('X',color="blue") 
        plt.ylabel('                                                                                              Y',color="blue")
        plt.scatter(x,y)
        for i_x, i_y in zip(x, y):
            plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
        plt.title('Robustness graph!') 
        plt.show()
    elif choice == "2":
        plt.xlabel('X',color="blue") 
        plt.ylabel('                                                                                              Y',color="blue")      
        plt.scatter(x,y)
        for i_x, i_y in zip(x, y):
            plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
        plt.title('Worst Case graph!') 
        plt.show()
    elif choice == "4":
        plt.xlabel('X',color="blue") 
        plt.ylabel('                                                                                              Y',color="blue")      
        plt.scatter(x,y)
        plt.title('Worst Case Robustness graph!') 
        for i_x, i_y in zip(x, y):
            plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
        plt.show()

serverName = 'localhost'
serverPort = 12000
str_choice = ''
x_min = 0 
x_max = ''
y_min = ''
y_max = ''
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while True: ## Client
    while True:
        while x_min is not int:
            try:
                x_min =float(input('Enter x min: '))
                break
            except ValueError:
                print('Please enter a valid number ')
        x_min =str(x_min)
        clientSocket.send(x_min.encode()) # ส่ง
        msg = clientSocket.recv(1024).decode()
        if msg == 'break':
            break
        print(msg)
    while True:
        while x_max is not int:
            try:
                x_max =float(input('Enter x max: '))
                break
            except ValueError:
                print('Please enter a valid number ')
        x_max =str(x_max)
        clientSocket.send(x_max.encode())
        msg = clientSocket.recv(1024).decode()
        if msg == 'break':
            break
        print(msg)
    while True:
        while y_min is not int:
            try:
                y_min =float(input('Enter y min: '))
                break
            except ValueError:
                print('Please enter a valid number ')
        y_min =str(y_min)
        clientSocket.send(y_min.encode())
        msg = clientSocket.recv(1024).decode()
        if msg == 'break':
            break
        print(msg)
    while True:
        while y_max is not int:
            try:
                y_max =float(input('Enter y max: '))
                break
            except ValueError:
                print('Please enter a valid number ')
        y_max =str(y_max)
        clientSocket.send(y_max.encode())
        msg = clientSocket.recv(1024).decode()
        if msg == 'break':
            break
        print(msg)
    while True:
        print("-----------------------------------------------------------------------")
        print("BVA[1]\nWorst Case[2]\nRobustness[3]\nWorst Case Robustness[4]")
        print("-----------------------------------------------------------------------")
        while str_choice is not int:
            try:
                str_choice = int(input("Select Your Choice [1-4]: "))
                str_choice = str(str_choice)
                clientSocket.send(str_choice.encode())
                break
            except ValueError:
                print('Please select correct type')
        
        if(str_choice != "1" and str_choice != "2" and str_choice != "3" and str_choice != "4"):
            print("*** Erorr: Please Enter [1-4] ***")
        else:
            msg = str(str_choice)
            clientSocket.send(msg.encode())
            break   
    msg = clientSocket.recv(1024)
    x = pickle.loads(msg)
    msg1 = clientSocket.recv(1024)
    y = pickle.loads(msg1)
    plotGraph(x,y,str_choice)
    break
clientSocket.close()
    
  
