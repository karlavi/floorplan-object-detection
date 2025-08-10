import os
import matplotlib.pyplot as plt
import pandas as pd

# Paths
labels_dir = "data/labels"  # Your current single labels folder
classes_path = "data/classes.txt"

# Load class names
with open(classes_path, "r") as f:
    CLASSES = [line.strip() for line in f.readlines()]

# Count objects per class
class_counts = {i: 0 for i in range(len(CLASSES))}
for file_name in os.listdir(labels_dir):
    if file_name.endswith(".txt"):
        with open(os.path.join(labels_dir, file_name), "r") as f:
            for line in f:
                class_id = int(line.strip().split()[0])
                class_counts[class_id] += 1

# Create DataFrame
df = pd.DataFrame({
    "class_id": list(class_counts.keys()),
    "class_name": [CLASSES[i] for i in class_counts.keys()],
    "count": list(class_counts.values())
}).sort_values("class_name")

# Save plot
save_dir = "notebooks/figures"
os.makedirs(save_dir, exist_ok=True)
out_path = os.path.join(save_dir, "class_distribution_pre_split.png")

plt.figure(figsize=(6, 4))
plt.bar(df["class_name"], df["count"])
plt.title("Class Distribution (pre-split)")
plt.xlabel("Class")
plt.ylabel("Number of objects")
plt.tight_layout()
plt.savefig(out_path, dpi=200)
print(f"✅ Saved chart to: {os.path.abspath(out_path)}")

plt.show()
