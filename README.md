# Phishing Website Detection using Machine Learning

This project aims to detect phishing websites using machine learning algorithms to enhance online security. Phishing attacks trick users into revealing sensitive information by mimicking legitimate websites. Our model helps classify websites as phishing or legitimate based on various extracted features.

## 🔍 Features

- URL-based feature extraction
- Machine learning classifiers (KNN, XGBoost, Hybrid Model)
- Real-time prediction support
- Android + Cloud Integration (Optional)
- Achieved high accuracy in phishing detection

## 📁 Dataset

We used publicly available phishing datasets that contain both legitimate and phishing URLs. The features include URL length, presence of '@' symbol, use of HTTPS, subdomain count, etc.

## ⚙️ Algorithms Used

- **K-Nearest Neighbors (KNN)**
- **Extreme Gradient Boosting (XGBoost)**
- **Hybrid Model**: Combines KNN and XGBoost for improved accuracy

## 🏗️ Project Structure

├── dataset/
├── models/
├── android_app/
├── phishing_detection.py
├── requirements.txt
└── README.md

markdown
Copy
Edit

## 🚀 How to Run

1. Clone the repository:
git clone https://github.com/PranayGaddam0906/phishing-detection.git
cd phishing-detection

markdown
Copy
Edit

2. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

3. Run the detection script:
python phishing_detection.py

yaml
Copy
Edit

## 📱 Android Integration

An Android app can be connected to a cloud-based API to detect phishing links in real time from mobile devices.

## 📈 Results

- KNN Accuracy: 92.3%
- XGBoost Accuracy: 96.5%
- Hybrid Model Accuracy: 97.8%

