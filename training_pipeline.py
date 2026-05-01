from packages import ImageResizer
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--resize_image124x124", action="store_true")
parser.add_argument("--resize_image96x96", action="store_true")
parser.add_argument("--resize_mask124x124", action="store_true")
parser.add_argument("--resize_mask96x96", action="store_true")
args = parser.parse_args()


if args.resize_image124x124:
    resizer = ImageResizer(target_size=(124, 124))
    input_dir = './public/datasets/kvasir-seg/images/'
    output_dir = './public/training/images/resized_124x124/'
    resizer.resize_folder(input_dir, output_dir)

if args.resize_mask124x124:
    resizer = ImageResizer(target_size=(124, 124))
    input_dir = './public/datasets/kvasir-seg/masks/'
    output_dir = './public/training/masks/resized_masks_124x124/'
    resizer.resize_folder(input_dir, output_dir)


if args.resize_image96x96:
    resizer = ImageResizer(target_size=(96, 96))
    input_dir = './public/datasets/kvasir-seg/images/'
    output_dir = './public/training/images/resized_96x96/'
    resizer.resize_folder(input_dir, output_dir)

if args.resize_mask96x96:
    resizer = ImageResizer(target_size=(96, 96))
    input_dir = './public/datasets/kvasir-seg/masks/'
    output_dir = './public/training/masks/resized_masks_96x96/'
    resizer.resize_folder(input_dir, output_dir)