
from flask import Flask, request
from sqlalchemy import create_engine
from json import dumps
from flask import make_response, jsonify
from flask import request
from model import user_model

app = Flask(__name__)

obj =user_model()

@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/get",methods=['GET'])
def get():
    return obj.get()

@app.route("/user/getall",methods=['GET'])
def getall_controller():
    return obj.user_getall_model()

@app.route("/user/add",methods=["POST"])
def addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/addmultiple", methods=["POST"])
def add_multiple_users():
    return obj.add_multiple_users_model(request.json)

if __name__ == '__main__':
     app.run(debug=False,host='0.0.0.0')



