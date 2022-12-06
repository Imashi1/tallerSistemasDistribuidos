from tkinter import *
from tkinter import ttk
from socket import *
import threading
                                         
def connect(): 
    global connectionSocket 
 
    serverPort = 12345
    socketServer = socket(AF_INET, SOCK_STREAM)
    socketServer.bind(('',serverPort))
    socketServer.listen(1) 
    print('The server is ready to receive') 
    
    while True:    
        connectionSocket, addr = socketServer.accept()
        connectionSocket.close()
        break
    s=0

def connectit():
    global s
    if (s==0):
        t = threading.Thread(target=connect)
        t.start()
        s = 1
s = 0
root = Tk()
root.title("Server App")
    
button_connect = ttk.Button(root,text = 'Connect', width = 20, command = connectit)

button_connect.grid(row = 0, column = 0) 
            
root.mainloop()