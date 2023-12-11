#!/usr/bin/python3
""" Index view
"""
from flask import jsonify, Blueprint

from api.v1.views import app_views


bp = Blueprint('api', __name__, '/api/v1')

@app_views.route('status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
