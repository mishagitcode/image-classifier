import tensorflow as tf


IMAGE_SIZE = (100, 100)
THRESHOLD = 0.5


def preprocess_image(image):
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = img_array / 255.0
    img_array = tf.expand_dims(img_array, 0)

    return img_array


def load_and_preprocess_image(path):
    image = tf.keras.preprocessing.image.load_img(
        path, target_size=IMAGE_SIZE
    )

    return preprocess_image(image=image)


def classify(model, image_path):
    preprecessed_image = load_and_preprocess_image(path=image_path)

    predictions = model.predict(preprecessed_image)
    score = predictions[0][0]

    label = "apple" if score <= THRESHOLD else "pear"
    prob = 1 - score if label == "apple" else score

    return label, prob
