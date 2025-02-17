from flask import Flask, request, jsonify
import pickle
import json
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load pre-trained modelvs
models = {
    'random_forest': pickle.load(open('models/aml_random_forest.pkl', 'rb')),
    'logistic_regression': pickle.load(open('models/aml_logistic_regression.pkl', 'rb')),
    'svm': pickle.load(open('models/aml_svm.pkl', 'rb')),
    'xgboost': pickle.load(open('models/aml_xgboost.pkl', 'rb')),
    'neural_network': pickle.load(open('models/aml_neural_network.pkl', 'rb'))  # scikit-learn MLPClassifier
}

# Load model metadata
metadata = {
    'random_forest': json.load(open('models/aml_random_forest_meta.json')),
    'logistic_regression': json.load(open('models/aml_logistic_regression_meta.json')),
    'svm': json.load(open('models/aml_svm_meta.json')),
    'xgboost': json.load(open('models/aml_xgboost_meta.json')),
    'neural_network': json.load(open('models/aml_neural_network_meta.json'))
}

# Load transaction data
transactions = pd.read_csv('SAML-D.csv')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    model_name = data.get('model', 'random_forest')
    transaction = np.array(data['transaction']).reshape(1, -1)
    
    if model_name == 'neural_network':
        prediction = models[model_name].predict(transaction)
    else:
        prediction = models[model_name].predict(transaction)
    
    return jsonify({'prediction': prediction.tolist()})

@app.route('/model_metadata', methods=['GET'])
def get_model_metadata():
    model_name = request.args.get('model', 'random_forest')
    return jsonify(metadata.get(model_name, 'Model metadata not found'))

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return transactions.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
