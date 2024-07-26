# Placement Prediction System

## Overview
This project involves developing a placement prediction system using deep learning techniques to forecast student placements. The system leverages TensorFlow and Keras for building and training neural network models, Flask for deployment, and Matplotlib for visualizing data insights. The objective is to provide accurate placement predictions based on various student attributes.

## Key Learnings

- **Data Preprocessing:** Applied scaling and normalization techniques to prepare data for model training, improving model performance and accuracy.
- **Model Training:** Trained neural network models using TensorFlow and Keras, tuning hyperparameters to enhance prediction reliability.
- **Web Deployment:** Integrated the trained model into a Flask-based web application, enabling real-time predictions through a user-friendly interface.
- **Model Evaluation:** Conducted rigorous testing and validation to ensure the robustness and accuracy of the prediction models.

## Experience Gained

- **Deep Learning:** Developed and fine-tuned neural network architectures to predict placement outcomes with high precision.
- **Data Handling:** Implemented data preprocessing pipelines to handle and prepare data for machine learning models effectively.
- **Web Application Development:** Deployed machine learning models in a web application environment, enhancing user interaction and accessibility.
- **Model Performance:** Evaluated model performance using appropriate metrics, ensuring reliable and actionable predictions.

## Installation and Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/placement-prediction-system.git

2. **Navigate to the Project Directory:**
   cd placement-prediction-system

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Run the Flask Application:**
     python index.py

5. **Access the Web Application:**
    Open your web browser and go to http://localhost:5000.


![Placement Prediction Demo pic1](https://github.com/yashmith-r/placement_prediction/assets/114250035/7e9cb3f2-a39e-4135-b645-6ad6d2e6cc7f)
![Placement Prediction Demo pic2](https://github.com/yashmith-r/placement_prediction/assets/114250035/9c9e23f5-e49a-4c32-97e6-1be0d8a9d054)


## Project Structure
1. index.py: Main script to run the Flask application.
2. model.py: Contains code for training and evaluating neural network models.
3. scaler.pkl: Saved scaler for data preprocessing.
4. my_model: Saved trained neural network model.
5. templates/: Contains HTML templates for the Flask web application.
6. tatic/: Contains static files such as CSS and JavaScript.
