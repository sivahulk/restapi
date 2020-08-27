from app import app
from db import db

db.init_app(app)

@app.before_first_request #this decorator function will execute before first request so it will create table which we used in py files
def create_all_table():
    db.create_all()
