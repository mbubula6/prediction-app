import os
import sys
import pickle
import hashlib
import threading
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Setup Django Environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prediction_project.settings')

import django
django.setup()

from app.models import UserInput
from django.contrib.auth.models import User

MODELS_DIR = os.path.join(BASE_DIR, 'app', 'ml_models')
os.makedirs(MODELS_DIR, exist_ok=True)

def mock_hash(string_val):
    if not string_val: return 0.5
    return int(hashlib.md5(str(string_val).lower().encode()).hexdigest()[:8], 16) / 4294967295.0

def extract_features_and_labels(queryset):
    """
    Converts a Django QuerySet into X and y arrays.
    Returns X, y. If less than 1 row, returns None, None.
    """
    if queryset.count() < 1:
        return None, None
        
    X = []
    y = [] # 0: Low Energy, 1: High Motivation, 2: Creative
    for entry in queryset:
        features = [
            mock_hash(entry.current_intent),
            mock_hash(entry.sleep_quality),
            mock_hash(entry.previous_action) + mock_hash(entry.device_type), 
            mock_hash(entry.action_3_hours_ago),
            mock_hash(entry.gender) + mock_hash(entry.os)
        ]
        X.append(features)
        
        # Super simple simulated label generation based on what they actually submitted.
        # In a real app, 'label' would be derived from a "How did you actually feel?" post-survey.
        # For prototype purposes, we map certain phrases to arbitrary states to show it trains.
        state_str = str(entry.current_intent).lower()
        if 'sleep' in state_str or 'rest' in state_str:
            y.append(0)
        elif 'work' in state_str or 'code' in state_str or 'study' in state_str:
            y.append(1)
        else:
            y.append(2)
            
    return np.array(X), np.array(y)

def train_and_save(X, y, model_name):
    rf = RandomForestClassifier(n_estimators=10, random_state=42)
    rf.fit(X, y)
    with open(os.path.join(MODELS_DIR, f"{model_name}.pkl"), 'wb') as f:
        pickle.dump(rf, f)
    print(f"Successfully trained {model_name}.pkl")

def retrain_models():
    print("Fetching History for Real Data ML Training...")
    
    # 1. Global Model
    all_data = UserInput.objects.all()
    X_global, y_global = extract_features_and_labels(all_data)
    
    if X_global is not None:
        print(f"Training Global Model on {len(y_global)} entries...")
        train_and_save(X_global, y_global, 'global_model')
    else:
        print("Not enough global data! Generating fallback synthetic model...")
        np.random.seed(42)
        X_sync = np.random.rand(100, 5)
        y_sync = np.random.randint(0, 3, 100)
        train_and_save(X_sync, y_sync, 'global_model')

    # 2. Daily Personal Models
    for user in User.objects.all():
        user_data = UserInput.objects.filter(user=user)
        X_user, y_user = extract_features_and_labels(user_data)
        
        if X_user is not None:
            print(f"Training Personal Model for {user.username} ({len(y_user)} entries)...")
            train_and_save(X_user, y_user, f'personal_{user.id}')
        else:
            print(f"Not enough data for {user.username}. They will fall back to Global model logic automatically.")

def get_prediction(model_name, features):
    model_path = os.path.join(MODELS_DIR, f"{model_name}.pkl")
    
    # Fallback to global model if personal model doesn't exist yet
    if not os.path.exists(model_path):
        model_path = os.path.join(MODELS_DIR, "global_model.pkl")
        if not os.path.exists(model_path):
            return 0 # Absolute fallback
            
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        
    X_pred = np.array(features).reshape(1, -1)
    prediction = model.predict(X_pred)
    
    if hasattr(prediction, '__len__'):
        return int(prediction[0])
    return int(prediction)

if __name__ == "__main__":
    retrain_models()
