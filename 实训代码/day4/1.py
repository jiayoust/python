import socket
import time
import tkinter
from tkinter.scrolledtext import ScrolledText
import threading
import requests
from socket import *
from time import ctime
from tkinter import *
def AI_Talk(s):
    response = requests.post("http://www.tuling123.com/openapi/api",data={
        "key": "5636c0854e88430383a861151bf764ca",
         "info": s,
        "userid": "123456" })
    response = response.json()
    answer=response['text']
    return answer
    #线程二函数，用来进行对话
def Sever_Thread(sock,caddr):
    Text_Show.insert('end',"客户端@"+str(caddr[1])+"已连接!\n")
    while True:
        data = str(sock.recv(1024).decode('UTF-8'))
        if data == "quit":
            Text_Show.insert('end',"客户端@"+str(caddr[1])+"终止了对话\n")
            Text_Show.see(tkinter.END)
            break
        else:
            Text_Show.insert('end',"来自客户端@"+str(caddr[1])+"的消息为："+data+'\n')
            Text_Show.see(tkinter.END)
            time.sleep(0.2)
            data=AI_Talk(data)
            sock.sendall(bytes(data, 'UTF-8'))
            sock.close()
def Sever_Accept(ss):
    while True:
        sock,caddr=ss.accept()
        Thread2 = threading.Thread(target=Sever_Thread, args=(sock,caddr))
        Thread2.daemon=True
def Sever_Init():
    HOST = ''
    PORT = 4700
    ADDR = (HOST, PORT)
    ss = socket(AF_INET, SOCK_STREAM, 0)
    ss.bind(ADDR)
    ss.listen(20)
    Thread1=threading.Thread(target=Sever_Accept,args=(ss,))
    Thread1.daemon=True
    Thread1.start()
if __name__ == "__main__":
    root=tkinter.Tk()
    root.title("聊天小程序服务器端 ")
    frame1=Frame(root)
    frame1.pack()
    IP_Show_Label=Label(frame1,text="默认IP:127.0.0.1\n默认端口为6000\n无法更改!!!")
    IP_Show_Label.pack(side='left')
    frame2=Frame(root)
    frame2.pack()
    Text_Show=ScrolledText(frame2,width=100,height=30)
    Text_Show.bind("<KeyPress>",lambda e:"break")
    Text_Show.pack(side="bottom",fill = 'both', expand = True)
    Sever_Init()
    root.mainloop()
