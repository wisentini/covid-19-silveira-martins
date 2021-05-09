from flask import Flask
from flask import jsonify
from flask_cors import CORS

from main import web_scraper
from main import get_keys_from_json

app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False

data = web_scraper()


@app.route('/')
def index():
    return jsonify(data)


@app.route('/titles')
def get_titles():
    titles = get_keys_from_json('title', data)

    return jsonify(titles)


@app.route('/numbers')
def get_numbers():
    numbers = get_keys_from_json('number', data)

    return jsonify(numbers)


@app.route('/updates')
def get_updates():
    updates = get_keys_from_json('update', data)

    return jsonify(updates)


@app.route('/last-updated-date')
def get_last_updated_date():
    last_updated_date = get_keys_from_json('lastUpdatedDate', data)
    last_updated_date = last_updated_date[0]

    return jsonify(last_updated_date)
