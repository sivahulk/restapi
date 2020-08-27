import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegistor
from resources.item import Item,ItemsList
from resources.store import Store,StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///data.db')# if u r running this in local os will take sqlite because second parameter is default one. if it is running in heroku it willtake 1st param
app.config['SQLALCHEMY_TRACK_MODIFICATIONs']=False #this will turn off track in flask and not the flask-sqlalchemy. why we used False because we imported flask-sqlalchemy so it will have its own tracking.
app.secret_key='hulk'
api=Api(app)

jwt=JWT(app,authenticate, identity) #/auth

items=[]

#adding resource to api
api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')#http://127.0.0.1:5000/item/chair
api.add_resource(StoreList,'/stores')
api.add_resource(ItemsList,'/items')
api.add_resource(UserRegistor,'/registor')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000)
