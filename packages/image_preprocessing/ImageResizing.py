import cv2
import os
from pathlib import Path

class ImageResizer:
    def __init__(self, target_size=(124, 124)):
        self.target_size = target_size
        # Supported image formats
        self.valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    def resize_single_image(self, image_path, output_path):
        """Resize and save a single image"""
        image = cv2.imread(str(image_path))
        if image is not None:
            resized_img = cv2.resize(image, self.target_size, interpolation=cv2.INTER_AREA)
            cv2.imwrite(str(output_path), resized_img)
            return True
        return False

    def resize_folder(self, input_folder, output_folder):
        """Resize all images in a folder and save to output folder"""
        input_path = Path(input_folder)
        output_path = Path(output_folder)

        # Create output directory if it doesn't exist
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"Processing folder: {input_path}")
        count = 0
        for file in input_path.iterdir():
            if file.suffix.lower() in self.valid_extensions:
                save_to = output_path / file.name
                success = self.resize_single_image(file, save_to)
                if success:
                    count += 1
                    if count % 10 == 0: # Print every 10 images
                        print(f"Resized {count} images...")

        print(f"Done! Total {count} images resized and saved to: {output_folder}")

