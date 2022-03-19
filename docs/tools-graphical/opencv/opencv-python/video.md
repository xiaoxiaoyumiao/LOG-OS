# Video

以下代码从指定文件中读入视频数据帧，每一帧为一个图片对象（ndarray）。

```python
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
```

## Reference

\[1\] [https://docs.opencv.org/master/dd/d43/tutorial\_py\_video\_display.html](https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html)

