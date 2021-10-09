import time
import cv2
import numpy as np
from display import Display
from extractor import Extractor


W=1920//2
H=1080//2

disp=Display(W, H)
fe=Extractor()

#uses to resize the image and call function from Display class
def process_frame(img):
    img=cv2.resize(img,(W,H))
    matches=fe.extract(img)


    for pt1,pt2 in matches:
        u1,v1=map(lambda x:int(round(x)),pt1)
        u2, v2 = map(lambda x: int(round(x)), pt2)
        cv2.circle(img,(u1,v1),2,(0,255,0),3)
        cv2.line(img,(u1,v1),(u2,v2),color=(0,255,0))

   # if matches is None:
   #     return

    # for p in kps:
    #     print(p)
    #     u,v=map(lambda x: int(round(x)),p.pt)
    #     img=cv2.circle(img,(u,v),2,(0,255,0),1)

    disp.paint(img)

#main method
if __name__=="__main__":
    cap=cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret,frame=cap.read()
        if ret == True:
            #call process_frame method
            process_frame(frame)
        else:
            break
