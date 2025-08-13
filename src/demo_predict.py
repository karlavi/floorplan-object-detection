from ultralytics import YOLO

# Load your trained model 
model = YOLO("models/colab_e100p20_640/best_yolo11n.pt")

# Run prediction on a folder of images or a single image
results = model.predict(
    source="test_images/",   # can be a folder or single image path
    conf=0.5,                # confidence threshold
    save=True,               # save results with boxes
    project="demo_results",  # output folder for predictions
    name="run1"              # subfolder
)

print("✅ Predictions saved in demo_results/run1")
