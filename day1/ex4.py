
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('sample.jpg', cv2.IMREAD_COLOR)

b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()
