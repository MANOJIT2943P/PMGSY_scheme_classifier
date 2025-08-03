# PMGSY Scheme Classifier

## Overview
The PMGSY Scheme Classifier is designed to assist in the classification of various schemes under the Pradhan Mantri Gram Sadak Yojana (PMGSY), a government initiative aimed at providing all-weather road connectivity to unconnected villages in India. This project leverages machine learning techniques to analyze and categorize schemes based on their features, enabling stakeholders to make informed decisions regarding infrastructure development.
The classifier is built using Python and Flask, providing a web-based interface for users to input scheme details and receive instant classification results. The underlying model is trained on a comprehensive dataset that includes various attributes of PMGSY schemes, ensuring accurate predictions.
By automating the classification process, this project aims to enhance the efficiency of scheme management and facilitate better planning and execution of rural road projects.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Features

- Classifies PMGSY schemes into predefined categories.
- User-friendly web interface for input and output.
- Built with Python and Flask for the backend.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/MANOJIT2943P/PMGSY_scheme_classifier.git
   cd PMGSY_scheme_classifier
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```


4. Open your web browser and go to http://127.0.0.1:5000/predict

## Usage

- Navigate to the web interface.
- Input the features values.
- Click on the "Predict" button to get the predicted category.

## Dataset
The dataset used for training the model is located in the Dataset folder. It contains various features related to PMGSY schemes.

## Model
The classification model is implemented in the Model folder. The model is trained using the dataset and can be modified or retrained as needed.
