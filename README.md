❤️ MatchMakerAI

Predicting Relationship Status on OKCupid Using Machine Learning

📌 Project Overview

MatchMakerAI is a machine learning project designed to analyze user profile information from OKCupid to predict relationship status.
The goal is to provide insights that can improve matchmaking recommendations on dating platforms.

This project demonstrates skills in:

✔ Natural Language Processing
✔ Handling imbalanced data
✔ Classification modeling
✔ Data visualization
✔ Real-world evaluation techniques

🎯 Objective

Build a supervised ML model that predicts whether a user is:

single

not single (seeing someone / married)

Using:

Text essays (TF-IDF)

Age

Height

🗂 Dataset  https://drive.google.com/drive/folders/1dkxyM9rPDn7y_4uhfCl3AGxlaP5UTZHq?usp=drive_link

Source: OKCupid public profiles dataset

Total records: ~60,000

Dataset contains:

Personal essays

Demographic data

⚠️ Full dataset is over 140MB → GitHub size limit is 100MB
➡️ A sample dataset (profiles_sample.csv) is included for reproducibility.

Full dataset available here: (add link when needed)

🔧 Techniques Used
Category	Method
Text preprocessing	TF-IDF vectorization
Numeric scaling	StandardScaler
Classification	Logistic Regression
Train/Test strategy	Stratified split
Data imbalance fix	Random oversampling
📊 Model Performance (After Balancing)
Metric	not_single	single
Precision	0.83	0.90
Recall	0.91	0.81
F1-score	0.87	0.85

📌 Accuracy ≈ 86%
✔ Model predicts both classes fairly
✔ Strong recall for relationship users (important for matchmaking)

🧠 Key Findings

Essay content contains strong relationship-status signals

Balancing data dramatically improves real-world performance

Accuracy alone is misleading when classes are imbalanced
