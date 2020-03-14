from flask import Flask
app = Flask(__name__)

@app.route('/post/<int:add1>&<int:add2>')
def post(add1, add2):
    # show the post with the given id, the id is an integer
    return str(add1+add2)
if __name__ == '__main__':

    app.run()