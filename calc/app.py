# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div

app= Flask(__name__)

@app.route('/add')
def add_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"a plus b equals {add(a,b)}"
  
@app.route('/sub')
def sub_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"a minus b equals {sub(a,b)}"

@app.route('/mult')
def mult_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"a times b equals {mult(a,b)}"

@app.route('/div')
def div_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"a times b equals {div(a,b)}"