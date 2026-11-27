
# 🛡️ ScamShield

### AI-Powered SMS Spam Detection System

ScamShield is a machine learning-based application that classifies SMS messages as Spam or Ham (Not Spam).

## Features
- SMS spam detection
- TF-IDF text vectorization
- Logistic Regression classification
- Confidence score display
- Interactive Gradio web interface

## Technology Stack
- Python
- Pandas and NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Gradio

## Model Performance
- Accuracy: 97.78%
- Spam Precision: 94%
- Spam Recall: 89%
- Spam F1-score: 91%

## Dataset
SMS Spam Collection Dataset from Kaggle.

## Project Structure

```text
ScamShield/
├── data/
├── models/
├── src/
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
python app.py
```

## Disclaimer
This project is an educational spam detection tool. Predictions may be incorrect and should not be treated as proof that a message is safe.
