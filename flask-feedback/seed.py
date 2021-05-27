from models import connect_db, db #import classes
from app import app

connect_db(app)
#* create all tables
db.drop_all()
db.create_all()


#* if table isn't empty, empty it
# User.query.delete()