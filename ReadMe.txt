# ENPM 661 - Planning for Autonomous Robots Project 3 (Phase 3)

## Authors

@ Nikhil Lal Kolangara (116830768)
@ Sanaulla Patan (116950985)

## Installation

-- Install all package dependencies like [matplotlib](https://matplotlib.org/users/installing.html) and [numpy](https://numpy.org/)
   and [OpenCV](https://opencv.org/) before running the code.

-- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matplotlib and other packages and to update all the packages to the latest versions.

'''bash
pip install matplotlib
'''

## Usage

'''python
import matplotlib.plyplot as plt
import numpy as np
plt.style.use('seaborn-pastel')
import cv2
'''

## Directory Structure

"proj3_group26_ros_python.zip" 										
 (Extract this compressed file to any desired folder) 					
	Folder Name after extraction: proj3_group26_ros_python
					|- Phase_3
					    |- Phase3_video.avi
					    |- Phase3.py
					    |- ReadMe.txt
					    |- MapInfo.py
					    |- README.md
					    |- Phase3_FinalOutput.png
						

## Intructions to run the files

-> Extract the "proj3_group26_ros_python.zip" to any desired folder.

-> 1. Using the Terminal:

NOTE: The coordinates are scaled by multiplying by 100

->-> Navigate to the "Phase_3" folder inside "proj3_group26_ros_python" folder, right click and select open terminal or command prompt here.
	*** use 'python3' instead of 'python' in the terminal if using Linux based OS ***
	Execute the files by using the following commands in command prompt or terminal:
	--python .\Phase3.py   
	-- Enter the Start Point parameters in single line terminal input as (-480, -480 ,60)
	-- Enter the Goal Point parameters in single line terminal input as (480, 480, no input or 0)
	-- Enter the Robot RPM as 5 and 5 (5 5)
	-- Enter the Robot Clearance as 5
	
-> 2. Using PyCharm IDE

	Open all the files in the IDE and click Run and select the "Phase3.py" to execute.
	-- Enter the Start Point parameters in single line terminal input as (-480, -480 ,60)
	-- Enter the Goal Point parameters in single line terminal input as (480, 480, no input or 0)
	-- Enter the Robot RPM as 5 and 5 (5 5)
	-- Enter the Robot Clearance as 5

## Sample Execution

'''bash

Enter the Start Points (x,y,theta) position: -480 -480 30
Enter the Goal Points (x,y) position: 470 470
Enter the RPM Values for the robot: 8 10
Enter the Clearance of the robot: 5
[[0, 8], [8, 0], [8, 8], [0, 10], [10, 0], [10, 10], [8, 10], [10, 8]]

Total Cost to reach the final Point: 686.1385915457098
total time for A star in seconds:  2.4936134815216064
length of step_object_list 2101
length of the pathvalues 804

'''

## Screenshots

![Final Output](Phase3_FinalOutput.png)

## Final Note

-> The Output file generated is 'Phase3_video.avi' video file. 
-> The video file generation takes more than an hour.


