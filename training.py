import numpy as np
import cv2
import os

import face as fr


#Training will begin from here
faces,faceID=fr.labels_for_training_data(r"C:\Users\Roshan Jha\AppData\Local\Programs\Python\Python37\Face recognition Project\images")

face_recognizer=fr.train_Classifier(faces,faceID)
face_recognizer.save(r'C:\Users\Roshan Jha\AppData\Local\Programs\Python\Python37\Face recognition Project\trainingData.json') #It will save the trained model. Just give path to where you want to save
