from flask import Flask, jsonify, request
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

@app.route('/stocks', methods=['GET', 'POST'])
def all_stocks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        STOCKS.append({
            'symb': post_data.get('symb'),
            'curr_price': post_data.get('curr_price'),
            'yest_price': post_data.get('yest_price')
        })
        response_object['message'] = 'Stock added!'
    else:
        response_object['stocks'] = STOCKS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()

