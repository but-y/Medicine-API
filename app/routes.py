from flask import Blueprint, jsonify, request
import json
import os

medicine_bp = Blueprint('medicine_bp', __name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@medicine_bp.route('/api/medicines', methods=['GET'])
def get_all_medicines():
    return jsonify(load_data())

@medicine_bp.route('/api/medicines/<string:name>', methods=['GET'])
def get_medicine_by_name(name):
    meds = load_data()
    for m in meds:
        if m['name'].lower() == name.lower():
            return jsonify(m)
    return jsonify({'error': 'Medicine not found'}), 404

@medicine_bp.route('/api/search', methods=['GET'])
def search_medicines():
    query = request.args.get('q', '').lower()
    results = [m for m in load_data() if query in m['name'].lower()]
    return jsonify(results)

@medicine_bp.route('/api/medicines', methods=['POST'])
def add_medicine():
    data = request.get_json()
    meds = load_data()
    meds.append(data)
    save_data(meds)
    return jsonify({'message': 'Medicine added successfully'}), 201

@medicine_bp.route('/api/medicines/<string:name>', methods=['PUT'])
def update_medicine(name):
    data = request.get_json()
    meds = load_data()
    for i, m in enumerate(meds):
        if m['name'].lower() == name.lower():
            meds[i].update(data)
            save_data(meds)
            return jsonify({'message': 'Medicine updated'})
    return jsonify({'error': 'Medicine not found'}), 404

@medicine_bp.route('/api/medicines/<string:name>', methods=['DELETE'])
def delete_medicine(name):
    meds = load_data()
    new_meds = [m for m in meds if m['name'].lower() != name.lower()]
    if len(new_meds) == len(meds):
        return jsonify({'error': 'Medicine not found'}), 404
    save_data(new_meds)
    return jsonify({'message': 'Medicine deleted'})
