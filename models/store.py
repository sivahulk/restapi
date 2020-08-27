from db import db

class StoreModel(db.Model):
    
    __tablename__='stores'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    
    items=db.relationship('ItemModel',lazy='dynamic')
    
    def __init__(self,name):
        self.name=name
      
    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}
    
    @classmethod
    def find_item_by_name(cls,name):
        return cls.query.filter_by(name=name).first()#select * from items where name=name limit=1(sqlalchemy will do query for us)
        
    def insert_and_update_item(self):
        db.session.add(self)#sqlalchemy can convert object into row
        db.session.commit()
        
    def delete_item(self):
        db.session.delete(self)#sqlalchemy can convert object into row
        db.session.commit()