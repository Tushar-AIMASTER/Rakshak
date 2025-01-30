# **RAKSHAK D.S. Drowsiness Detector - Python Project with GUI**


*This Python project implements a drowsiness detection system using facial landmark recognition and eye aspect ratio (EAR). It also includes a graphical user interface (GUI) for ease of use and Web Application*

**Project Name: RAKSHAK D.S.**

**Team: ANARGHYA**

**Developer: Tushar Srivastava**

## **Description:**

This program detects drowsiness in real-time by analyzing the eye aspect ratio (EAR) of the driver using computer vision techniques. The EAR is a metric that measures the distance between the vertical points of the eye relative to the horizontal distance between the eye corners. When a driver is drowsy, their eyelids tend to droop, which decreases the EAR.

The program utilizes OpenCV and dlib libraries for facial landmark detection and eye aspect ratio calculation. It also includes functionalities like:

GUI with functionalities to start/stop detection and view history.
Audio and visual alerts for drowsiness detection.
Recording timestamps of drowsiness detection events in a text file for history tracking.
This project implements a real-time drowsiness detection system using computer vision techniques. It captures video from the webcam, analyzes the eye aspect ratio (EAR) to detect drowsiness, and triggers an alert (sound and visual) if the driver appears to be falling asleep.  It also logs drowsiness events to a text file and provides reminders to take breaks.  


## Features

* **Real-time Drowsiness Detection:**  Utilizes the Eye Aspect Ratio (EAR) to accurately detect eye closure, a key indicator of drowsiness.
* **Alert System:** Triggers both a sound alert (beep) and a visual alert ("DROWSINESS DETECTED" on the screen) when drowsiness is detected.  Also increases system volume for the alert per beep.
* **Drowsiness Logging:** Records the date and time of each drowsiness event in a "History.txt" file.
* **Break Reminders:**  Provides reminders to take breaks every (configurable) time interval.
* **Web Interface:**  Streams the video feed with drowsiness detection overlay to a web page using Flask.
* **Configurable Parameters:**  Allows for adjustment of EAR threshold and consecutive frame count for drowsiness detection.


The **WEB application** is built using Python, OpenCV, dlib, and Flask.

and their is GUI Version also, built using Python, OpenCV, dlib, and PyQt5.


# How to Run:
## Install the Dependencies
**Ensure you have the following libraries installed:**
* Python 3
* OpenCV (cv2)
* dlib
* imutils
* scipy
* numpy
* winsound (Windows)
* pyautogui
* pyttsx3
* datetime
* speech_recognition
* Flask
* PyQt5

You can also use the code below


    pip install -r requirements.txt 
    

**Download the shape predictor:**
    Download the shape_predictor_68_face_landmarks.dat file from https://github.com/Tushar-AIMASTER/Rakshak/blob/main/shape_predictor_68_face_landmarks.dat and place it in the same directory as the Python script.

## **Run the script using Python:**
Via cmd:

    python main.py
## **GUI Usage:**

The GUI provides two main functionalities:

**Start:** Click this button to initiate the drowsiness detection process. The program will access your webcam and analyze your facial features.
History: Click this button to open the text file containing the timestamps of drowsiness detection events.


## **Run the Flask application:**
    python app.py  
### Open the web interface:
Navigate to http://127.0.0.1:5501/ in your web browser.  (The port might be different if you changed it in the code.)

Drowsiness detection: The system will start detecting drowsiness in real-time.

# **Note:**

*This is a basic implementation of a drowsiness detection system. Further enhancements can be made to improve accuracy and robustness.
We can even integrate this system in vehicles with FPGA and Arduino
 boards.*



#### CODE: [GITHUB](https://github.com/Tushar-AIMASTER/Rakshak)

## **Problem Statement:**
**Who:**
Drivers: Primarily professional drivers (truckers, bus drivers, delivery personnel) who face long hours, monotonous routes, and potential fatigue.
Fleets: Companies operating fleets of vehicles (transportation companies, logistics firms) seeking to improve driver safety and reduce accidents.

**What:**
Drowsiness-related accidents: These accidents are a significant cause of road fatalities, injuries, and property damage.
Lack of real-time driver monitoring: Existing safety measures may be insufficient (e.g., breaks, regulations) in preventing accidents caused by driver fatigue.
Inefficient safety protocols: Current methods for detecting drowsiness (e.g., driver logs) may be unreliable and difficult to enforce.

**When:**
During long drives: Especially during night shifts, early morning hours, or after extended periods of monotonous driving.
In situations of driver fatigue: Such as after insufficient sleep, extended work hours, or while under the influence of medication.

**Where:**
Commercial vehicles: Trucks, buses, delivery vans, and other vehicles used for professional driving.
Private vehicles: Potentially applicable to private vehicles, especially for long-distance travel or for drivers with known sleep disorders.

## **Key Problem Statement:**
*"How might we effectively detect and prevent drowsiness in drivers of commercial and potentially private vehicles, thereby reducing the occurrence of accidents caused by driver fatigue"*
