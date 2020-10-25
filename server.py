#!/usr/bin/env python3
import webtech
from flask import Flask, request, abort, jsonify
import json

# you can use options, same as from the command line
wt = webtech.WebTech(options={'json': True})

app = Flask(__name__)

@app.route("/process", methods = ['POST'])
def process():

    if 'url' not in request.args or len(request.args['url']) <= 0:
        return abort(404)
    
    if not request.data:
        return abort(404)
    
    url = request.args['url']
    report = wt.start_from_data(url, request.data.decode(encoding="ISO-8859-1"))
    response = jsonify(report['tech'])
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run(port=5891)
