import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), np.uint8)

img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
img = cv2.line(
