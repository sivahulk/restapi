import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegistor(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help='pls fill the username')
    parser.add_argument('password',type=str,required=True,help='pls fill the password')
    
    def post(self):
        data=UserRegistor.parser.parse_args()# data from json payload
        
        if UserModel.find_by_username(data['username']): #checking the username exists. if not it wwill create it in db 
            return {'msg':'this '+data['username']+' username is already exists'},400 #400 Bad Reques
        
        user=UserModel(**data)#data['username'],data['password'] packing the dictionary
        user.save_to_db()
        
        return {'msg':'user created sucessfully'},201 #201 created
        