import joblib
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from preprocessing import preprocessing

# Load the dataset
df = pd.read_csv("./datasets/spam.csv")

X = df['text']
y = (df['text_type'] == "spam").astype(int)

# Apply the preprocessing function
X.apply(preprocessing)

# Vectorize the data
vec = CountVectorizer()
X = vec.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
rfc = RandomForestClassifier(n_jobs=-1)
rfc.fit(X_train, y_train)

# joblib.dump(rfc, "./models/rfc.pkl")
# joblib.dump(vec, "./models/vec.pkl")