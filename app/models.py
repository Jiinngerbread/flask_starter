from . import db
from werkzeug.security import generate_password_hash


class UserProperty(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'userProperty'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title= db.Column(db.String(100))
    description= db.Column(db.String(256))
    roomNum= db.Column(db.INTEGER())
    bRoomNum = db.Column(db.INTEGER())
    price= db.Column(db.DecimalField())
    propertyType= db.Column(db.String(10))
    location= db.Column(db.String(256))
    photo= db.Column(db.String(256))
   
    def __init__(self, title, description, roomNum, bRoomNum, price, propertyType, location, photo):
    self.title= title
    self.description= description
    self.roomNum=roomNum
    self.bRoomNum =bRoomNum
    self.price= price
    self.propertyType= propertyType
    self.location= location
    self.photo=photo
    

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  
        except NameError:
            return str(self.id)  

    def __repr__(self):
        return '<User %r>' % (self.username)
