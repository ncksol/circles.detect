import numpy as np
import cv2

for x in range(1,6):    
    img = cv2.imread('circles%s.jpg' % x)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.medianBlur(gray, 25)

    minDist = 15 #100
    param1 = 30 #30
    param2 = 26 #21
    minRadius = 10 #40
    maxRadius = 30 #100

    #pink
    #minDist = 35 #100
    #param1 = 30 #30
    #param2 = 23 #21
    #minRadius = 35 #40
    #maxRadius = 50 #100

    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
 
    window_name = 'img' + str(x)
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(window_name, img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()