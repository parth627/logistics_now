# Implement a POST, GET, DELETE API to fetch the data from the database.

from flask import Flask, make_response
import time
import datetime
import logging
import json

app = Flask(__name__)

HOST = "127.0.0.1"
PORT = 5000
EVENT_COUNT = 5
GLOBAL_DATA = [
        {
            "id": i,
            "created_at": datetime.datetime.utcnow().isoformat("T","seconds") + "Z",
            "event_category":"Logistics",
            "company_name":"LogisticsNow",
        }
        for i in range(EVENT_COUNT)
    ]

# GET
@app.route('/')
@app.route('/get_events', methods=['GET'])                                   
def get_events():
    global GLOBAL_DATA
    return send_response(GLOBAL_DATA)

# POST
@app.route('/post_events', methods=['POST'])
def post_events():
    new_event = {
        "id": len(GLOBAL_DATA),
        "created_at":datetime.datetime.utcnow().isoformat("T","seconds") + "Z",
        "event_category":"Logistics",
        "company_name":"LogisticsNow",
    }
    GLOBAL_DATA.append(new_event)
    return send_response(GLOBAL_DATA)

# DELETE
@app.route('/delete_events/<int:id>', methods=['DELETE'])
def delete_events(id):
    global GLOBAL_DATA
    GLOBAL_DATA = [event for event in GLOBAL_DATA if event['id'] != id]
    return send_response(GLOBAL_DATA)


def send_response(response):
    resp = make_response(json.dumps(response), 200)
    time.sleep(1)
    return resp

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s in %(module)s:%(lineno)d - %(message)s')
    app.run(host=HOST,port=PORT,debug=True)