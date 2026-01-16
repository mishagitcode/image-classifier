import os
import tensorflow as tf
from flask import Flask, request, render_template

from classifier import classify

app = Flask(__name__)

STATIC_FOLDER = "static/"
UPLOAD_FOLDER = "static/uploads/"
MODEL_PATH = os.path.join("static", "models", "apple_pear.h5")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

cnn_model = tf.keras.models.load_model(MODEL_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload")
def upload_page():
    return render_template("upload_image.html")


@app.post("/classify")
def upload_file():
    if "image" not in request.files:
        return "No file uploaded", 400

    file = request.files["image"]
    upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(upload_image_path)

    label, prob = classify(cnn_model, upload_image_path)

    display_prob = round((prob * 100), 2)

    return render_template(
        "result.html",
        label=label,
        probability=display_prob,
        filename=file.filename
    )


if __name__ == "__main__":
    app.run()
