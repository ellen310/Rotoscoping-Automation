import cv2

videoFile='C:/Users/User/Videos/Captures/catVideo.mp4'
capture = cv2.VideoCapture(videoFile)

while(capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        video = cv2.resize(frame, dsize=(700, 480), interpolation=cv2.INTER_AREA)
        video_canny = cv2.Canny(video, 100, 200)
        cv2.imshow('out', video_canny)

        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()