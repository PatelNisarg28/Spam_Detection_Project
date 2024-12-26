Sentiment Analysis API

This project provides a Sentiment Analysis API to classify text as either positive or negative sentiment. The API uses a trained machine learning model (e.g., SVM with TF-IDF features) and is implemented with FastAPI for quick and easy deployment.

Features

	•	Classifies input text into positive or negative sentiment.
	•	Supports integration with tools like Postman or curl for testing.
	•	Easy-to-train pipeline for custom datasets.

Requirements

	•	Python 3.8 or later
	•	Dependencies specified in requirements.txt

Installation

1. Clone the repository:
   
   git clone <repository_url>
    
cd sentiment_analysis


2. Install dependencies:

   pip install -r requirements.txt

Training the Model

Ensure you have a dataset with two columns: text (review text) and label (positive/negative sentiment).
	1.	Place your dataset (e.g., sentiment_data.csv) in the project directory.
	2.	Train the model:

python model/train.py

This will save the trained model (e.g., model/sentiment_model.pkl) in the model directory.

Running the API

Start the FastAPI server using Uvicorn:

uvicorn app.main:app --reload

The API will be accessible at http://127.0.0.1:8000.

API Endpoints

1. Predict Sentiment

	•	URL: /predict/
	•	Method: POST
	•	Input: JSON body with the text to classify:

{
    "text": "Waste of money, I regret buying this."
}


Output:

{
    "status": "success",
    "data": {
        "prediction": "negative",
        "probability": [
            0.9981279316388347,
            0.0018720683611652684
        ]
    }
}

