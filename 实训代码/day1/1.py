import qrcode
print("输入你想要生成二维码的个数")
x = int(input())
print("依次输入生成的二维码的内容以空格分隔")
b = input()
xlist = b.split(" ")
num=0
for k in range(0,x):
    
   img = qrcode.make(xlist[num])
   img.save("%d.jpg"%(num))
#    plt.imshow(img)
#    plt.savefig("%d.jpg"%(num))
   num=num+1

