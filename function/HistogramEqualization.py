import cv2
import numpy as np
import matplotlib.pyplot as plt

# histogram equalization
def hist_equal(img, z_max=255):
	H, W, C = img.shape
	S = H * W * C * 1.

	out = img.copy()

	sum_h = 0.

	for i in range(1, 255):
		ind = np.where(img == i)
		sum_h += len(img[ind])
		z_prime = z_max / S * sum_h
		out[ind] = z_prime

	out = out.astype(np.uint8)

	return out
