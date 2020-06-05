from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib

flask_app = Flask(__name__)

app = Api(app = flask_app,
          version = "1.0",
          title = "Covid machine learning app",
          description = "")
