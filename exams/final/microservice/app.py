from flask import Flask, jsonify

app = Flask(__name__)

VOTES = [
    {
        'post_id': 0,
        'vote_count': -1,
    },
    {
        'post_id': 1,
        'vote_count': 5,
    },
    {
        'post_id': 2,
        'vote_count': 42,
    },
]

@app.route('/api/votes', methods=['GET'])
def votes():
    return jsonify(VOTES)

@app.route('/api/votes/<int:id>', methods=['GET'])
def vote(id):
    return jsonify(VOTES[id])