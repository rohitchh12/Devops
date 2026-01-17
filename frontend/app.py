from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import pymongo
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['flask-api']

app = Flask(__name__)


@app.route("/" , methods = ["GET"])

def get_home():
    return render_template('index.html')


@app.route("/submit", methods = ["POST"])
def submit():
    form_data = dict(request.form)
    error_message = None
    print(form_data)
    try:
        collection.insert_one(form_data)
    except Exception as e:
        error_message = str(e)

    if error_message:
        return error_message

    return "Data Submitted Succesfully"

if __name__ == "__main__":
    app.run(debug=True)

