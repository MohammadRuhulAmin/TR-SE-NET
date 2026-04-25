import numpy as np
import os
import cv2

# =========================
# INPUT
# =========================
image_npy = "cancer_cells/Part 1/images/images.npy"
mask_npy = "cancer_cells/Part 1/masks/masks.npy"

# =========================
# OUTPUT
# =========================
img_out = "dataset/images"
mask_out = "dataset/masks"

os.makedirs(img_out, exist_ok=True)
os.makedirs(mask_out, exist_ok=True)

# =========================
# LOAD DATA
# =========================
images = np.load(image_npy)
masks = np.load(mask_npy)

print("Images shape:", images.shape)
print("Masks shape :", masks.shape)

# =========================
# LOOP
# =========================
for i in range(len(images)):

    img = images[i]              # (256,256,3)
    mask = masks[i]              # (256,256,5)

    # ----------------------
    # IMAGE SAVE
    # ----------------------
    img = img.astype(np.uint8)

    # ----------------------
    # MASK PROCESS
    # ----------------------
    # multi-channel → single mask
    mask_single = np.argmax(mask, axis=-1)  # (256,256)

    # optional: binary mask
    # mask_single = (mask_single > 0).astype(np.uint8) * 255

    # ----------------------
    # SAVE
    # ----------------------
    filename = f"img_{i:05d}"

    cv2.imwrite(os.path.join(img_out, filename + ".jpg"), img)
    cv2.imwrite(os.path.join(mask_out, filename + ".png"), mask_single)

print("Done ✅")