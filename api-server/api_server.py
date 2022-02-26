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
        result_calc = num1 + num2
    elif operator == "product":
        result_calc = num1 * num2
    else:
        return "Error: No operator isn't product or sum"

    mydict = {"calc": result_calc}
    fnd = 0
    for document in mycol.find(mydict):
        fnd = document['calc']
    if fnd != result_calc:
        mycol.insert_one(mydict)

    return jsonify(result_calc)


@app.route('/list', methods=['POST'])
def list_calc():
    if 'del' in request.args:
        del_result = int(request.args['del'])
        mycol.delete_one({"calc": del_result})
        return "deleted " + str(del_result)
    else:
        col_list = []
        for document in mycol.find():
            col_list.append(document['calc'])
        return jsonify(col_list)


app.run()
