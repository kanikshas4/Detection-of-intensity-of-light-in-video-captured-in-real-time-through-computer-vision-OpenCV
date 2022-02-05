#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import glob
import cv2
import numpy as np
import cvzone
import matplotlib.pyplot as plt
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector= FaceMeshDetector(maxFaces=1)




while(True):
    
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (640, 360))
    frame,faces= detector.findFaceMesh(frame)
    
    thresh=0.5
    
    frame= frame/np.max(frame)
    
    
    
   
        
        
    
    
    
    def isbrightF():
        if np.mean(frame) > thresh:
            cvzone.putTextRect(frame, 'bright', (50, 150), scale=1.5,
                           colorR=(255, 0, 255))
            
            color=(0,128,0)
            stroke=2
            start_point = (10, 10)
            end_point = (630, 350)
            
            cv2.rectangle(frame,start_point,end_point,color,stroke)
            
        else:
            cvzone.putTextRect(frame, 'dark', (50, 150), scale=1.5,
                           colorR=(255, 0, 255))
            cvzone.putTextRect(frame, 'increase the intensity of light', (50, 250), scale=1.5,
                           colorR=(255, 0, 255))
            color=(255,69,0)
            stroke=2
            start_point = (10, 10)
            end_point = (630, 350)
            
            cv2.rectangle(frame,start_point,end_point,color,stroke)
            
            
            
            
                
            
            
    isbrightF()
    
    
    
    
    cv2.imshow('frame',frame)
    
    
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
    
    
    
    



cap.release()
cv2.destroyAllWindows()


# In[ ]:




