import cv2
import numpy
from win32api import GetSystemMetrics
import pyautogui
import datetime

width,height = pyautogui.size()

format = cv2.VideoWriter_fourcc(*"XVID")

output= cv2.VideoWriter('input.mp4', format, 30.0, (width,height))

st = datetime.datetime.now()

endtime = st + datetime.timedelta(10)
try:
    while st < endtime:

        img = pyautogui.screenshot()
        frame = numpy.array(img)
        frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output.write(frame)

except KeyboardInterrupt:
    print("Interrupted by user.")
    output.release()
    cv2.destroyAllWindows()


