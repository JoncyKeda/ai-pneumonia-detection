import numpy as np
from utils.preprocess import preprocess_image

# Demo prediction logic
# Replace with trained model later

def predict_image(image):
    processed_image = preprocess_image(image)

    score = np.random.rand()

    if score > 0.5:
        prediction = "Pneumonia"
        confidence = score * 100
    else:
        prediction = "Normal"
        confidence = (1 - score) * 100

    return prediction, confidence
