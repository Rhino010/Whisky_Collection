from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Whisky, whisky_schema, whiskies_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/whisky_item', methods = ['POST'])
@token_required
def input_whisky(current_user_token):
    brand = request.json['brand']
    country_state = request.json['country_state']
    batch = request.json['batch']
    proof = request.json['proof']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    whisky = Whisky(brand, country_state, batch, proof, user_token=user_token)

    db.session.add(whisky)
    db.session.commit()

    response = whisky_schema.dump(whisky)
    return jsonify(response)


@api.route('/whisky_item', methods = ['GET'])
@token_required
def retrieve_whiskies(current_user_token):
    a_user = current_user_token.token
    whiskies = Whisky.query.filter_by(user_token = a_user).all()
    response = whiskies_schema.dump(whiskies)
    return jsonify(response)

@api.route('/whisky_item/<id>', methods = ['GET'])
@token_required
def get_single_whisky(current_user_token, id):
    whisky = Whisky.query.get(id)
    response = whisky_schema.dump(whisky)
    return jsonify(response)

@api.route('/whisky_item/<id>', methods = ['POST', 'PUT'])
@token_required
def update_whisky(current_user_token, id):
    whisky = Whisky.query.get(id)
    whisky.brand = request.json['brand']
    whisky.country_state = request.json['country_state']
    whisky.batch = request.json['batch']
    whisky.proof = request.json['proof']

    db.session.commit()
    response = whisky_schema.dump(whisky)
    return jsonify(response)

@api.route('/whisky_item/<id>', methods = ['DELETE'])
@token_required
def delete_whisky(current_user_token, id):
    whisky = Whisky.query.get(id)
    db.session.delete(whisky)
    db.session.commit()
    response = whisky_schema.dump(whisky)
    return jsonify(response)


