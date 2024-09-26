import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier as cuRF
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

model_file_path = 'trained_rf_model_pickel_cpu.pkl'
with open(model_file_path, 'rb') as model_file:
    loaded_rf_model = pickle.load(model_file)

# new_data = pd.read_csv('cleaned_heart_disease_data.csv')

# X_new = new_data.drop('HadHeartAttacks', axis=1)  
# X_new_cupy = X_new.values

# predictions_cupy = loaded_rf_model.predict(X_new_cupy)
# print(predictions_cupy)

#Archit DATA
single_sample = np.array([0, 4, 1.829, 78, 1, 0, 0, 0, 0, 0, 0, 0])
single_sample_reshaped = single_sample.reshape(1, -1)
predicted_output = loaded_rf_model.predict(single_sample_reshaped)
print("Predicted Output:", predicted_output)