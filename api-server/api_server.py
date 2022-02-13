import flask
from flask import request, jsonify
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hour', methods=['GET'])
def api_hour():
    return jsonify(datetime.utcnow())


@app.route('/sum', methods=['POST'])
def calc_sum():
    if 'num1' in request.args:
        num1 = int(request.args['num1'])
    else:
        return "<h1>Error: No num1 field provided. Please specify num1.</h1>"

    if 'num2' in request.args:
        num2 = int(request.args['num2'])
    else:
        return "<h1>Error: No num2 field provided. Please specify num2.</h1>"

    result_sum = num1 + num2

    return jsonify(result_sum)


app.run()
