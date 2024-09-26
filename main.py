import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier as cuRF
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the model
model_file_path = 'trained_rf_model_pickel.pkl'
with open(model_file_path, 'rb') as model_file:
    loaded_rf_model = pickle.load(model_file)

# Load your new data for prediction (assuming it's a CSV file)
new_data = pd.read_csv('cleaned_heart_disease_data.csv')

# Preprocess new data
X_new = new_data.drop('HadHeartAttacks', axis=1)  # Ensure to drop the target column
# Convert to CuPy array for compatibility with cuML
X_new_cupy = X_new.values

# Make predictions using the loaded model
predictions_cupy = loaded_rf_model.predict(X_new_cupy)
print(predictions_cupy)
