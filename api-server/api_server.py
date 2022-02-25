import flask
import pymongo
from flask import request, jsonify
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["api-server"]
mycol = mydb["calcs"]

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hour', methods=['GET'])
def api_hour():
    return jsonify(datetime.utcnow())


@app.route('/calc', methods=['POST'])
def calc():
    if 'num1' in request.args:
        num1 = int(request.args['num1'])
    else:
        return "Error: No num1 field provided. Please specify num1"

    if 'num2' in request.args:
        num2 = int(request.args['num2'])
    else:
        return "Error: No num2 field provided. Please specify num2"

    if 'operator' in request.args:
        operator = request.args['operator']
    else:
        return "Error: No operator field provided. Please specify operator"

    if operator == "sum":
        result_sum = num1 + num2
    elif operator == "product":
        result_sum = num1 * num2
    else:
        return "Error: No operator isn't product or sum"

    mydict = {"calc": result_sum}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    return jsonify(result_sum)


app.run()
