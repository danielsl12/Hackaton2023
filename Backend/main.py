from flask import Flask, request, jsonify
import hf_test

app = Flask(__name__)

@app.route('/api/get-guide', methods=['POST'])
def get_guide():
    print('MATAN: ', request.get_json())
    data = request.get_json()
    input_string = data['task']
    return jsonify({'reply': hf_test.retrieve_document(input_string)})

if __name__ == '__main__':
    app.run(debug=True)