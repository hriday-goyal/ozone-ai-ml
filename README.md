# 🌿 AirGuard – AI-Powered Ozone & Air Quality Analysis

A machine learning project exploring ozone output prediction, synthetic air-purification efficiency estimation, and safety classification using simulated data.

## 📌 Overview

AirGuard combines multiple machine learning workflows into an interactive Streamlit dashboard and supporting Jupyter notebooks.

The project explores how supervised machine learning can be applied to environmental and air-quality related problems using simulated ozone-generator data.

> ⚠️ **Important:** The models in this project are trained and evaluated on simulated data. Their results should not be interpreted as real-world measurements, medical advice, or validation of ozone-generation or air-purification performance.

## 🔧 Technologies Used

- Python
- Streamlit
- scikit-learn
- NumPy
- Pandas
- Matplotlib
- Seaborn
- XGBoost
- Jupyter / Google Colab

## 🚀 Features

- Predict simulated ozone output using regression models
- Compare Linear Regression, Random Forest, and XGBoost
- Estimate simulated air-purification efficiency
- Classify observations using a synthetic safety threshold
- Explore model performance through evaluation metrics and visualizations
- Interactive Streamlit dashboard for model inference

## 🧪 ML Models Implemented

### 1. Ozone Output Estimation

Predicts simulated ozone output using environmental and generator-related input variables.

Models compared:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

On the test split of the simulated dataset:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 5.724 | 7.742 | 0.815 |
| Random Forest | 3.503 | 4.895 | 0.926 |
| XGBoost | 4.182 | 5.395 | 0.910 |

Random Forest achieved the strongest R² and lowest error among the three models on this simulated test split.

### 2. Air-Purification Efficiency Estimation

A Random Forest regression model estimates a synthetically generated purification-efficiency target based on simulated environmental and ozone-related variables.

Test-set performance:

- **R²:** 0.993
- **MAE:** 0.586
- **RMSE:** 1.949

Because the target is generated using a simulation formula with added noise, these results demonstrate model performance on the simulated target rather than measured purification performance.

### 3. Synthetic Safety Classification

Classification models are used to demonstrate binary classification of observations based on a synthetic ozone-output threshold.

Models implemented:

- Logistic Regression
- Random Forest Classifier

Test-set performance:

| Model | Accuracy |
|---|---:|
| Logistic Regression | 100% |
| Random Forest | 90% |

These results are specific to the simulated dataset and synthetic classification rule. They should not be interpreted as validation of a real-world safety controller.

## 🔗 Live Demo

👉 [Launch AirGuard](https://ozone-ai-ml-ozoneapphriday.streamlit.app)

## 📂 Project Structure

```text
ozone-ai-ml/
├── data/
│   └── simulated_ozone_data.csv
├── notebooks/
│   ├── ozone_output_model.ipynb
│   ├── purification_predictor_model.ipynb
│   └── safety_controller_model.ipynb
├── README.md
├── app.py
└── requirements.txt
