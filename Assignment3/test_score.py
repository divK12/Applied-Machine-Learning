import pytest
from Assignment3.score import score

import pickle
import requests
import os
import time
import subprocess
import warnings
warnings.filterwarnings("ignore")


model = pickle.load(open(r"E:\Downloads\model.pkl", "rb"))


def test_smoke_test():
    result = score("Example", model, 0.5)
    assert isinstance(result, tuple) and len(result) == 2, "Smoke test failed"

def test_format_test():
    text = "Meeting rescheduled to 3 PM"
    threshold = 0.6
    prediction, probability = score(text, model, threshold)
    assert type(prediction) == int
    
    try:
        float(probability)
    except Exception as e:
        pytest.fail(f"score function raised an exception: {e} (Format test failed)")

def test_prediction_0_or_1():
    text = "Reminder: Your bill is due tomorrow"
    threshold = 0.6
    prediction, _ = score(text, model, threshold)
    assert prediction in (0, 1)

def test_propensity_between_0_and_1():
    text = "Win a free trip by clicking the link below!"
    threshold = 0.6
    _, propensity = score(text, model, threshold)
    assert 0<=propensity<=1

def test_when_threshold_0_prediction_always_1():
    text_1 = "Get 50% off on your next purchase!"
    threshold = 0
    prediction, _ = score(text_1, model, threshold)
    assert prediction == 1
    
    text_2 = "Exclusive deal just for you!"
    threshold = 0
    prediction, _ = score(text_2, model, threshold)
    assert prediction == 1

def test_when_threshold_1_prediction_always_0():
    text_1 = "Reminder: Your appointment is scheduled for tomorrow."
    threshold = 1
    prediction, _ = score(text_1, model, threshold)
    assert prediction == 0
    
    text_2 = "Please review the attached document."
    threshold = 1
    prediction, _ = score(text_2, model, threshold)
    assert prediction == 0

def test_obvious_spam_gives_prediction_1():
    text = "Congratulations! You have won a brand-new car. Click the link to claim now."
    threshold = 0.7
    prediction, _ = score(text, model, threshold)
    assert prediction == 1

def test_obvious_non_spam_gives_prediction_0():
    text = "Don't forget to submit your report by the end of the day."
    threshold = 0.4
    prediction, _ = score(text, model, threshold)
    assert prediction == 0


def test_flask():

    process = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE)

    time.sleep(2)

    payload = {"text": "Hello, congratulations! You have won a prize."}
    response = requests.post("http://127.0.0.1:5000/score", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert 'prediction' in data
    assert 'propensity' in data

    process.terminate()