from flask import Blueprint,jsonify,request
from models.user import User
from models.task import Task
from extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
from utils.jwt import generate_token

auth=Blueprint('auth',__name__)

@auth.route('/register',methods=['POST'])
def add_user():
    data=request.get_json()

    if not data:
        return jsonify ({
            'success':False,
            'error':'No data provided'
        })
    
    if not data.get('email') or not data.get('password'):
        return jsonify({
            'success': False,
            'error': 'Email and password required'
        }), 400

    existing_user = User.query.filter_by(email=data.get('email')).first()
    if existing_user:
        return jsonify({
            'success': False,
            'error': 'User already exists'
        }), 400
    
    password=generate_password_hash(data.get('password'))

    user=User(name=data.get('name'),email=data.get('email'),password=password)



    db.session.add(user)
    db.session.commit()

    return jsonify({
        'success':True,
        'massage':'Added successfully'
    }),201


@auth.route('/login',methods=['POST'])
def login():
    data=request.get_json()

    if not data:
        return jsonify({
            'success': False,
            'error': 'No data provided'
        }), 400

    password=data.get('password')
    email=data.get('email')

    user=User.query.filter_by(email=email).first()

    if not user or  not check_password_hash(user.password,password):
        return jsonify({
            'success':False,
            'error':'Invalide email or password'
        }),400
    
    token=generate_token(user.id)
    
    return jsonify({'message':'Login successfully',
                    'token':token
                    })
    


    
     