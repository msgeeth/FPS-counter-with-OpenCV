import cv2
vid_capture = cv2.VideoCapture(r'C:\Users\Lenovo\Desktop\Car.mp4')

if (vid_capture.isOpened()== False):
    print("Error when opening the video")
else:
    fps = vid_capture.get(5)
    print('Frames per second:',fps,'FPS')

    frame_count= vid_capture.get(7)
    print('Frame count : ',frame_count)

while(vid_capture.isOpened()):
    ret,frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        key = cv2.waitKey(20)

        if key == ord('q'):
            break
        else:
            break
#reselasing the video obj
vid_capture.release()
cv2.destroyAllWindows()