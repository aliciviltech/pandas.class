import cv2
import winsound as ws
xyz = cv2.VideoCapture(0)
total = 0
while (True):
    ret , frame = xyz.read()
    abc = cv2.QRCodeDetector()
    v1, v2, v3 = abc.detectAndDecode(frame)
    if (v1 != ""):
        print(v1)
        if (v1 == 'Keyboard'):
            total += 500
            print(total)
        elif (v1 == 'CPU'):
        ws.beep(1000,1000)

    cv2.imshow('img1', frame)

    if (cv2.waitKey(200) == 27):
        break


xyz.release()
cv2.destroyAllWindows()