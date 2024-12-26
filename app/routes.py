from fastapi import APIRouter, HTTPException
from model.predict import ModelPredictor
# from model.monitor import monitor_prediction_time

# Initialize API router
router = APIRouter()

# Load the model for predictions
predictor = ModelPredictor("model/svm_model.pkl")

# Initialize monitor for measuring prediction time
# monitor = monitor_prediction_time()

@router.post("/predict/")
# @monitor
def predict(text: str):
    """
    Endpoint for making predictions.

    Args:
    text (str): The input text to classify.

    Returns:
    dict: A dictionary containing the prediction result and status.
    """
    try:
        result = predictor.predict(text)
        return {"status": "success", "data": result}
    except Exception as e:
        # Handle prediction errors
        raise HTTPException(status_code=500, detail=str(e))