import os
import pandas as pd

# Paths
images_dir = "data/images"
labels_dir = "data/labels"
classes_file = "data/classes.txt"

# Read classes
with open(classes_file, "r") as f:
    classes = [line.strip() for line in f]
print(f"Classes: {classes}")

# Count images & labels
image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
label_files = [f for f in os.listdir(labels_dir) if f.lower().endswith('.txt')]

print(f"Total images: {len(image_files)}")
print(f"Total labels: {len(label_files)}")

# Check if all images have matching labels
missing_labels = [img for img in image_files if os.path.splitext(img)[0] + ".txt" not in label_files]
missing_images = [lbl for lbl in label_files if os.path.splitext(lbl)[0] + ".jpg" not in image_files and os.path.splitext(lbl)[0] + ".png" not in image_files]

if missing_labels:
    print("⚠ Missing label files for these images:", missing_labels)
else:
    print("✅ All images have matching labels.")

if missing_images:
    print("⚠ Missing image files for these labels:", missing_images)
else:
    print("✅ All labels have matching images.")

# Quick class distribution check
class_counts = {}
for lbl_file in label_files:
    with open(os.path.join(labels_dir, lbl_file), "r") as f:
        for line in f:
            cls_id = int(line.split()[0])
            class_counts[cls_id] = class_counts.get(cls_id, 0) + 1

class_df = pd.DataFrame({
    "class_id": list(class_counts.keys()),
    "class_name": [classes[i] for i in class_counts.keys()],
    "count": list(class_counts.values())
})

print("\nClass distribution:")
print(class_df)
