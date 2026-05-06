import numpy as np

def preprocess_image(image):
    image = image.resize((128,128))

    img = np.array(image)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    return img
