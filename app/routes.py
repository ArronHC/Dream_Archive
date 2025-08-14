# app/routes.py

from flask import current_app as app, jsonify, request
from .models import db, User, Dream

@app.route('/')
def index():
    return 'Welcome to Dream Archive!'

@app.route('/api/dreams', methods=['POST'])
def create_dream():
    data = request.get_json()
    # Simple example, assumes user_id is provided
    new_dream = Dream(content=data['content'], user_id=data['user_id'])
    db.session.add(new_dream)
    db.session.commit()
    return jsonify({'message': 'Dream saved!'}), 201
