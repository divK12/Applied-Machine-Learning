from flask import Flask, request, jsonify, render_template_string
import pickle
from score import score
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load model
model = pickle.load(open(r"E:\Downloads\model.pkl", "rb"))

DEFAULT_THRESHOLD = 0.5  # Default threshold for classification

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        prediction, probability = score(text, model, 0.55)

        return jsonify({"prediction": prediction, "propensity": probability})

    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Spam Classifier</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    flex-direction: column;
                }
                h1 {
                    text-align: center;
                    margin-top: 20px;
                }
                form {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Spam Classifier</h1>
            <form action="/" method="post">
                <label for="text">Enter Text:</label><br>
                <input type="text" id="text" name="text"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    """

@app.route("/score", methods=["POST"])
def score_text():
    """API Endpoint for Scoring"""
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing text in request body"}), 400

    text = data["text"]
    threshold = data.get("threshold", DEFAULT_THRESHOLD)

    prediction, probability = score(text, model, threshold)

    return jsonify({"prediction": prediction, "propensity": probability})

if __name__ == "__main__":
    app.run(debug=True)