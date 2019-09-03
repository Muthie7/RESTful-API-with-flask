from db import db
from app import app

db.init_app(app)


@app.before_first_request  # auto creates all tables from the resources present first before starting off the API
def create_tables():
    db.create_all()

# basically it does exactly what the __main__ is doing but doesnt import resources itself
# also CUT the decorator for building the db tables so that whenever you execute run.py it also follows
