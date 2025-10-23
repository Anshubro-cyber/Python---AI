import cv2
import matplotlib.pyplot as plt

image = 'Ferrari.jpg'
image_r = cv2.imread(image)

image_rgb = cv2.cvtColor(image_r, cv2.COLOR_BGR2RGB)
h, w, _ = image_rgb.shape

rect_w, rect_h = 150, 150
top_left = (20,20)
bottom_right = (top_left[0]+rect_w, top_left[1]+rect_h)
cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 255), 3)

rect2_w, rect2_h = 150, 150
top_left2 = (w - rect2_w - 20, h - rect2_h - 20)
bottom_right2 = (top_left2[0] + rect2_w, top_left2[1] + rect2_h)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255,0, 255), 3)

center1_x = top_left[0] + rect_w // 2
center1_y = top_left[1] + rect_h // 2
center2_x = top_left2[0] + rect2_w // 2
center2_y = top_left2[1] + rect2_h // 2
cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 255, 0), -1)
cv2.circle(image_rgb, (center2_x, center2_y), 15, (0, 255, 0), -1)

cv2.line(image_rgb, (center1_x, center1_y), (center2_x , center2_y), (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left[0], top_left[1] - 10), font, 0.7, (0, 255 , 255) , 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1] - 10), font, 0.7, (0, 255 , 255) , 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 3', (center1_x - 40, center1_y + 40), font, 0.7, (255,0,255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 4', (center2_x - 40, center2_y + 40), font, 0.7, (255,0,255), 2, cv2.LINE_AA)

arrow_start = (w - 50, 20)
arrow_end = (w - 50, h - 20)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

height_label = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2)
cv2.putText(image_rgb, f'Height: {h}px', height_label, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.show()
