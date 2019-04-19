import validators
from flask import Flask, request
from sqlalchemy import create_engine, Column, Table, String, MetaData, Integer

app = Flask(__name__)
engine = create_engine('sqlite:///:memory:', echo=True)

def validate_url(url):
    pass

@app.route('/')
def index():
    return "<h1>Shorter URL</h1>"

@app.route('/shorter', methods=['POST'])
def shorter():
    # get the url
    url = request.args.get('url', '')

    # validate the url
    if not validators.url(url):
        return 'Invalid url'
    
    # register the url on database

    # return the shorter link
    return 'testng..'
