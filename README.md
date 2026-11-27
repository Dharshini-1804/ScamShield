# 🛡️ ScamShield

### AI-Powered SMS Spam Detection System

ScamShield is a machine learning-based application that classifies SMS messages into two categories: **Spam** and **Ham (Not Spam)**.

It uses Natural Language Processing (NLP) and machine learning to identify suspicious SMS messages.

## 📸 Application Demo

![ScamShield Demo](Screenshot%202026-11-27%20153710.png)

## 🚀 Features

- SMS spam detection
- Text preprocessing using TF-IDF
- Logistic Regression classification
- Prediction confidence display
- Interactive Gradio web interface
- Sample messages for testing

## 🛠️ Technology Stack

- Python
- Pandas and NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Gradio

## 📊 Model Performance

The model was evaluated using a stratified 80:20 train-test split.

| Metric | Score |
|---|---:|
| Accuracy | 97.78% |
| Spam Precision | 94% |
| Spam Recall | 89% |
| Spam F1-score | 91% |

**Confusion Matrix**

```text
[[895   8]
 [ 15 116]]
```

## 📁 Project Structure

```text
ScamShield/
├── data/
│   └── spam.csv
├── models/
│   └── scamshield_model.pkl
├── src/
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 📚 Dataset

SMS Spam Collection Dataset from Kaggle.

Add the exact Kaggle dataset URL here.

## ⚙️ Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
python app.py
```

## ⚠️ Limitations

- The model was trained on an SMS spam dataset.
- It may not detect every phishing or scam message.
- Confidence scores are model estimates, not guarantees of correctness.
- Predictions should not be treated as proof that a message is safe.

## 🔮 Future Improvements

- Expand the dataset with more diverse scam messages.
- Test additional machine learning algorithms.
- Improve detection of phishing-related messages.
- Evaluate performance on unseen real-world messages.

## 👩‍💻 Author

Dharshini P J

B.Tech Artificial Intelligence and Data Science

