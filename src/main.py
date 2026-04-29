from packages import ImageAugmentation


imageAug = ImageAugmentation(rotation_range=45,width_shift_range=0.2, height_shift_range=0.2,
            shear_range=0.2,horizontal_flip=True,zoom_range=0.2,fill_mode='constant',
            cval=125)

print(imageAug)