from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    
    def get(self,name):
        store=StoreModel.find_item_by_name(name)
        if store:
            return store.json()
        return {'msg':'store not found'},404
        
    def post(self,name):
        
        if StoreModel.find_item_by_name(name):
            return {'msg':'A store '+name+' is already exists'},404
        
        store=StoreModel(name)
        
        try:
            store.insert_and_update_item()
        except:
            return{'msg':'error occured while creating the store'},500
        
        return store.json(),201
        
    def delete(self): 
        store=StoreModel.find_item_by_name(name)
        
        if store:
            store.delete_item()
         
        return {'msg':'store is deleted'}
        
        
class StoreList(Resource):
    
    def get(self):
        
        return {'stores':[store.json() for store in StoreModel.query.all()]}