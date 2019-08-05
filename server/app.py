from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

STOCKS = [
    {
        'symb': 'ABCD',
        'curr_price': 25.03,
        'yest_price': 25.03
    },
    {
        'symb': 'ABCD',
        'curr_price': 30.01,
        'yest_price': 25.03
    },
    {
        'symb': 'ABCD',
        'curr_price': 20.01,
        'yest_price': 25.03
    }
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/stocks', methods=['GET'])
def all_stocks():
    return jsonify({
        'status': 'success',
        'stocks': STOCKS
    })


if __name__ == '__main__':
    app.run()

