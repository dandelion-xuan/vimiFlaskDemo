from server.server import app
from flask import Blueprint,send_file

test_api = flask.Blueprint('test', __name__, url_prefix='/test')

@app.route('/')
def hello_world():
    return 'Hello World!'

@test_api.route('/test/')
def test():
	return send_file("../../app/test.html")