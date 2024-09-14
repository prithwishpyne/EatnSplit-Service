from flask import Flask, jsonify, request
from db import db
from flask_cors import CORS
import api_logic
import yaml

app = Flask(__name__)

with open("config.yaml","r") as file:
    try:
        config = yaml.safe_load(file)["db_creds"]
    except yaml.YAMLError as exc:
        print(exc)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eatnsplit.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/postgres'.format(config["username"], config["password"], config["url"], config["port"])
db.init_app(app)
# db = SQLAlchemy(app)
CORS(app)

with app.app_context():
    db.create_all()

@app.route('/v1/addUser', methods=['POST'])
def addUser():
    try:
        response={}
        obj = api_logic.EatNSplit()

        if request.method == 'POST':
            data = request.get_json()
            name = data['name']
            image = data['image']

            message = obj.addUser(name, image)

            response['status'] = 'SUCCESS'
            response['message'] = message

            return jsonify(response),200
    
    except Exception as e:
        response['status'] = 'FAILED'
        response['message'] = str(e)

@app.route('/v1/getAllUserDetails', methods=['GET'])
def getDetails():
    try:
        response = {}
        obj = api_logic.EatNSplit()

        if request.method == 'GET':
            data = obj.getDetails()

        response['status'] = 'SUCCESS'
        response['message'] = data

        return jsonify(response),200
    
    except Exception as e:
        response['status'] = 'FAILED'
        response['message'] = str(e)

@app.route('/v1/editBalance/<int:id>', methods=['POST'])
def editBalance(id):
    try:
        response = {}
        obj = api_logic.EatNSplit()

        if request.method == 'POST':
            data = request.get_json()
            newBalance = data["balance"]
            message = obj.editBalance(id, newBalance)

            response['status'] = 'SUCCESS'
            response['message'] = message

            return jsonify(response),200
    
    except Exception as e:
        response['status'] = 'FAILED'
        response['message'] = str(e)

            

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1200)
    app.debug = True
