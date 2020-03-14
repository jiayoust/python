import qrcode
import time

while True:
    data = input("\n请输入内容：")
    img = qrcode.make(data)
    img.save("二维码.jpg")
    print("二维码生成成功！")
    time.sleep(0.1)  # 休眠100ms
    img.show()
