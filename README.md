# Rakshak
RAKSHAK : Drowsiness Detection System built to save lives.
# **RAKSHAK D.S. Drowsiness Detector - Python Project with GUI**


*This Python project implements a drowsiness detection system using facial landmark recognition and eye aspect ratio (EAR). It also includes a graphical user interface (GUI) for ease of use.*

**Project Name: RAKSHAK D.S.**

**Team: ANARGHYA**

**Developer: Tushar Srivastava**

## **Description:**

This program detects drowsiness in real-time by analyzing the eye aspect ratio (EAR) of the driver. The EAR is a metric that measures the distance between the vertical points of the eye relative to the horizontal distance between the eye corners. When a driver is drowsy, their eyelids tend to droop, which decreases the EAR.

The program utilizes OpenCV and dlib libraries for facial landmark detection and eye aspect ratio calculation. It also includes functionalities like:

GUI with functionalities to start/stop detection and view history.
Audio and visual alerts for drowsiness detection.
Recording timestamps of drowsiness detection events in a text file for history tracking.
How to Run:

**Ensure you have the following libraries installed:**

- OpenCV
- dlib
- PyQt5
- pyttsx3
- imutils
- Download the project files, including the Python script (main.py) and the shape predictor file (shape_predictor_68_face_landmarks.dat).

## **Run the script using Python:**

### Bash

*python main.py*
## **GUI Usage:**

The GUI provides two main functionalities:

**Start:** Click this button to initiate the drowsiness detection process. The program will access your webcam and analyze your facial features.
History: Click this button to open the text file containing the timestamps of drowsiness detection events.
# **Note:**

*This is a basic implementation of a drowsiness detection system. Further enhancements can be made to improve accuracy and robustness.
We can even integrate this system in vehicles with FPGA and Arduino
 boards.*


Demonstration Link: [Video](https://youtu.be/CTGr3dqklb4)
CODE: [GITHUB](https://github.com/Tushar-AIMASTER/Rakshak)

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
