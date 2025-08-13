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

## 📌 Methodology

### 1. Dataset Preparation
- A custom floorplan dataset was used, containing annotated images of **doors**, **windows**, and **zones**.
- The dataset was split into:
  - **Training**: 80%
  - **Validation**: 20%  
  This ensured robust performance evaluation.

### 2. Environment & Version Control
- A private **GitHub repository** was created to track changes, maintain reproducibility, and store:
  - Scripts for EDA
  - Data preparation scripts
  - Training scripts

### 3. Exploratory Data Analysis (EDA)
- Visualized **class distributions** and checked annotation quality to ensure dataset balance.
- Verified that all images had corresponding label files.

### 4. Model Selection & Training
- **YOLOv11** architecture was chosen for:
  - Real-time object detection capabilities
  - Efficient computation
  - Strong balance between accuracy and speed
- Trained two variants for comparison:
  - **YOLO11n**: Nano — faster, lighter
  - **YOLO11s**: Small — more capacity
- Applied **early stopping** with a patience of 20 epochs to prevent overfitting.
- Experiments included different image resolutions (**640** and **1024**) to evaluate performance impact.

### 5. Evaluation
- Models were evaluated using:
  - **Precision**
  - **Recall**
  - **mAP@50**
  - **mAP@50–95**
- The **best-performing model checkpoint** was saved for inference.

---

## 📊 Results

| Metric    | YOLO11n | YOLO11s |
|-----------|---------|---------|
| Precision | 0.873   | 0.875   |
| Recall    | 0.834   | 0.830   |
| mAP@50    | 0.903   | 0.905   |
| mAP@50–95 | 0.656   | 0.661   |

---

## 🏁 Conclusion

- Both **YOLO11n** and **YOLO11s** performed very closely in terms of accuracy, with **YOLO11s** slightly outperforming YOLO11n in **mAP** scores.  
- **YOLO11n** is faster and more lightweight, making it more suitable for **real-time applications**.  
- **YOLO11s** offers a marginal accuracy improvement and may be preferred for **offline analysis** or when **computational resources are sufficient**.  
- The results demonstrate that **YOLOv11** is highly effective for **floorplan object detection**, capable of detecting **doors**, **windows**, and **zones** with **high precision** and **recall**.
