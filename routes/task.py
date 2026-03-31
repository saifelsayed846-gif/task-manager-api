from flask import Blueprint,jsonify,request
from extensions import db
from utils.decorator import token_required
from models.task import Task


tasks=Blueprint('tasks',__name__)

@tasks.route('/task',methods=['POST'])
@token_required
def add_task(user_id):
    data=request.get_json()

    if not data :
        return jsonify ({
            'success':False,
            'error':'NO data provided'
        }),400

    if not data.get('task'):
        return jsonify({
            'success':False,
            'error':'Task is requirded'
        }),400

    task=Task(
        task=data.get('task'),
        status=data.get('status'),
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify ({
        'success':True,
        'message':'add successfully'
    }),201


@tasks.route('/task',methods=['GET'])
@token_required
def get_tasks(user_id):


    page=request.args.get('page',1,type=int)
    per_page=request.args.get('per_page',4,type=int)

    tasks=Task.query.filter_by(user_id=user_id).paginate(
        page=page,
        per_page=per_page
    )

    result=[]

    for task in tasks.items:
        result.append(
            {
                "id":task.id,
                "task":task.task,
                "status":task.status
            }
        )

    return jsonify({
        'tasks':result,
        'total':tasks.total,
        'pages':tasks.pages,
        'page':tasks.page
    }),200


@tasks.route('/task/<int:task_id>',methods=['PUT'])
@token_required
def update_task(user_id,task_id):

    data=request.get_json()

    task=Task.query.get(task_id)

    if not task or task.user_id != user_id :
        return jsonify ({
            'success':False,
            'error':'Task is not found'
        }),404


    task.task=data.get('task')
    task.status=data.get('status')

    db.session.commit()

    return jsonify ({
        'success':True,
        'message':'Updated successfully'
    })


@tasks.route('/task/<int:task_id>',methods=['DELETE'])
@token_required
def delete_task(user_id,task_id):

    task=Task.query.get(task_id)

    if not task or task.user_id != user_id :
        return jsonify ({
            'success':False,
            'error':'Task is already not found'
        }),404
    
    db.session.delete(task)
    db.session.commit()

    return jsonify ({
        'success':True,
        'message':'Deleted successfully'
    })








