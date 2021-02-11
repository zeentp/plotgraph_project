import matplotlib.pyplot as plt
from socket import *
import random
import pickle

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()

def BVA (x_max,x_min,y_max,y_min):
    x=[x_min,x_min+rand_x,(x_min+x_max)/2,x_max-rand_x,x_max,
        (x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2]
    y=[(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,
        y_max,y_max-rand_y,y_min+rand_y,y_min]
    data_x = pickle.dumps(x)
    data_y = pickle.dumps(y)

    connectionSocket.send(data_x)
    connectionSocket.send(data_y)
        
def Robustness (x_max,x_min,y_max,y_min):
    x=[x_min,x_min+rand_x,(x_min+x_max)/2,x_max-rand_x,x_max,
        (x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,
        x_min-rand_x,x_max+rand_x,(x_min+x_max)/2,(x_min+x_max)/2]
    y=[(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,
        y_max,y_max-rand_y,y_min+rand_y,y_min,
        (y_max+y_min)/2,(y_max+y_min)/2,y_max+rand_y,y_min-rand_y]  
    data_x = pickle.dumps(x)
    data_y = pickle.dumps(y)
    connectionSocket.send(data_x)
    connectionSocket.send(data_y)
def Worst_Case (x_max,x_min,y_max,y_min):
    x=[x_min,x_min+rand_x,(x_min+x_max)/2,x_max-rand_x,x_max,
        (x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2,(x_min+x_max)/2
        ,x_min,x_min+rand_x,x_min,x_min+rand_x,x_min,x_min+rand_x,x_min,x_min+rand_x,
        x_max-rand_x,x_max,x_max-rand_x,x_max,x_max-rand_x,x_max,x_max-rand_x,x_max]
    y=[(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,(y_max+y_min)/2,
        y_max,y_max-rand_y,y_min+rand_y,y_min,
        y_max,y_max,y_max-rand_y,y_max-rand_y,y_min+rand_y,y_min+rand_y,y_min,y_min,
        y_max,y_max,y_max-rand_y,y_max-rand_y,y_min+rand_y,y_min+rand_y,y_min,y_min]
    data_x = pickle.dumps(x)
    data_y = pickle.dumps(y)
    connectionSocket.send(data_x)
    connectionSocket.send(data_y)
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
    data_x = pickle.dumps(x)
    data_y = pickle.dumps(y)
    connectionSocket.send(data_x)
    connectionSocket.send(data_y)
while True:
    print('Connected by', addr)
    while True:
        x_min = connectionSocket.recv(1024).decode() # รับ
        x_min = float(x_min)
        print("From Client x min : " + str(x_min))
        if x_min < 0:
            msg = 'Please enter a positive number'
            connectionSocket.send(msg.encode())
        elif x_min >= 5000:
            msg = "x min should less than maximum number (Maximum number: 5000)"
            connectionSocket.send(msg.encode())
        else:
            msg = 'break'
            connectionSocket.send(msg.encode())
            break
    while True:
        x_max = connectionSocket.recv(1024).decode() # รับ
        x_max = float(x_max)
        print("From Client x max : " + str(x_max))
        if x_max <= x_min and x_max >= 0:
            msg = 'Please input correct value'
            connectionSocket.send(msg.encode())
        elif x_max > 5000 :
            msg = 'Please input correct value (Maximum number: 5000)'
            connectionSocket.send(msg.encode())
        elif x_max < 0:
            msg = 'Please enter a positive number'
            connectionSocket.send(msg.encode())
        elif x_max > x_min:
            msg = 'break'
            connectionSocket.send(msg.encode())
            break
    while True:
        y_min = connectionSocket.recv(1024).decode()
        y_min = float(y_min)
        print("From Client y min : " + str(y_min))
        if y_min < 0:
            msg = 'Please enter a positive number'
            connectionSocket.send(msg.encode())
        elif y_min >= 5000:
            msg = 'y min should less than maximun number'
            connectionSocket.send(msg.encode())
        else:
            msg = 'break'
            connectionSocket.send(msg.encode())
            break
    while True:
        y_max = connectionSocket.recv(1024).decode()
        y_max = float(y_max)

        print("From Client y max: " + str(y_max))
        if y_max <= y_min:
            msg = ('Please input correct value')
            connectionSocket.send(msg.encode())
        elif y_max > 5000 :
            msg = ("Please input correct value (Maximun number: 5000)")
            connectionSocket.send(msg.encode())
        elif y_max > y_min:
            msg = 'break'
            connectionSocket.send(msg.encode())
            break
    rand_x = ((x_max - x_min)/100)*10
    rand_y = ((y_max - y_min)/100)*10
    while True:
        str_choice = connectionSocket.recv(1024).decode()
        str_choice = int(str_choice)
        if(str_choice==1):
            BVA(x_max,x_min,y_max,y_min)
            break
        elif(str_choice==2):
            Worst_Case(x_max,x_min,y_max,y_min)
            break
        elif(str_choice==3):
            Robustness(x_max,x_min,y_max,y_min)
            break
        elif(str_choice==4):
            Worst_Case_Robustness(x_max,x_min,y_max,y_min)
            break
    print("Client disconnected.")
    connectionSocket, addr = serverSocket.accept()
connectionSocket.close()