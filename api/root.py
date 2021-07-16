
from flask import Blueprint, jsonify
from models import RootFetch

__all__ = [
    'root_page'
]

root_page = Blueprint('root_page', __name__)


@root_page.route('/')
def home():
    return {
        "msg": "Connection Successful"
    }


@root_page.route('/dump')
def about():
    data = RootFetch().get()
    return jsonify(data)
    # return r
