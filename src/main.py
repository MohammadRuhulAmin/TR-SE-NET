from packages import ImageAugmentation
from skimage import io
import numpy as np
import os
imageAug = ImageAugmentation(
    rotation_range=45,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='constant',
    cval=125
)
# -------------------------------
# Load image safely
# -------------------------------
img_path = "public/training/farm_x.jpg"
img = io.imread(img_path)

# If grayscale → convert to RGB
if len(img.shape) == 2:
    img = np.stack((img,) * 3, axis=-1)

# Convert to uint8 (important for Keras save)
img = img.astype(np.uint8)

# Add batch dimension (VERY IMPORTANT)
img = np.expand_dims(img, axis=0)

# -------------------------------
# Generator
# -------------------------------
datagen = imageAug.data_generator()

# Create output folder if not exists
save_dir = "./public/training/augmented"
os.makedirs(save_dir, exist_ok=True)

# -------------------------------
# Generate images
# -------------------------------
i = 0

for batch in datagen.flow(
        img,
        batch_size=1,
        save_to_dir=save_dir,
        save_prefix="aug",
        save_format="png"):

    i += 1
    print(f"Generated image: {i}")

    if i >= 10:
        break