# Driver Drowsiness Detection System

## Introduction
This repository contains the code for a Driver Drowsiness Detection System created using Python and OpenCV.
The system utilizes computer vision techniques to detect the driver's eye aspect ratio and mouth yawning in real-time. By monitoring these facial features, the system can predict whether the driver is 
becoming drowsy and issue alerts accordingly.

## Requirements
- Python 3.x
- OpenCV (cv2)

  ## Algorithm
The Driver Drowsiness Detection System utilizes the following algorithm:
- **Eye Aspect Ratio (EAR)**: Calculates the ratio of distances between the vertical eye landmarks and the distances between the horizontal eye landmarks. A decrease in EAR below a certain threshold indicates that the driver's eyes are closing, potentially due to drowsiness.
- **Mouth Yawning Detection**: Detects changes in the mouth's shape, specifically the degree of yawning. A significant increase in mouth yawning beyond a threshold suggests that the driver may be drowsy.
