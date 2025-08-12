## Project on Object Detection
# 🏠 Floorplan Object Detection with YOLOv11

## 📌 Project Overview
This project implements **object detection on architectural floorplan images** to identify and classify:
- **Doors**
- **Windows**
- **Zones**

We use **YOLOv11** for training and evaluation, leveraging annotated images to detect these structural components accurately.  
The model was trained and tested on a custom dataset prepared specifically for this task.

---

## 🎯 Objectives
- Develop a robust object detection model for architectural floorplans.
- Evaluate performance across different YOLO models (`yolo11n`, `yolo11s`) and image resolutions (`640`, `1024`).
- Compare results and identify the optimal configuration.
- Demonstrate model predictions with visual outputs for real-world interpretability.

---

## 📂 Project Structure
floorplan-object-detection/
│
├── configs/ # Dataset YAML configuration files
├── data/ # Raw dataset (images + labels)
├── src/ # Python scripts
│ ├── prepare_dataset.py # Splits dataset into train/val sets
│
├── outputs/ # Model training outputs
│ ├── <experiment_name> # Weights, results.csv, visual predictions
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Files to ignore in version control