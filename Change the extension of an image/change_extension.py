import cv2
img = cv2.imread('a.jpg')
cv2.imwrite('b.png', img)
cv2.imshow('show',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
