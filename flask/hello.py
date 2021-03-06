from flask import Flask
from flask import request
from flask_cors import CORS
from data_analysis import analyze
from basic_dtw import get_dtw
import numpy as np

app = Flask(__name__)
CORS(app, origins="*", allow_headers=[
        "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
        supports_credentials=True)


@app.route("/", methods=['GET', 'POST'])
def hello():
    result = str(analyze("yo", "test.json"))
    return "The model returned: " + result


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            jsondata = request.get_json()
            print(jsondata)
            filename = jsondata['filename']
            data = jsondata['data']
            result = str(analyze(data, filename))

        except ValueError:
            return jsonify("Please send only valid JSONs including Myo IMU data")

        return jsonify({"score": result})
