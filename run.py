import os
from extensions import db
from app import app

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))