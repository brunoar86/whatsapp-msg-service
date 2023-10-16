from flask import Flask, request, render_template
from flask_cors import CORS
import json
import os
from datetime import datetime
from bson import ObjectId
import formatCelNumbers
import whatsappApi

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
CORS(app)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    PHONE_NUMBER_ID = os.environ.get('PHONE_NUMBER_ID', 'default-phone-id')
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN', 'default-bearer-token')

app.config.from_object(Config)

@app.route('/send_msg_to_all', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message', '')
        secret_key = request.form.get('secret_key', '')
        phone_number_id = request.form.get('phone_number_id', '')
        bearer_token = request.form.get('bearer_token', '')
        xlsx_file = request.form.get('xlsx_file', '')

        app.config['SECRET_KEY'] = secret_key
        app.config['PHONE_NUMBER_ID'] = phone_number_id
        app.config['BEARER_TOKEN'] = bearer_token

        formatCelNumbers.loadData(xlsx_file)
        whatsappApi.send_msg_to_all(message)

        return "Mensagens enviadas com sucesso!"

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
