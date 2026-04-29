from tensorflow.keras.preprocessing.image import ImageDataGenerator
from skimage import io


class ImageAugmentation:
    def __init__(self, **kwargs):
        self.config = {
            "rotation_range": 0,"width_shift_range": 0.0,
            "height_shift_range": 0.0,"shear_range": 0.0,
            "zoom_range": 0.0,"horizontal_flip": False,
            "fill_mode": "nearest","cval": 0
        }
        self.config.update(kwargs)

    def get_property(self, key):
        return self.config.get(key)

    def update_property(self, **kwargs):
        self.config.update(kwargs)

    def __str__(self):
        return f"Augmentation Config: {self.config}"
    


