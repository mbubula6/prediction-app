import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import xgboost as xgb

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'ml_models')

# Create ml_models directory if it doesn't exist
os.makedirs(MODELS_DIR, exist_ok=True)

def train_dummy_models():
    print("Generating synthetic data...")
    # 5 dummy features: Time_of_day_hash, sleep_quality_mapping, intent_hash, prior_hash, gender_hash
    np.random.seed(42)
    X = np.random.rand(200, 5)
    # Target classes: 0, 1, 2 representing 3 behavioral states
    y = np.random.randint(0, 3, 200)

    print("Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=10)
    rf.fit(X, y)
    with open(os.path.join(MODELS_DIR, 'random_forest.pkl'), 'wb') as f:
        pickle.dump(rf, f)

    print("Training Logistic Regression...")
    lr = LogisticRegression(max_iter=100)
    lr.fit(X, y)
    with open(os.path.join(MODELS_DIR, 'logistic_regression.pkl'), 'wb') as f:
        pickle.dump(lr, f)

    print("Training Classifier (SVC)...")
    svc = SVC(probability=True)
    svc.fit(X, y)
    with open(os.path.join(MODELS_DIR, 'classifier.pkl'), 'wb') as f:
        pickle.dump(svc, f)

    print("Training XGBoost...")
    xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    xgb_model.fit(X, y)
    with open(os.path.join(MODELS_DIR, 'xgboost.pkl'), 'wb') as f:
        pickle.dump(xgb_model, f)

    print("All dummy models successfully trained and saved to ml_models/.")

def get_prediction(model_name, features):
    """
    Load the specified model and make a prediction.
    Features should be a 1D array/list of length 5.
    """
    model_path = os.path.join(MODELS_DIR, f"{model_name}.pkl")
    if not os.path.exists(model_path):
        return 0 # Default fallback
        
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        
    X_pred = np.array(features).reshape(1, -1)
    prediction = model.predict(X_pred)
    
    # Extract prediction value
    if hasattr(prediction, '__len__'):
        return int(prediction[0])
    return int(prediction)

if __name__ == "__main__":
    train_dummy_models()
