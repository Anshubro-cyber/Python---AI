import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_picture(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def edge_detection(image_path):
        image = cv2.imread(image_path)
        if image is None:
            print("Error! Image Not Found")
            return
        
        gray_scale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        display_picture("Original Grayscale Image", gray_scale)

        print("Select an option")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Smoothening")
        print("5. Median Fitting")
        print("6. exit")

        while True:
            option = input("Enter a choice(1-6)")

            if option == '1':
                sobelx = cv2.Sobel(gray_scale, cv2.CV_64F, 1, 0, ksize=3)
                sobely = cv2.Sobel(gray_scale, cv2.CV_64F, 0, 1, ksize=3)
                combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
                display_picture("Sobel Edge Detection", combined_sobel)

            elif option == '2':
                print("adjust thresholds for canny default: 100 and 200")
                lower_threshold = int(input("Enter lower threshold: "))
                upper_threshold = int(input("Enter upper threshold: "))
                edges = cv2.Canny(gray_scale, lower_threshold, upper_threshold)
                display_picture("Canny Edge Detection", edges)

            elif option == '3':
                laplacian = cv2.Laplacian(gray_scale, cv2.CV_64F)
                display_picture("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

            elif option == '4':
                print("Adjust kernel size for Gaussian smoothening blur(must be an odd number)")
                kernel_size = int(input("Enter the kernel size (odd number)"))
                blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
                display_picture("Gaussian smoothed Image", blurred)

            elif option == '5':
                print("Adjust kernel size for Median Filtering blur(must be an odd number (5) )")
                kernel_size = int(input("Enter the kernel size (odd number): "))
                median_blur = cv2.medianBlur(image, kernel_size)
                display_picture("Median Filtered Image", median_blur)

            elif option == '6':
                print("Exiting Program ...")
                break

            else:
                print("Invalid option. Pls! enter a number between 1 and 6")
   
edge_detection("example.jpeg")

