from models.dataset import User
from models.mysql_db import db

def select_by_username(username):
    user = User.query.filter_by(username = username).first()
    return user

def get_by_user_id(user_id):
    user = User.query.filter_by(id = user_id).first()
    return user

def save_user(username, password, email):
    user = select_by_username(username)       
    if user:
        raise ValueError("User already exists")
    
    user = User(
        username=username,
        password=password,
        email=email
    )
    db.session.add(user)
    db.session.commit()
    return user
