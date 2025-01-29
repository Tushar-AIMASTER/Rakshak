

# Drowsiness Detector Project

### Project Title: RAKSHAK D.S.

#### Name: Tushar Srivastava
#### Team Name: ANARGHYA
# Installing the libraries needed for the Detector:

# Importing the Libraries:

import scipy
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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime as dt
from datetime import date as d
import glob
import os.path
import webbrowser
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)

# Initializing Beep Sound

frequency = 2500
duration = 1000 # here 1000 resemble 1 second

# Initializing Speak

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Buliding GUI & MAIN PROGRAM

# Creating G.U.I. with PyQt5
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(806, 604)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(226, 241, 255);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(210, 90, 450, 337))
        self.imageLbl.setStyleSheet("background-color: rgb(226, 241, 255);")
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 621, 37))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setGeometry(QtCore.QRect(140, 440, 151, 101))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.START.setFont(font)
        self.START.setStyleSheet("background-color: rgb(189, 236, 238);")
        self.START.setObjectName("START")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 440, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(560, 490, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 60, 211, 21))
        self.label_4.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.HISTORY = QtWidgets.QPushButton(self.centralwidget)
        self.HISTORY.setGeometry(QtCore.QRect(350, 440, 151, 101))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.HISTORY.setFont(font)
        self.HISTORY.setStyleSheet("background-color: rgb(189, 236, 238);")
        self.HISTORY.setObjectName("HISTORY")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.START.clicked.connect(self.detectionFunction)

        self.HISTORY.clicked.connect(self.historyFunction)
    def __init__(self):
        super().__init__()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "DROWSINESS DETECTOR"))
        self.START.setText(_translate("MainWindow", "START"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.label_4.setText(_translate("MainWindow", "CAMERA FEED"))
        self.HISTORY.setText(_translate("MainWindow", "HISTORY"))

    ##################################   MAIN PROGRAM TO DETECT DROWISNESS    ###################################

    def detectionFunction(self):
        self.textEdit.setText("Initializing...") # This will put text in status bar of GUI
        # This will get current working directory:
        path = os.getcwd()
        os.chdir(path)
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

        three_Hour_Later = datetime.datetime.today() + datetime.timedelta(minutes=1)
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
            frame = imutils.resize(frame, width=450)
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
                self.textEdit.setText("Detecting...")

                # this will compare the current ear value with the predefined
                if ear < earThresh:
                    count += 1

                    if count >= earFrames:
                        cv2.putText(frame, "DROWSINESS DETECTED", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        winsound.Beep(frequency, duration) # This will create a beep sound
                        pyautogui.press("volumeup",presses=5) # This will increase the volume & intensity of sound
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
                        self.textEdit.setText("Drowisness Detected")

                else:
                    count = 0
                    self.textEdit.setText("Detecting...")
            # This will dispaly the Detector's output interface:
            #cv2.imshow("DETECTOR", frame)


            image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_BGR888)
            self.imageLbl.setPixmap(QtGui.QPixmap.fromImage(image))
            # This will take the keyboard input:
            key = cv2.waitKey(1) & 0xFF
            # To Close the pop up window which appear press "q" on the keyboard:
            if key == ord("q") or key == ord("Q"):# This line will take the input from the keyboard in the background & if it is "q" then the program will terminate.
                break
            # This will compare the current time with the re,=minder time :
            if currentTime()==three_h: # when the both with will equall then it will give the reminder.
                remind()



        #These command will release the camera and close the window:
        cam.release()
        cv2.destroyAllWindows()
    def historyFunction(self):
        webbrowser.open("HISTORY.txt") # This will open the text file when History button is clicked on the GUI



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

