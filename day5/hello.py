from flask import Flask
import qrcode
import time
app = Flask(__name__)

@app.route('/')
def home():
    data = input("\n请输入内容：")
    img = qrcode.make(data)
    img.save("picture.jpg")
    print("二维码生成成功！")
    time.sleep(0.1)  # 休眠100ms
    img.show()





if __name__ == '__main__':
    app.run()
