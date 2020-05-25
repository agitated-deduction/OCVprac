import cv2

img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv22.destroyAllWindow()
elif k == ord('s'):
    cv2.imwrite('lenagray.png', img)
    cv2.destroyAllWindow()
