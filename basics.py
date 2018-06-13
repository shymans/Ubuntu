import cv2

img = cv2.imread('test.jpg')
print img.shape

'''
if img is None:
	print "Image not loaded"
else:
	print "Image is loaded!"
'''

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
