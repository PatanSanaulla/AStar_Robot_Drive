import sys


print("Enter the two rpms: ")
rpm1 = input(int())
rpm2 = input(int())

actionMoves = [0, rpm1, rpm2]

move1 = [0,  rpm1]
move2 = [rpm1, 0]
move3 = [rpm1, rpm1]
move4 = [0, rpm2]
move5 = [rpm2, 0]
move6 = [rpm2, rpm2]
move7 = [rpm1, rpm2]
move8 = [rpm2, rpm1]

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

