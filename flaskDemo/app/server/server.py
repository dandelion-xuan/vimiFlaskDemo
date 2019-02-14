import api.test
from flask import Flask

app = Flask(__name__)
app.register_blueprint(api.test.test_api)