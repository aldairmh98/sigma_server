from flask import Flask, jsonify
from flask import request
import os
from pyfcm import FCMNotification
import crud
from flask_cors import CORS
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return 'Hello world'

@app.route("/vitalData", methods=["POST", "GET"])
def vitalData():
    if request.method == "POST":
        content = request.json
        crud.saveVitalData(content)
        response = jsonify(content)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif request.method == "GET":
        response = jsonify(crud.getVitalData())
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/vitalData/id/<id>', methods=["GET"])
def vitalDataId(id):
    id_ = request.view_args['id']
    print(id_)
    response = jsonify(crud.getVitalDataUser(id_))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/incidents', methods = ["GET"])
def incidentsList():
    response = jsonify(crud.getIncidents())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/incident/<user_id>', methods=["POST"])
def incidents(user_id):
    # SEARCH FOR USER, SEND NOTIFICATION AND SEND INFORMATION
    #AIzaSyBzu6jeeyGabLpGPj7KutBzR-BmXwsMcrc
    #Expected Input = {USER_ID, LOCATION{latitude, longitude}}
    id = request.view_args['user_id']
    
    crud.createIncident(request.json, id )
    push_service = FCMNotification(api_key="AIzaSyBzu6jeeyGabLpGPj7KutBzR-BmXwsMcrc")
    result = push_service.notify_topic_subscribers(topic_name="covadonga", message_body='Alerta!')
    response = jsonify({'prueba':'pruebita'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')