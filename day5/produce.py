from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    f=open("index","r",encoding="utf-8")

    data=f.read()
    f.close()
    return  data
if __name__ == '__main__':

    app.run()