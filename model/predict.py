import joblib

class ModelPredictor:
    def __init__(self, model_path: str):
        """
        Initializes the ModelPredictor by loading the trained model.
        
        Args:
        model_path (str): Path to the saved model file.
        """
        self.model = joblib.load(model_path)

    def predict(self, text: str):
        """
        Makes a prediction for the given text input.

        Args:
        text (str): The input text to classify.

        Returns:
        dict: A dictionary containing the prediction and probability for each class.
        """
        # Perform prediction
        prediction = self.model.predict([text])[0]
        
        # Get probability scores
        probability = self.model.predict_proba([text])[0]
        
        return {
            "prediction": prediction,
            "probability": probability.tolist()
        }