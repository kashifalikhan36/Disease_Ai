import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier as cuRF
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class Heart():
    def __init__(self):
        self.model_file_path = 'trained_rf_model_pickel_cpu.pkl'

    def Model(self,data):
        with open(self.model_file_path, 'rb') as model_file:
            loaded_rf_model = pickle.load(model_file)
        physical_health_days = data['data']['PhysicalHealthDays']
        sleep_hours = data['data']['SleepHours']
        height_in_meters = data['data']['HeightInMeters']
        weight_in_kilograms = data['data']['WeightInKilograms']
        gender = data['data']['Gender']
        physical_activitie = data['data']['PhysicalActivitie']
        had_strokes = data['data']['HadStrokes']
        had_diabetess = data['data']['HadDiabetess']
        had_depressive_disorders = data['data']['HadDepressiveDisorders']
        alcohol_drinker = data['data']['AlcoholDrinker']
        high_risk_last_years = data['data']['HighRiskLastYears']
        covid_posi = data['data']['CovidPosi']
        single_sample = np.array([physical_health_days, sleep_hours, height_in_meters, weight_in_kilograms, gender, physical_activitie, had_strokes, had_diabetess, had_depressive_disorders, alcohol_drinker, high_risk_last_years, covid_posi])
        single_sample_reshaped = single_sample.reshape(1, -1)
        predicted_output = loaded_rf_model.predict(single_sample_reshaped)
        print("Predicted Output:", predicted_output)
        return predicted_output
    #Archit DATA