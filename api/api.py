import flask
from flask import request, jsonify
from datetime import datetime


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/hour', methods=['GET'])
def api_all():
    return jsonify(datetime.utcnow())


app.run()
