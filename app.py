import json
from flask import Flask, request,make_response
from flask_sqlalchemy import  SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80),unique=True,nullable=True)
    name=db.Column(db.String(50))
    password=db.Column(db.String(80))


class Todo(db.Model):
    text = db.Column(db.String(50))
    user_email=db.Column(db.String(50),primary_key=True)

@app.route('/user/<email>',methods=['GET'])
def get_user(email):
    email=request.form.get(email)
    user=User.query.filter_by(email=email).first()

    if  not user:
        return make_response({'Message':'User not found'})

    data = request.get_json()
    name=data['name']
    password=data['password']
    return make_response({'name':name,'password':password})

@app.route('/user',methods=['POST'])
def create_user():
    data=request.get_json()
    password =data['password']
    email=data['email']
    new_user=data['name']

    return make_response({'message':'New User Created'})


if __name__ ==  '__main__':
    app.run(debug=True)
