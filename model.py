from sqlalchemy import create_engine
import json
from flask import make_response, jsonify

class user_model():
    def __init__(self):
        try:
            self.con = create_engine('sqlite:///iris.db')
            self.con.autocommit=True        
            print("Connection Sucessful")
        except:
            print("Error")

    def get(self):
        #Business logic
        return make_response({"message":"Service is up"},201)

    def user_getall_model(self):
        #Business logic
        query = self.con.execute("Select * from iris")
        res= {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        if len(res)>0 :
            res = make_response({"payload":res},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return  make_response({"message":"No Data Found"},201)

    def user_addone_model(self,data):
        #print(data)
        query = self.con.execute(f"INSERT INTO iris(sepal_length, sepal_width, petal_length, petal_width, species) VALUES('{data['sepal_length']}', '{data['sepal_width']}', '{data['petal_length']}', '{data['petal_width']}', '{data['species']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)

    def add_multiple_users_model(self, dataa):
        # Generating query for multiple inserts
        qry = "INSERT INTO iris(sepal_length, sepal_width, petal_length, petal_width, species) VALUES "
        for data in dataa:
            #print(data)
            qry += f"('{data['sepal_length']}', '{data['sepal_width']}', '{data['petal_length']}', '{data['petal_width']}', '{data['species']}'),"
        finalqry = qry.rstrip(",")
        query =self.con.execute(finalqry)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)