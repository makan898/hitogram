import sys  
sys.path.append(r'.\function')
#ヒストグラム表示　display(img)
import DisplayHistogram as DH 
#ヒストグラム正規化 hist_equal(img, z_max=255)
import HistogramEqualization as HE 
#ヒストグラム平坦化 hist_normalization(img, a=0, b=255)
import HistogramNormalization as HN 
import cv2
import numpy as np

# Read image
img = cv2.imread("sample.jpg").astype(np.float)
H, W, C = img.shape

# histogram normalization
HNout = HN.hist_normalization(img)
HEout = HE.hist_equal(img)

# Display histogram
DH.display(HNout)
DH.display(HEout)


# Save result
cv2.imshow("Histogram Equalization", HEout)
cv2.imshow("Histogram Normalization", HNout)

cv2.imwrite("HNout.jpg", HNout)
cv2.imwrite("HEout.jpg", HEout)

cv2.waitKey(0)
cv2.destroyAllWindows() 

