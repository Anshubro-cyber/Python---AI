import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Ferrari.jpg")
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w//2, h//2)
Matrix = cv2.getRotationMatrix2D(center, 180, 2)
rotated = cv2.warpAffine(image, Matrix, (h, w))
rotated_rbg = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rbg)
plt.title("Rotated Image")
plt.show()
