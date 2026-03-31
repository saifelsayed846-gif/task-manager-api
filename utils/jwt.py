from flask import current_app
import jwt 
import datetime

def generate_token(user_id):
    payloud={
        "user_id":user_id,
        "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
    }

    token=jwt.encode(payloud,current_app.config['SECRET_KEY'],algorithm='HS256')
    return token