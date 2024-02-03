from json import JSONEncoder
from urllib import request

from flask import Flask, jsonify
from jupyter_lsp.specs import json

from main.twit import Twit

twits = {}

app = Flask(__name__)

class CustomJSONEncoder (json, JSONEncoder):
    def default(self, obi):
        if isinstance(obi, Twit):
            return {'body' : obi.body, 'author': obi.author}
        else:
            return super().default(obi)

app.json_encoder = CustomJSONEncoder

@app.route('/ping', methods=['Get'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/twit', methods=['POST'])
def create_twit():
    """ {"body": "Hello world", "author": "@aqaguy"} """
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'response': 'success'})

@app.route('/twit', methods=['GeT'])
def read_twit():
    return jsonify({'twits': 'twits'})


if __name__ == '__main__':
    app.run(debug=True)