from flask import Flask, request,jsonify,make_response
from flask_sqlalchemy import  SQLAlchemy

app=Flask(__name__)

app.config['SECRET_KEY']='thisissecret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    password=db.Column(db.String(80))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    user_id= db.Column(db.Integer)

@app.route('/user',methods=['GET'])
def get_user():
    users=User.query.all()
    output=[]
    for user in users:
        user_data={}
        user_data['name']=user.name
        user_data['password'] = user.password
        output.append(user_data)
    return jsonify({'users':output})


@app.route('/user',methods=['POST'])
def create_user():
    data=request.get_json()
    password =data['password']
    new_user=User(name=data['name'],password=password)

    return jsonify({'message':'New User Created'})


if __name__ ==  '__main__':
    app.run(debug=True)