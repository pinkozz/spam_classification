import string
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def preprocessing(text=str):
  """Preprocess the text for better model performance"""
  # Make all characters lowercase
  text = text.lower()
  # Remove the punctuation
  text = text.translate(str.maketrans('', '', string.punctuation))
  # Simplify the words
  text = [stemmer.stem(word) for word in text.split()]
  # Put spaces between each character
  text = " ".join(text)
  return text