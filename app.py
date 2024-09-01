from flask import Flask, request, render_template

import joblib
import pandas as pd
from preprocessing import preprocessing

app = Flask(__name__)

# Load the vectorizer
vec = joblib.load("./models/vec.pkl")
# Load the trained model
rfc = joblib.load("./models/rfc.pkl")

@app.route("/", methods=['GET'])
def index():
  return render_template("main.html")

@app.route("/", methods=['POST'])
def predict():
  data = request.form
  message = data['message']

  X = pd.DataFrame({
    "text": [message]
  })

  X['text'].apply(preprocessing)

  X = vec.transform(X['text'])

  prediction = rfc.predict(X)[0]

  if prediction == 1:
    prediction = "This message is spam."
  else:
    prediction = "This message is not spam."

  return render_template("main.html", message=message, prediction=prediction)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)