import cv2
import numpy as np

def apply_filters(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1]=0
        filtered_image[:, :, 0]=0
        
    elif filter_type == "green_tint":
        filtered_image[:, :, 0]=0
        filtered_image[:, :, 2]=0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1]=0
        filtered_image[:, :, 2]=0
    
    elif filter_type == "sobel":
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_scale, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_scale, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype('uint8'), sobely.astype('uint8'))
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)

    elif filter_type == "canny":
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_scale, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error! Could not acess webcam")
    exit()

filter_type = "original"

print("Press the following keys to apply the filter!")
print("r - red tint")
print("g - Green tint")
print("b - Blue tint")
print("s - Sobel Edge Detection")
print("c - Canny Edge Detection")
print("o - original")
print("q - Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed! to capture the frame.")
        break

    if filter_type != "original" :
        display_frame = apply_filters(frame, filter_type)
    
    else:
        display_frame = frame

    cv2.imshow("Webcame Filters", display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
        filter_type = "red_tint"
    
    elif key == ord("g"):
        filter_type = "green_tint"

    elif key == ord("b"):
        filter_type = "blue_tint"

    elif key == ord("s"):
        filter_type = "sobel"

    elif key == ord("c"):
        filter_type = "canny"

    elif key == ord("o"):
        filter_type = "original"

    elif key == ord("q"):
        print("Exiting Program..")
        break

cap.release
cv2.destroyAllWindows()

