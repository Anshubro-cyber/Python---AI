import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Ferrari.jpg")

grey_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_scale, cmap='gray')
plt.title("Grey Scale Picture")
plt.show()

cropped_image = image[250:750, 350:850]
cropped_rbg = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rbg)
plt.title("Cropped Picture")
plt.show()