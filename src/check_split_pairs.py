# src/check_split_pairs.py
import os, pathlib
for split in ["train","val"]:
    imgp = f"data/images/{split}"
    lblp = f"data/labels/{split}"
    imgs = {pathlib.Path(f).stem for f in os.listdir(imgp)}
    lbls = {pathlib.Path(f).stem for f in os.listdir(lblp)}
    only_imgs = sorted(imgs - lbls)
    only_lbls = sorted(lbls - imgs)
    print(f"[{split}] images={len(imgs)} labels={len(lbls)}")
    if only_imgs: print("  -> images without labels:", only_imgs[:10])
    if only_lbls: print("  -> labels without images:", only_lbls[:10])
