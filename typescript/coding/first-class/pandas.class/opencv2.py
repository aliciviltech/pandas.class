import cv2

obj = cv2.VideoCapture(0)

while (True):
    _, img = obj.read()
    cv2.circle('img', (300,200), 50 , (100,100,200),4 )

    cv2.imgshow('win', img)

    if (cv2.waitKey(200) == 27):
        break

# xyz.release()
# cv2.destroyAllWindows()