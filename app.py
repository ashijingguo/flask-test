from flask import Flask, render_template, request, jsonify
import json
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    service = request.args.get('service')
    with open('config.json', 'r') as f:
        data = json.load(f)
    print(data)
    res = requests.get(data.get(service))

    return f'服务{service}访问成功了,返回结果是{res.text}'


@app.route('/info')
def info():
    with open('info.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')