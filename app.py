from dotenv import load_dotenv
load_dotenv()
from flask import Flask,jsonify
from config import Config
from extensions import db
from routes.auth import auth
from routes.task import tasks

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(tasks)


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success':False,
        'error':'Not found'
    }),404


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'success':False,
        'error':'Internal server error'
    }),500


with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=Config.DEBUG)