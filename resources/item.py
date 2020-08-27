from flask import request
from flask_restful import reqparse,Resource
from flask_jwt import jwt_required
from models.item import ItemModel

#defining resource
class Item(Resource):
    #we can use parser for one or function by defining it in one place without self because the parser is itself belong to class
    #so we can call it by class name 
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="This price field can't leave blank")
    parser.add_argument('store_id',type=int,required=True,help="Every item needs store id")
    
    
    @jwt_required()
    def get(self,name):
        
        item=ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        
        return {'msg':'item not found'},404 #404 not found
    
    def post(self,name):
        
        if ItemModel.find_item_by_name(name):
            return {'msg':'The '+name+' is already exists'},400
        
        data=Item.parser.parse_args()
        item=ItemModel(name,data['price'],data['store_id'])
        
        try:
            item.insert_and_update_item()
        except:
            return {'msg':'error occured while inserting the item'}, 500#500 internal server error
        
        return item.json(), 201 #201 created
    
    def delete(self,name):
        
        item=ItemModel.find_item_by_name(name)
        
        if item:
            item.delete_item()
        
        return {'message':'The given '+name+' item is deleted'}
    
    def put(self, name):
        
        data=Item.parser.parse_args() # data from json payload
        
        returned_item_obj=ItemModel.find_item_by_name(name)
        
        if(returned_item_obj is None):
            returned_item_obj=ItemModel(name,data['price'],data['store_id'])
            
        else:
            returned_item_obj.price=data['price']
            
        returned_item_obj.insert_and_update_item()
        
        return returned_item_obj.json()

#defining resource
class ItemsList(Resource):
    def get(self):    
        return {'items':[item.json() for item in ItemModel.query.all()]}
        #list(map(lambda x: x.json(),ItemModel.query.all()))