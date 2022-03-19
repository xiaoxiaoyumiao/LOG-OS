# GUI & Event System

## Painting

```python
# draw rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
"""
img - the image to draw on (but its content will not be modified)
(384, 0) - the top-left point
(510, 128) - the bottom-right point
    notice: The point is in the screen coordinate, that is, (column, row)
(0, 255, 0) - color, this is green.
3 - width of lines, negative for filling
"""

```

## Event System

以下代码可以读取一个视频文件并播放，在按下 p 时暂停，按下 c 时继续播放，按下 q 时退出播放；暂停时可以通过鼠标拖拽在当前画面上绘制矩形框。代码中展示了如何处理鼠标和键盘事件。

```python
import sys
import argparse
import numpy as np
import cv2 as cv

class ClickHandler:
    x_start = 0
    y_start = 0
    x_end = 0
    y_end = 0
    image = None
    output = None
    drawing = False
    def __init__(self, image):
        self.image = image
        self.output = np.copy(self.image)

    def get_mouse_callback(self):
        return self._mouse_callback

    def _mouse_callback(self, event, x, y, flags, param):
        
        if event == cv.EVENT_LBUTTONDOWN:
            self.output = np.copy(self.image)
            self.x_start, self.y_start = x, y
            self.drawing = True
        elif event == cv.EVENT_MOUSEMOVE:
            if self.drawing:
                self.x_end, self.y_end = x, y
                self.output = np.copy(self.image)
                cv.rectangle(self.output, 
                    (self.x_start, self.y_start),
                    (self.x_end, self.y_end), 
                    (0, 255, 0), 4)
        elif event == cv.EVENT_LBUTTONUP:   
            self.drawing = False
            print((self.x_start, self.y_start),
                    (self.x_end, self.y_end))


def interactive_labeling(video_path):
    cap = cv.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame)
        key = cv.waitKey(100)
        if key == ord('q'):
            break
        elif key == ord('p'):
            print("frame count: ", frame_count)
            handler = ClickHandler(frame)
            cv.setMouseCallback('frame', handler.get_mouse_callback())
            cv.imshow('frame', frame)
            while (cv.waitKey(1) != ord('c')):
                cv.imshow('frame', handler.output)
        frame_count += 1

    cap.release()
    cv.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, default="../resource/cars.avi", 
                        help="Path to the analyzed video.")
    args = parser.parse_args()
    interactive_labeling(args.path)

if __name__ == "__main__":
    main()
```

## Reference

\[1] [https://docs.opencv.org/master/dc/da5/tutorial\_py\_drawing\_functions.html](https://docs.opencv.org/master/dc/da5/tutorial\_py\_drawing\_functions.html)

\[2] [https://docs.opencv.org/master/db/d5b/tutorial\_py\_mouse\_handling.html](https://docs.opencv.org/master/db/d5b/tutorial\_py\_mouse\_handling.html)

\[3] [https://docs.opencv.org/3.4/d3/d96/tutorial\_basic\_geometric\_drawing.html](https://docs.opencv.org/3.4/d3/d96/tutorial\_basic\_geometric\_drawing.html)
