from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Room, Item

app = Flask(__name__, static_folder='../static/dist', template_folder='../templates')

engine = create_engine('sqlite:///ItemCatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
    app.debug = True
