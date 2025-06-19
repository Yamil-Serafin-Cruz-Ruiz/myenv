from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)
modelo = load('/modelobichos15.pkl')

@app.route('/')
def home():
    return "¡Hola, Mundo!"

@app.route('/predict', methods=['POST'])
def predict():
    datos = request.get_json()
    prediccion = modelo.predict([datos['features']])
    return jsonify({'resultado': int(prediccion[0])})

