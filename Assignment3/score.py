# score.py
import sklearn
import numpy as np
import joblib

def score(text: str, model: sklearn.base.BaseEstimator, threshold: float) -> tuple:
    """
    Score a given text using a trained model and return prediction and propensity.
    
    Args:
        text (str): The text to be scored
        model (sklearn.estimator): Trained sklearn model
        threshold (float): Threshold for classification
        
    Returns:
        tuple: (prediction: bool, propensity: float)
    """
    # Get propensity score (probability of class 1)
    propensity = model.predict_proba([text])[0, 1]
        
    # Make prediction based on threshold
    if propensity >= threshold:
        prediction = 1
    else:
        prediction=0
    
    return prediction, propensity