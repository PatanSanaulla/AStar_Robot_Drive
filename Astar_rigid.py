import sys
import math
import time
from MapInfo import *

# Global Variables
START_POINT = []        # [x, y]
GOAL_POINT = []         # [x, y]
EXPLORED = {}           # x,y,theta and Index
RADIUS = 10.5              # Default Radius 105mm
STEP_OBJECT_LIST = []
COST_MAP_DICT = {}      # Index and Cost
r = 3.3                 # 0.038 3.8
L = 16.0                # 0.354 35.4

# Definition of Class Step:
class Step:
    # Method to initialize the node with the values/attributes and add the step
    # self: Object of class step
    # parent: Object of class step
    # position: the x,y values of the current step
    # cost: cost of the step to move from the parent to the current position
    def __init__(self, parent, position, angle):

        self.position = position  # [x, y]
        self.parent = parent
        self.angle = angle  # angle % (2 * math.pi)
        if parent == None:
            self.costToCome = 0.0
        else:
            self.costToCome = parent.costToCome + abs((parent.position[0]-position[0])**2 - (parent.position[1]-position[1])**2) ** 0.5  # cost
        self.cost = self.costToCome + float(
            ((GOAL_POINT[0] - self.position[0]) ** 2 + (GOAL_POINT[1] - self.position[1]) ** 2) ** (
                0.5))  # Euclidean Distance
        print("creating a new step with", position, "and angle: ", angle, "and cost", self.cost)
        self.addToGraph()

    def addToGraph(self):
        key = str(self.position[0]) + "," + str(self.position[1]) + "," + str(self.angle)
        value = EXPLORED.get(key)
        if value == None:  # Not Visited
            EXPLORED.update({key: len(STEP_OBJECT_LIST)})
            COST_MAP_DICT.update({len(STEP_OBJECT_LIST): self.cost})
            STEP_OBJECT_LIST.append(self)
        # else:
        #     if self.cost < STEP_OBJECT_LIST[value].cost: # COST_MAP_DICT.get(value):
        #         EXPLORED.update({key: len(STEP_OBJECT_LIST)})
        #         COST_MAP_DICT.update({len(STEP_OBJECT_LIST): self.cost})
        #         STEP_OBJECT_LIST.append(self)

    def generateSteps(self):
        for move in MOVES_LIST:
            t = 0
            dt = 0.1  # 0.1
            newX = self.position[0]
            newY = self.position[1]
            newAngle = 3.14 * self.angle / 180

            # Xi, Yi,Thetai: Input point's coordinates
            # Xs, Ys: Start point coordinates for plot function
            # Xn, Yn, Thetan: End point coordintes
            while t < 1:
                t = t + dt
                Xs = self.position[0] # to remove
                Ys = self.position[1] # to remove
                newX += (r * 0.5) * (move[0] + move[1]) * math.cos(newAngle) * dt
                newY += (r * 0.5) * (move[0] + move[1]) * math.sin(newAngle) * dt
                newAngle += (r / L) * (move[0] - move[1]) * dt

                newAngle = thresholding(180 * newAngle / 3.14)
                if newAngle < 0:
                    newAngle = newAngle + 360
                if newAngle > 360:
                    newAngle = newAngle % 360
                newPosition = [thresholding(newX), thresholding(newY)]
                if newX >= -MAX_X and newX <= MAX_X and newY >= -MAX_Y and newY <= MAX_Y and (
                        isValidStep(newPosition, RADIUS + CLEARANCE) == True):
                    try:
                        if (self.parent.position == newPosition):
                            pass
                        else:
                            plt.plot([Xs, newX], [Ys, newY], color="blue")
                            newStep = Step(self, newPosition, newAngle)
                    except AttributeError:
                        plt.plot([Xs, newX], [Ys, newY], color="blue")
                        newStep = Step(self, newPosition, newAngle)
                else:
                    pass


