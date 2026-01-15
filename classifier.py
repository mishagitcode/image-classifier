import tensorflow as tf
import numpy as np


def classify(model, image_path):
    img = tf.keras.utils.load_img(image_path, target_size=(100, 100))
    img_array = tf.keras.utils.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    score = float(predictions[0][0])

    if score <= 0.5:
        label = "Apple"
        prob = (1 - score)
    else:
        label = "Pear"
        prob = score

    return label, prob
