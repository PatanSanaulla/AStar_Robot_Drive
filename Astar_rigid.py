import sys

try:
    startPoints = input("Enter the Start Points (x,y,theta) position: ")
    START_POINT = [int(each) for each in startPoints.split(" ")]
    # Start or goal points have 3 Values: START_POINT[0] -> x, START_POINT[1] -> y, and START_POINT[2] -> theta
    goalPoints = input("Enter the Goal Points (x,y) position: ")
    GOAL_POINT = [int(each) for each in goalPoints.split(" ")]
    rpm = int(input("Enter the RPM Values for the robot: "))
    RPM_LIST = [int(each) for each in goalPoints.split(" ")]  # NEED TO CHANGE IF THE RPM ARE FLOAT VALUES
    CLEARANCE = int(input("Enter the Clearance of the robot: "))

except:
    print("Please enter the proper points: Example: 200 30 30")
    print("Exiting the Algorithm")
    sys.exit(0)

