from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/intdata/<int:value>', methods=["GET"])
def intdata(value):
    eveness = False
    if(value % 2 == 0):
        eveness = True
    return_data = {"even": eveness, "inverted": -value}
    return jsonify(return_data)

