# 📱 Mobile Price Prediction Web App

This project is a complete machine learning pipeline designed to predict the **approximate price (in EUR)** of mobile phones based on their specifications. It includes data cleaning, analysis, visualization, model building, evaluation, and deployment setup.

Link to the trained model pickle file: (https://drive.google.com/file/d/1hshIgOPKBTgZyW7hUb3OInisjnkOnzv8/view?usp=sharing) . Download the pickle file and place it as mentioned in the folder structure below 

## 🔧 Features

- 📊 **Data Cleaning & Profiling**  
  Performed functional and physical cleansing using Pandas; generated an HTML profiling report for raw data insights.

- 📈 **Exploratory Data Analysis**  
  Visualized feature distributions, correlations, and key trends affecting phone prices.

- 🤖 **Model Building**  
  Applied and evaluated multiple regression models to select the best performer. Final model was saved using `joblib`.

- 🔌 **Backend Deployment**  
  Created backend services using Python (Flask/FastAPI) to handle real-time predictions with future user input.

- 🧪 **Testing & Validation**  
  Extensive testing was performed to ensure the model's accuracy, stability, and generalizability.

## 🚧 GUI Development

> **Note:** GUI implementation is currently in progress. The goal is to create an interactive front-end where users can upload mobile phone specs and get price predictions.

## 🛠️ Folder Structure

```
├── requirements/
│   ├── data_prep_modeling.ipynb   # Data cleaning, EDA, model training
│   ├── price_report.html             # Pandas profiling report
|   |__ mobile_price_stacked.pickle 
├── server/
│   ├── server.py                # Model loading and prediction logic
│   ├── util.py                            # API server for predictions
```

## 🚀 Future Improvements

- Add a user-friendly front-end (using Streamlit, Gradio, or HTML/JS)
- Integrate CI/CD for continuous deployment
- Implement auto-retraining based on fresh data
- Enhance model monitoring and logging

## 🧩 Tech Stack

- Python, Pandas, Scikit-learn  
- Flask / FastAPI (Backend)  
- Jupyter Notebook  
- Pandas Profiling  
- Joblib  

## 🤝 Contribution

GUI developers and contributors are welcome to help build the front-end!
