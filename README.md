## Spam Classification
An ML-integrated tool for classifying spam text from non-spam. Simply paste any text into the text area and click "submit". You will receive the prediction immediately, so give it a try!

https://github.com/user-attachments/assets/0e4a1046-7b5c-45ea-b639-c1062ce5c3a6

# Table of contents
• [Set Up](https://github.com/pinkozz/spam_classification#installation)

• [Usage](https://github.com/pinkozz/spam_classification#usage)

• [Contributing](https://github.com/pinkozz/spam_classification#contributing)


# Set up

!! Before starting the app on your machine, ensure you have Python3 installed !!

Clone the repository
```shell
git clone https://github.com/pinkozz/spam_classification
```

Navigate to project folder
```shell
cd spam_classification
```

Install requirements
```shell
pip3 install -r requirements.txt
```

(Optional) If you want to make changes to the model, make sure you run model.py once you're done. Don't forget to uncomment the following lines of code to reaplace old model with a new one:
```py
# joblib.dump(rfc, "./models/rfc.pkl")
# joblib.dump(vec, "./models/vec.pkl")
```

Run the app
```shell
python3 app.py
```

# Usage
Once the app is up and runnning, you can use it on your local machine http://localhost:3000.


# Contributing
Contributions to the repository are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Submit a pull request to the main repository.

Please ensure that your contributions align with the project's coding style, and guidelines.
