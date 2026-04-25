import h5py
import numpy as np
import cv2
import os

input_folder = "brainTumorDataPublic_2299-3064"
image_folder = "dataset/images"
mask_folder = "dataset/masks"

os.makedirs(image_folder, exist_ok=True)
os.makedirs(mask_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".mat"):
        path = os.path.join(input_folder, file)

        with h5py.File(path, 'r') as f:
            cjdata = f['cjdata']

            # image
            image = np.array(cjdata['image']).T
            image = (image - image.min()) / (image.max() - image.min())
            image = (image * 255).astype(np.uint8)

            # mask
            mask = np.array(cjdata['tumorMask']).T
            mask = (mask * 255).astype(np.uint8)

            filename = file.replace(".mat", "")

            # save
            cv2.imwrite(os.path.join(image_folder, filename + ".jpg"), image)
            cv2.imwrite(os.path.join(mask_folder, filename + ".png"), mask)