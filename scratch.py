### Load the images and plot them here.
### Feel free to use as many code cells as needed.

import os
import numpy as np
import cv2

examples_dir = 'examples'
example_files = [os.path.join(examples_dir, filename) for filename in list(os.walk(examples_dir))[0][2]]
n_imgs = len(example_files)
example_images = np.zeros((n_imgs, 32, 32, 1))

for i in range(n_imgs):
    img = cv2.imread(example_files[i], cv2.IMREAD_GRAYSCALE)
    shape = img.shape
    scale = (shape[0] / 32, shape[1] / 32)
    scale = max(scale)
    shape = (int(shape[1] / scale), int(shape[0] / scale))
    img = cv2.resize(img, shape)
    img = np.expand_dims(img, 3)
    example_images[i][:shape[1]][:shape[0]][:] = img
    # example_images[i][:17][:18] = img

print(type(example_images[0][0]))
print(example_images[0].shape)
print(example_images.shape)

