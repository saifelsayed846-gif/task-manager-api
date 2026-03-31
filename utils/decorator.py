from functools import wraps
from flask import request,jsonify,current_app
import jwt
def token_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        auth_header=request.headers.get('Authorization')

        if auth_header:
            try:
                token=auth_header.split(" ")[1]
            except:
                return jsonify({
                    'success':False,
                    'error':'Invalid token format'
                }),401

        if not token:
            return jsonify({
                'success':False,
                'error':'Token is missing'
            }),401

        try:

            data=jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
                )
            user_id=data.get('user_id') 

        except jwt.ExpiredSignatureError:
            return jsonify ({
                'success':False,
                'error':'Token expired'
            }),401
        
        except jwt.InvalidTokenError:
            return jsonify({
                'success':False,
                'error':'Invalid token'
            }),401
        
        
        return func(user_id,*args,**kwargs)
    
    return wrapper
