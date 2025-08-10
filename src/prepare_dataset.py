import os
import random
import shutil
from pathlib import Path

# Paths
images_dir = Path("data/images")
labels_dir = Path("data/labels")

train_img_dir = images_dir / "train"
val_img_dir = images_dir / "val"

train_lbl_dir = labels_dir / "train"
val_lbl_dir = labels_dir / "val"

# Make sure output dirs exist
for d in [train_img_dir, val_img_dir, train_lbl_dir, val_lbl_dir]:
    d.mkdir(parents=True, exist_ok=True)

# Parameters
split_ratio = 0.8  # 80% train, 20% val

# Get all image files
image_files = list(images_dir.glob("*.jpg")) + list(images_dir.glob("*.png"))

# Shuffle to randomize
random.seed(42)
random.shuffle(image_files)

# Split
split_idx = int(len(image_files) * split_ratio)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

def move_files(file_list, target_img_dir, target_lbl_dir):
    for img_path in file_list:
        lbl_path = labels_dir / f"{img_path.stem}.txt"
        if lbl_path.exists():
            shutil.move(str(img_path), str(target_img_dir / img_path.name))
            shutil.move(str(lbl_path), str(target_lbl_dir / lbl_path.name))
        else:
            print(f"⚠️ Warning: Missing label for {img_path.name}")

# Move files
move_files(train_files, train_img_dir, train_lbl_dir)
move_files(val_files, val_img_dir, val_lbl_dir)

print(f"✅ Split complete:")
print(f"Train images: {len(list(train_img_dir.glob('*')))}")
print(f"Val images: {len(list(val_img_dir.glob('*')))}")

