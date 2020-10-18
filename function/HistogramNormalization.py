import cv2
import numpy as np
import matplotlib.pyplot as plt

# histogram normalization
def hist_normalization(img, a=0, b=255):
	# get max and min
	c = img.min()
	d = img.max()

	out = img.copy()

	# normalization
	out = (b-a) / (d - c) * (out - c) + a
	out[out < a] = a
	out[out > b] = b
	out = out.astype(np.uint8)
	
	return out