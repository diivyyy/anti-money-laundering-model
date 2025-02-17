import pandas as pd
import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.neural_network import MLPClassifier

# Load dataset
data = pd.read_csv('SAML-D.csv')

X = data[['Sender_account', 'Receiver_account', 'Amount', 'date', 'time']]  # Feature columns
y = data['Laundering_type']  # Target column

# Convert categorical features into numerical (if needed)
X = pd.get_dummies(X, columns=['Sender_account ', 'Receiver_account'], sparse=True)  # Use sparse=True to save memory

# Split dataset
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
pickle.dump(rf, open('models/aml_random_forest.pkl', 'wb'))

# Save Random Forest metadata
rf_metadata = {
    "model": "Random Forest",
    "training_accuracy": rf.score(X_train, y_train),
    "test_accuracy": rf.score(X_test, y_test),
    "feature_importances": rf.feature_importances_.tolist()
}
with open('models/aml_random_forest_meta.json', 'w') as f:
    json.dump(rf_metadata, f)

# Train Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
pickle.dump(lr, open('models/aml_logistic_regression.pkl', 'wb'))

# Save Logistic Regression metadata
lr_metadata = {
    "model": "Logistic Regression",
    "training_accuracy": lr.score(X_train, y_train),
    "test_accuracy": lr.score(X_test, y_test)
}
with open('models/aml_logistic_regression_meta.json', 'w') as f:
    json.dump(lr_metadata, f)

# Train SVM
svm = SVC(probability=True)
svm.fit(X_train, y_train)
pickle.dump(svm, open('models/aml_svm.pkl', 'wb'))

# Save SVM metadata
svm_metadata = {
    "model": "Support Vector Machine",
    "training_accuracy": svm.score(X_train, y_train),
    "test_accuracy": svm.score(X_test, y_test)
}
with open('models/aml_svm_meta.json', 'w') as f:
    json.dump(svm_metadata, f)

# Train XGBoost
xgboost = xgb.XGBClassifier()
xgboost.fit(X_train, y_train)
pickle.dump(xgboost, open('models/aml_xgboost.pkl', 'wb'))

# Save XGBoost metadata
xgboost_metadata = {
    "model": "XGBoost",
    "training_accuracy": xgboost.score(X_train, y_train),
    "test_accuracy": xgboost.score(X_test, y_test)
}
with open('models/aml_xgboost_meta.json', 'w') as f:
    json.dump(xgboost_metadata, f)

# scikit-learn MLPClassifier (Neural Network)
mlp = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500)
mlp.fit(X_train, y_train)
pickle.dump(mlp, open('models/aml_neural_network.pkl', 'wb'))

# Save MLPClassifier metadata
mlp_metadata = {
    "model": "MLPClassifier Neural Network",
    "training_accuracy": mlp.score(X_train, y_train),
    "test_accuracy": mlp.score(X_test, y_test)
}
with open('models/aml_neural_network_meta.json', 'w') as f:
    json.dump(mlp_metadata, f)
