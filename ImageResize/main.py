import cv2

#Configurable parameters
source="pet.jpg"
destination='newImage.jpg'
scale_percent = 50

src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("titlr",src)

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
#cv2.waitKey(0)