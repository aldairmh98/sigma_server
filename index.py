from flask import Flask, jsonify
from flask import request
import os
from pyfcm import FCMNotification


app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello world'

@app.route("/vitalData", methods=["POST", "GET"])
def vitalData():
    if request.method == "POST":
        content = request.json
        print(content['colonies'])
        response = jsonify({'Chale': 'Chalecos'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif request.method == "GET":
        data = [
            {
                'name': 'Aldair'
            }
        ]
        return jsonify({'datos': data})

@app.route('/vitalData/id/<id>', methods=["GET"])
def vitalDataId(id):
    print(request.view_args['id'])
    return "Hi"

@app.route('/incident/<user_id>', methods=["POST"])
def incidents(user_id):
    # SEARCH FOR USER, SEND NOTIFICATION AND SEND INFORMATION
    #AIzaSyBzu6jeeyGabLpGPj7KutBzR-BmXwsMcrc
    #Expected Input = {USER_ID, LOCATION{latitude, longitude}}
    push_service = FCMNotification(api_key="AIzaSyBzu6jeeyGabLpGPj7KutBzR-BmXwsMcrc")
    result = push_service.notify_topic_subscribers(topic_name="covadonga", message_body='hetmm')
    return "HEY"

if __name__ == '__main__':
    app.run(debug=True)