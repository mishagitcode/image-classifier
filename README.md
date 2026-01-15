# 📊 Image Classifier (Apple vs Pear)

---

**Table of Contents**
1. [Project Overview](#-project-overview)
2. [Project Structure](#-project-structure)
3. [Dataset Description](#-dataset-description)
4. [Model Description](#-model-description)
5. [How to Run the Project](#-how-to-run-the-project)
   - [Prerequisites](#1-prerequisites)
   - [Installation](#2-installation)
   - [Running the Application](#3-running-the-application)
6. [Technologies](#-technologies)

---

## 📝 Project Overview

This project is a full-stack deep learning application designed to classify fruits—specifically Apples and Pears. It leverages a pre-trained CNN model (.h5 format) and provides a user-friendly web interface for real-time predictions.

The workflow includes:
1. Image Upload (users can upload .jpg, .png, or other common image formats via a web form)
2. Image Preprocessing (automatic resizing to 100x100 pixels and normalization of pixel values)
3. Inference (the backend uses TensorFlow to predict the probability of the class)
4. Result Display (the application calculates the confidence percentage and displays the final label (Apple or Pear))

---

## 📂 Project Structure

```text
image-classifier/   
├── app.py                      # Flask application routes and server logic
├── classifier.py               # Image preprocessing and model inference logic
├── requirements.txt            # Project dependencies
├── static/                     # Static assets
│   ├── models/                 # Folder containing the trained Keras model (.h5)
│   │   └── apple_pear.h5
│   └── uploads/                # Temporary storage for user-uploaded images
│   └── images_for_test/        # Storage of images for test
│   └── styles.css              # CSS styles for the web interface
└── templates/                  # HTML templates for the web interface
    ├── base.html               # Base HTML structure page
    ├── index.html              # Landing page
    ├── upload_image.html       # Upload form page
    └── result.html             # Result display page
```

---

## 🍏 Dataset Description

This project utilizes a refined subset of the popular Fruits 360 dataset to train and validate the image classifier.

- **Dataset Source:** [Fruits 360 dataset on Kaggle](https://www.kaggle.com/datasets/moltean/fruits)

- **Selected Varieties:** To ensure high accuracy, the model focuses on Apple and Pear classes, specifically utilizing subsets like Apple 10 and Pear 10

- **Dataset Composition:** 
  - *Training Set:* `1,400 images distributed across the 2 classes`
  - *Validation Set:* `462 images distributed across the 2 classes`

- **Image Properties:**
  - *Dimensions:* `100x100 pixels`
  - *Format:* `RGB color images`
  - *Visual Style:* `Fruits are captured against a clear white background to minimize noise during training`

- **Preprocessing:** In the application pipeline, images are scaled to 100x100 and normalized by a factor of 1/255.0 to convert pixel values to a range between 0 and 1.

---

## 🧠 Model Description

The classification engine relies on a Convolutional Neural Network (CNN).

- Input Shape 
> The model expects an input size of 100x100x3 (RGB)

- Binary Classification
> The model uses a sigmoid activation function in the output layer, producing a single score between 0 and 1 

- Classification Logic
> A score < 0.5 is classified as an Apple.
> A score > 0.5 is classified as a Pear.

- Preprocessing
> All input images are normalized by dividing pixel values by 255 to scale them into the [0, 1] range before being fed into the network

---

## 🚀 How to Run the Project

Follow these steps to set up the environment and run the analysis on your local machine.

### 1. Prerequisites
- Python 3.8+
- Git
- A pre-trained apple_pear.h5 model file placed in static/models/.

### 2. Installation

2.1. Clone the repository:

```commandline
git clone https://github.com/mishagitcode/image-classifier.git
```

```commandline
cd image-classifier
```

2.2. Create virtual environment

```commandline
python -m venv venv
```

2.3. Activate virtual environment

2.3.1. Windows:

```commandline 
venv\Scripts\activate
```

2.3.2. macOS/Linux:

```commandline
source venv/bin/activate
```


2.4. Install the required dependencies:

```commandline
pip install -r requirements.txt
```

---

### 3. Running the Application

Launch the Flask server:

```Bash
python app.py
```

---

## 🛠 Technologies

- **Python**: Core programming language.

- **Flask**: Lightweight WSGI web application framework for the backend.

- **TensorFlow/Keras**: Used for loading the CNN model and performing image inference.

- **NumPy**: For numerical operations and array manipulation.

- **HTML/CSS**: For the front-end user interface.

---

Developed by [mishagitcode](https://github.com/mishagitcode)