def backtrack(stepObj):
    pathValues = []
    while stepObj.parent != None:
        pathValues.append([stepObj.position[0], stepObj.position[1], stepObj.angle])
        stepObj = stepObj.parent
    pathValues.append([stepObj.position[0], stepObj.position[1], stepObj.angle])

    pathValues.reverse()
    x = []
    y = []
    for each in pathValues:
        x.append(each[0])
        y.append(each[1])
    plt.plot(x, y, color="red")
    showPath()
    print("length of step_object_list", len(STEP_OBJECT_LIST))
    print("length of the pathvalues", len(pathValues))
    print(pathValues)


def inGoal(position):
    x, y = position[0], position[1]
    if ((x - GOAL_POINT[0]) ** 2 + (y - GOAL_POINT[1]) ** 2 <= (1.5) ** 2):
        return True
    else:
        return False


def thresholding(val):
    splitData = str(val).split('.')
    intData = int(splitData[0])
    decimalData = int(splitData[1][0])
    if decimalData > 7:
        return intData + 1.0
    else:
        if decimalData > 2:
            return intData + 0.5
        else:
            return intData + 0.0


try:
    startPoints = input("Enter the Start Points (x,y,theta) position: ")
    START_POINT = [int(each) for each in startPoints.split(" ")]
    # Start or goal points have 3 Values: START_POINT[0] -> x, START_POINT[1] -> y, and START_POINT[2] -> theta
    goalPoints = input("Enter the Goal Points (x,y) position: ")
    GOAL_POINT = [int(each) for each in goalPoints.split(" ")]
    rpm = input("Enter the RPM Values for the robot: ")
    RPM_LIST = [int(each) for each in rpm.split(" ")]  # NEED TO CHANGE IF THE RPM ARE FLOAT VALUES
    rpm1 = RPM_LIST[0]
    rpm2 = RPM_LIST[1]
    MOVES_LIST = [[0, rpm1], [rpm1, 0], [rpm1, rpm1], [0, rpm2], [rpm2, 0], [rpm2, rpm2], [rpm1, rpm2], [rpm2, rpm1]]
    CLEARANCE = int(input("Enter the Clearance of the robot: "))
    print(MOVES_LIST)

except:
    print("Please enter the proper points: Example: 200 30 30")
    print("Exiting the Algorithm")
    sys.exit(0)

isPossible = 0

if START_POINT[0] >= -MAX_X and START_POINT[0] <= MAX_X and START_POINT[1] >= -MAX_Y and START_POINT[1] <= MAX_Y and (
        isValidStep(START_POINT, RADIUS + CLEARANCE) == True):
    isPossible += 1
else:
    print("Invalid Start Point")

if GOAL_POINT[0] >= -MAX_X and GOAL_POINT[0] <= MAX_X and GOAL_POINT[1] >= -MAX_Y and GOAL_POINT[1] <= MAX_Y and (
        isValidStep(GOAL_POINT, RADIUS + CLEARANCE) == True):
    isPossible += 1
else:
    print("Invalid Goal Point")

# To check if both the values are possible to work with in the puzzle
if isPossible == 2:
    root = Step(None, START_POINT[:2], START_POINT[2])  # Starting the linked list with start point as the root

    start_time = time.time()
    while True:  # to keep traversing until the goal area is found
        topKey = next(iter(COST_MAP_DICT))
        COST_MAP_DICT.pop(topKey)
        poppedStep = STEP_OBJECT_LIST[topKey]
        if inGoal(poppedStep.position) == True:
            break
        else:
            poppedStep.generateSteps()
            COST_MAP_DICT = {index: totalcost for index, totalcost in sorted(COST_MAP_DICT.items(), key=lambda cost: cost[1])} # EXPLORED.sort()

    end_time = time.time()

    print("Total Cost to reach the final Point:", poppedStep.costToCome)

    print("total time for A star in seconds: ", end_time - start_time)
    backtrack(poppedStep)  # To show the backtrack on the graph

else:
    print("Exiting the Algorithm")
    sys.exit(0)
