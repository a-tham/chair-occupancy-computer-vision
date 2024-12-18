# Seat Occupancy Detection 

A computer vision prototype developed to detect the occupancy of chairs around a swimming pool. This project utilizes Ultralytics’ YOLOv8 model to determine whether chairs are occupied based on physical presence or the presence of personal items like towels.

## Table of Contents

- [Overview](#overview)
- [Technical Information](#technical-information)
  - [How to Run Inference on the Web](#how-to-run-inference-on-the-web)
  - [How to Run Inference Locally](#how-to-run-inference-locally)
- [Project Code Structure](#project-code-structure)
  - [Folders](#folders)
  - [Scripts](#scripts)
  - [Other Files](#other-files)
- [Model Training and Performance Details](#model-training-and-performance-details)
  - [Overview](#overview)
  - [Model](#model)
  - [Dataset Introduction](#dataset-introduction)
    - [Real Life Images](#real-life-images)
    - [Synthetic Images](#synthetic-images)
  - [Model Training](#model-training)
  - [Limitations](#limitations)
  - [Next Steps](#next-steps)
- [License](#license)
- [Contact](#contact)

## Overview

This project provides a robust solution for monitoring chair occupancy around swimming pools, leveraging computer vision techniques to ensure efficient space utilization. The system can be previewed via a web application or run locally for demonstration and testing purposes.

## Technical Information

### How to Run Inference on the Web

Running inference on the web is the simpler method of the two available options. Follow the steps below to preview the model's performance through the web application.

1. **Azure Hosting:**
   - The model can be hosted on Azure, with a front-end provided for a web application.

2. **Access the Web Application:**
   - Once the Azure Web App is live, navigate to the web application live link.

3. **Upload a Video File:**
   - Click on the **“Browse Files”** button or drag and drop a video file.
   - **File Size Limit:** Ensure the video file is less than 200MB.

4. **Run Inference:**
   - Inference begins automatically after uploading.
   - A video will play with real-time predictions displayed.

### How to Run Inference Locally

For those who prefer running inference on a local machine, follow these steps:

1. **Download and Extract the Project:**
   - Download the `chair.zip` file.
   - Extract it to a desired location on your drive.

2. **Install Python:**
   - Download Python from [python.org](https://www.python.org/downloads/).
   - During installation, ensure to check the box for **“Add Python to Path”**.

3. **Setup the Environment:**
   - Open a Command Prompt or Terminal:
     - **Windows:** Press `Win + R`, type `cmd`, and press Enter.
     - **Mac:** Open Terminal from Applications > Utilities.
   - Navigate to the extracted folder:
     ```bash
     cd path/to/ExtractedFolder
     ```

4. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt

5. **Run The Streamlit App:**
   streamlit run app.py

# Pool Chair Occupancy Detection

This project uses YOLOv8 to detect whether chairs around swimming pools are occupied, considering both human occupants and reservations (e.g., towels).

## Project Structure

### Folders

- **datasets/**
  - Contains images and labels, divided into train, val, and test folders
  - Includes dataset.yaml for model training configuration

- **runs/**
  - Stores information from validation and prediction runs post-training

- **wandb/**
  - Houses data from Weights and Biases integration (validated images and metrics)

- **yolov8_mbs/**
  - Contains metrics, training and validation plots, and model weights during training runs

### Scripts

#### app.py
- Runs the Streamlit application
- Handles video uploads and performs inference
- Automatically manages front-end by loading specified model checkpoint

#### training.py
Manages dataset splitting, model training, and validation.

Usage:
1. **Splitting Dataset**: Uncomment and set paths for:
   - image_directory
   - label_directory
   - output_directory
   - split_dataset

2. **Training**: Set model checkpoint (default: best.pt) and run script

3. **Validation**: Comment out train_model and uncomment validation lines with desired checkpoint

Test Results Arguments:
- `split`: 'val' or 'test'
- `plots`: True or False
- `conf`: Confidence threshold (0-1)
- `iou`: Intersection over Union threshold (0-1)
- `device`: GPU device number (default: 0)

#### helper.py
Contains helper functions for dataset splitting and file renaming

#### rename_files.py
Renames all images in a folder for filename uniformity

#### split_dataset.py
- Splits dataset into training, validation, and testing sets
- Default ratio: 80% train, 10% validation, 10% test

#### modelling.py
Contains functions for running model training

### Other Files
- **best.pt**: Best model checkpoint after training (please run the training to get best model checkpoint)
- **startup.sh**: Command file for starting up Azure instance

## Model Training and Performance Details

### Overview
The project aims to accurately detect occupied pool chairs, considering both human occupants and indicators like reserved towels.

### Model Selection
Ultralytics' YOLOv8 was chosen for its:
- Superior inference speed
- High accuracy compared to alternatives (e.g., Faster R-CNN, SSD)

### Dataset Composition
Total: 324 images
- 128 real-life images
- 196 synthetic images

#### Real Life Images
- Sources: Guest-captured smartphone photos
- Characteristics:
  - Predominantly bright daylight settings
  - Lower camera angles with varying perspectives
- Considerations:
  - Monitoring cameras typically positioned higher
  - Includes diverse styles from various Sands hospitality locations

#### Synthetic Images
- Generation: Adobe Firefly and Midjourney
- Purpose: Enhanced model generalization
- Variety: Covers different:
  - Pool sizes
  - Crowd densities
  - Furniture styles
  - Camera angles
  - Times of day
- Quality: Manually evaluated and annotated using Notate ML on iPad

### Training Details
- Interactive Report: Available on Weights and Biases
- Duration: 6.5 hours
- Data Split: 80/10/10 (train/val/test)
- Performance:
  - Recall: Lower detection rate for occupied chairs
  - Precision: High accuracy in chair state identification

### Current Limitations
1. Night Environments
   - Poor performance under harsh lighting and dark backgrounds
   - Insufficient training data for these conditions

2. Distance and Crowding
   - Difficulty detecting distant chairs
   - Challenges with overlapping chairs in crowded scenes

3. Real-life Footage
   - Lack of actual in-situ camera footage
   - Impacts model adherence to real-world scenarios

4. Perspective Angles
   - Low-angle guest images obscure chairs
   - Overlapping perspectives complicate annotation

## Next Steps

### 1. Acquire Real Camera Footage
- Integrate actual monitoring camera images
- Better align model with real-world conditions

### 2. Expand Synthetic Dataset
- Generate additional synthetic images covering various conditions
- Continue training from current best model checkpoint

### 3. Hyperparameter Tuning
- Experiment with different hyperparameters
- Optimize image augmentation techniques

### 4. Address Class Imbalance
- Generate additional synthetic images with empty chairs
- Balance dataset distribution
