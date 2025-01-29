import scipy
import numpy as np
from scipy.spatial import distance as dist
from imutils import face_utils 
import imutils
import dlib
import cv2
import winsound
import time
import pyttsx3
import datetime
import speech_recognition as sr
import os
import sys
import pyautogui
from datetime import datetime as dt
from datetime import date as d
import glob
import os.path
import webbrowser
from flask import Flask,render_template,Response


frequency = 2500
duration = 1000 # here 1000 resemble 1 second


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

app=Flask(__name__)
 
def detectionFunction():
    # Creating the function to get the eye aspect ratio:
    def eyeAspectRatio(eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        # Here ear mean eye aspect ratio
        ear = (A + B) / (2.0 * C)# This will give us the average & because we have two eyes therefore dividing by 2
        return ear
    

    # Creating a function to make the detector give reminder for breaks every 3 hours:
    def currentTime():
        return datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-%Hh/%Mm')

    three_Hour_Later = datetime.datetime.today() + datetime.timedelta(minutes=5) 
    three_h=datetime.datetime.strftime(three_Hour_Later , '%d/%m/%Y-%Hh/%Mm')
    # This functiion will make the detector speak & print to take a break: 
    def remind():
        text = "Please take a break, you have been driving the vehicle continously for 3 hours"
        print(text)
        speak(text)
    
    # Initializing some values to some variable
    count = 0
    earThresh = 0.3 # Distance between vertical eye coordinate Threshold
    earFrames = 45 # Consecutive frames for eye closure
    # Locating the predicitor file and assigning the variable
    shapePredictor = "shape_predictor_68_face_landmarks.dat"
    # This command will connect the camera for taking the input:
    cam = cv2.VideoCapture(0)
    # Loading the detector for the program:
    detector = dlib.get_frontal_face_detector()
    # Passing the algorithm file into the predicitor:
    predictor = dlib.shape_predictor(shapePredictor)

    # Getting  the coordinates of the  left & right eye
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    while True:
        # Reading the feed from the camera :
        _, frame = cam.read()
        # Resizing the images obtaining from the camera:
        frame = imutils.resize(frame, width=500)
        # converting the images into grayscale image for further processing:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        '''cv2.putText(frame, "press 'q' to exit", (270, 320),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 100, 255), 2)'''

        
        for rect in rects:
            shape = predictor(gray, rect)
            # here we are converting the points location in an array:
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eyeAspectRatio(leftEye)
            rightEAR = eyeAspectRatio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)
            
            # this will compare the current ear value with the predefined
            if ear < earThresh:
                count += 1

                if count >= earFrames:
                    cv2.putText(frame, "DROWSINESS DETECTED", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    winsound.Beep(frequency, duration) # This will create a beep sound
                    pyautogui.press("volumeup",presses=2) # This will increase the volume & intensity of sound
                    now = dt.now() # This get the time when drowisness was detected
                    current_time = now.strftime("%H:%M:%S")
                    today = d.today() # This get the current date
                    d2 = today.strftime("%B %d, %Y")
                    # This will check if text file exists or not , if exist then append new entries and if not exist then will create a new file to save info. 
                    if os.path.exists('History.txt')==True:
                        f = open("History.txt", "a")
                        f.write("\n  Drowisness Detected on "+d2+" at "+current_time+"\n")
                        f.close()
                    else:
                        with open('History.txt', 'w') as f:
                            f.write("\n  Drowisness Detected on "+d2+" at ",current_time+"\n")
                    print("Drowisness Detected on "+ d2+" at "+ current_time)
                    

            else:
                count = 0
                
        # This will take the keyboard input:
        key = cv2.waitKey(1) & 0xFF
        # To Close the pop up window which appear press "q" on the keyboard:
        if key == ord("q") or key == ord("Q"):# This line will take the input from the keyboard in the background & if it is "q" then the program will terminate.
            break
        # This will compare the current time with the re,=minder time :
        if currentTime()==three_h: # when the both with will equall then it will give the reminder.
            remind()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
            
    cam.release()
    cv2.destroyAllWindows()



    
    
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(detectionFunction(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug=True, port=5501)
