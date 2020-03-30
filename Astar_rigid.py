import sys
import math
import time
from MapInfo import *

# Global Variables
START_POINT = []  # [x, y]
GOAL_POINT = []  # [x, y]
EXPLORED = []
VISITED = []
RADIUS = 0  # Default Radius
THRESHOLD = 0.5
STEP_OBJECT_LIST = []
COST_MAP_DICT = {}
STEP_SIZE = 1  # Default step size
THETA = math.pi / 6  # Default 30 degrees
r = 0.038
L = 0.354


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
        self.xPoint = int(position[0] / THRESHOLD) - 1
        self.yPoint = int(position[1] / THRESHOLD) - 1
        self.anglePoint = int((math.ceil(angle) % math.pi) / THETA)  # (int(angle/THETA)%12)-1
        # self.costMapIndex = len(COST_MAP)
        if parent == None:
            self.costToCome = 0.0
        else:
            self.costToCome = parent.costToCome + 1 # cost
        self.cost = self.costToCome + 2 * float(
            ((GOAL_POINT[0] - self.position[0]) ** 2 + (GOAL_POINT[1] - self.position[1]) ** 2) ** (
                0.5))  # Euclidean Distance
        print("creating a new step with", position, "and angle: ", angle, "and cost", self.cost)
        self.addToGraph()

    def __lt__(self, other):
        return self.cost < other.cost

    def addToGraph(self):
        # if not self.isVisited():
        #     self.visitStep()
            EXPLORED.append(self)
            STEP_OBJECT_LIST.append(self)

        # else:
        #     # it is visited hence finding its cost and current index
        #     pointKeys = list(COST_MAP_DICT.keys())
        #     costValues = list(COST_MAP_DICT.values())
        #     index = pointKeys.index((self.xPoint, self.yPoint, self.anglePoint))
        #     if self.cost < costValues[index]:
        #         try:
        #             EXPLORED.remove(STEP_OBJECT_LIST[index])
        #         except:
        #             pass  # not present to remove form the list
        #         self.visitStep()
        #         EXPLORED.append(self)

    def isVisited(self):
        if VISITED[self.xPoint][self.yPoint][self.anglePoint] == 0:
            return False
        else:
            return True

    def visitStep(self):
        VISITED[self.xPoint][self.yPoint][self.anglePoint] = 1
        COST_MAP_DICT[(self.xPoint, self.yPoint, self.anglePoint)] = self.cost

    def generateSteps(self):
        # EXPLORED.append(self)
        # for i in [-30, -(math.pi / 6), 0, (math.pi / 6), (math.pi / 3)]:
        #     angle = i + self.angle
        #     newX = thresholding((math.cos(angle) * STEP_SIZE) + self.position[0])
        #     newY = thresholding((math.sin(angle) * STEP_SIZE) + self.position[1])
        for move in MOVES_LIST:
            t = 0
            dt = 1 #0.1
            newX = self.position[0]
            newY = self.position[1]
            newAngle = 3.14 * self.angle / 180

            # Xi, Yi,Thetai: Input point's coordinates
            # Xs, Ys: Start point coordinates for plot function
            # Xn, Yn, Thetan: End point coordintes
            while t < 1:
                t = t + dt
                # Xs = newX
                # Ys = newY
                newX += r * (move[0] + move[1]) * math.cos(newAngle) * dt
                newY += r * (move[0] + move[1]) * math.sin(newAngle) * dt
                newAngle += (r / L) * (move[0] - move[1]) * dt
                #plt.plot([Xs, Xn], [Ys, Yn], color="blue")
                
                newAngle = 180 * newAngle / 3.14
                newPosition = [newX, newY]
                if newX >= -MAX_X and newX <= MAX_X and newY >= -MAX_Y and newY <= MAX_Y and (
                        isValidStep(newPosition, RADIUS + CLEARANCE) == True):
                    try:
                        if (self.parent.position == newPosition):
                            pass
                        else:
                            newStep = Step(self, newPosition, newAngle)  # cost 1.0
                    except AttributeError:
                        newStep = Step(self, newPosition, newAngle)  # cost 1.0
                else:
                    pass


def backtrack(stepObj):
    pathValues = []
    while stepObj.parent != None:
        pathValues.append([stepObj.position[0], stepObj.position[1], stepObj.angle])
        stepObj = stepObj.parent
    pathValues.append([stepObj.position[0], stepObj.position[1], stepObj.angle])

    pathValues.reverse()
    print("length of step_object_list", len(STEP_OBJECT_LIST))
    print("length of the pathvalues", len(pathValues))
    showPath(START_POINT, GOAL_POINT, STEP_OBJECT_LIST, pathValues)


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
    

    VISITED = [[[0 for i in range(int(2 * math.pi / THETA))] for j in range(int(MAX_Y / THRESHOLD))] for k in
               range(int(MAX_X / THRESHOLD))]

    root = Step(None, START_POINT[:2], START_POINT[2]) # Starting the linked list with start point as the root

    start_time = time.time()
    while True:  # to keep traversing until the goal area is found
        eachStep = EXPLORED.pop(0)
        # print(eachStep.position, math.degrees(eachStep.angle))
        eachStep.generateSteps()
        EXPLORED.sort()
        break

        if inGoal(eachStep.position) == True:
            break
    end_time = time.time()
    # while True:
    #	eachStep = STEP_OBJECT_LIST.pop(0) #to Keep popping until a unvisted node is found
    #	if eachStep.isVisited() == False:
    #		break

    print("Total Cost to reach the final Point:", eachStep.costToCome)
    # stepsTakenToCompute() #Once the whole generation is completed begin the animation

    # now = datetime.now().time()
    print("total time for A star in seconds: ", end_time - start_time)
    # backtrack(eachStep)  # To show the backtrack on the graph

else:
    print("Exiting the Algorithm")
    sys.exit(0)
