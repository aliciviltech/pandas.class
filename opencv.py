import cv2
xyz = cv2.VideoCapture(0)
while (True):
    ret , frame = xyz.read()
    abc = cv2.QRCodeDetector()
    v1, v2, v3 = abc.detectAndDecode(frame)
    if (v1 != ""):
        print(v1)

    cv2.imshow('img1', frame)

    if (cv2.waitKey(200) == 27):
        break

xyz.release()
cv2.destroyAllWindows()