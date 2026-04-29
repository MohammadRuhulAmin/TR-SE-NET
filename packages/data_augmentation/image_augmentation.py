from tensorflow.keras.preprocessing.image import ImageDataGenerator
from skimage import io
import numpy as np
import os
class ImageAugmentationEngine:
    def __init__(self, **kwargs):
        self.config = {
            "rotation_range": 0,
            "width_shift_range": 0.0,
            "height_shift_range": 0.0,
            "shear_range": 0.0,
            "zoom_range": 0.0,
            "horizontal_flip": False,
            "fill_mode": "nearest",
            "cval": 0
        }
        self.config.update(kwargs)
    def get_generator(self):
        return ImageDataGenerator(**self.config)
    def load_image(self, img_path):
        img = io.imread(img_path)
        if len(img.shape) == 2:
            img = np.stack((img,) * 3, axis=-1)
        img = img.astype(np.uint8)
        img = np.expand_dims(img, axis=0)
        return img
    def augment(self, img_path, save_dir, num_images=10):
        img = self.load_image(img_path)
        datagen = self.get_generator()
        os.makedirs(save_dir, exist_ok=True)
        i = 0
        for batch in datagen.flow(
                img,
                batch_size=1,
                save_to_dir=save_dir,
                save_prefix="aug",
                save_format="png"):
            i += 1
            print(f"Generated image: {i}")
            if i >= num_images:
                break