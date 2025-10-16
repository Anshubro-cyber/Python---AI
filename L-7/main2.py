import cv2

image = cv2.imread('L-7\Ferrari.jpg')
gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_scale, (500, 500))

cv2.imshow("Processed Image", resized_image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("Greyscale_picture.jpg", resized_image)
    print("Image saved successfully")
else:
    print("Image not saved")

cv2.destroyAllWindows()

