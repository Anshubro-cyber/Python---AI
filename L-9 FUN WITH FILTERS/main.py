import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == 'red tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'blue tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'green tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'increased red':
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 100)
    elif filter_type == 'decreased blue':
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], -50)
    return filtered_image

image_path = 'Ferrari.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not find the Image!")
else:
    filter_type = 'original'

    print("Press to apply a filter!")
    print("r - red tint")
    print("b - blue tint")
    print("g - Green Tint")
    print("i - increase red indent")
    print("d - decrease blue tint")
    print("q - exit")

while True:
    filtered_image = apply_filter(image, filter_type)

    cv2.imshow("Filtered Image", filtered_image)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('r'):
        filter_type = 'red tint'
    elif key == ord('b'):
        filter_type = 'blue tint'
    elif key == ord('g'):
        filter_type = 'green tint'
    elif key == ord('i'):
        filter_type = 'increased red'
    elif key == ord('d'):
        filter_type = 'decreased blue'
    elif key == ord('q'):
        print( 'Exiting the program...')
        break
    else:
        print("Ivalid key presses. Pls! try again ..")

cv2.destroyAllWindows()
        

