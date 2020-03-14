import qrcode
import requests
from tkinter import *
from PIL import Image,ImageTk
def get_ewm():
    strs = entry.get()
    img = qrcode.make
    img.save("二维码.jpg" )
if __name__ == '__main__':
    tk = Tk()
    tk.title('二维码生成器')
    tk.geometry('640x600+200+20')
    entry = Entry(tk, font=('微软雅黑'),width=60)  # 创建输入框
    entry.grid(row=1, column=4)  # 定位第1行3列
    str_b = Button(tk,text='生成二维码',command=get_ewm)
    str_b.grid(row=1,column=5)
    tk.mainloop()
