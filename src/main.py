from packages import ImageAugmentationEngine
aug = ImageAugmentationEngine(
    rotation_range=45,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='constant',
    cval=125
)

aug.augment(
    img_path="public/training/farm_x.jpg",
    save_dir="./public/training/augmented",
    num_images=10
)