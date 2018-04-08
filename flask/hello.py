from flask import Flask
from flask_cors import CORS
# from data_analysis import analyze
# from sklearn.externals import joblib

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
# app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, origins="*", allow_headers=[
        "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
        supports_credentials=True)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()

            # lin_reg = joblib.load("../data/linear_regression_model.pkl")

        except ValueError:
            return jsonify("Please send only valid JSONs from Myo IMU data")

        # return jsonify(lin_reg.predict(years_of_experience).tolist())
        return jsonify({"score": "Don't quit your day job"})
