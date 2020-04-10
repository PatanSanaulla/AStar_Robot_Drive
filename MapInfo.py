import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import cv2

# import matplotlib.lines as mlines
plt.style.use('seaborn-pastel')
import numpy as np

# import math
# import cv2
# import glob

MAX_X = 500
MAX_Y = 500

plotSquare1 = np.array([(-325, 75), (-475, 75), (-475, -75), (-325, -75)], dtype='float')
plotSquare2 = np.array([(325, 75), (475, 75), (475, -75), (325, -75)], dtype='float')
plotSquare3 = np.array([(-275, 375), (-125, 375), (-125, 225), (-275, 225)], dtype='float')

plotCircle1 = [(100), (0, 0)]
plotCircle2 = [(100), (-200, -300)]
plotCircle3 = [(100), (200, -300)]
plotCircle4 = [(100), (200, 300)]

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(8.5, 6)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

axis = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-MAX_X, MAX_X), ylim=(-MAX_Y, MAX_Y))
font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_style('italic')
axis.set_xlabel('x coordinate', fontproperties=font)
axis.set_ylabel('y coordinate', fontproperties=font)

axis.spines["top"].set_linewidth(2)
axis.spines["top"].set_capstyle("round")
axis.spines["bottom"].set_linewidth(2)
axis.spines["bottom"].set_capstyle("round")
axis.spines["left"].set_linewidth(2)
axis.spines["left"].set_capstyle("round")
axis.spines["right"].set_linewidth(2)
axis.spines["right"].set_capstyle("round")

def solveLine(obsCoords1, obsCoords2, x, y):
    x1 = obsCoords1[0]
    y1 = obsCoords1[1]

    x2 = obsCoords2[0]
    y2 = obsCoords2[1]

    if y1 == y2:
        line = y - y2
        return line
    if x1 == x2:
        line = x - x2
        return line
    line = (y - y2) - ((x - x2) * (y1 - y2)) / (x1 - x2)
    return line

def circleOne(x, y, clearance):
    if ((x - 0) ** 2 + (y - 0) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def circleTwo(x, y, clearance):
    if ((x - (-200)) ** 2 + (y - (-300)) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def circleThree(x, y, clearance):
    if ((x - 200) ** 2 + (y - (-300)) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def circleFour(x, y, clearance):
    if ((x - 200) ** 2 + (y - 300) ** 2 - (100 + clearance) ** 2) <= 0:
        return False
    else:
        return True


def squareOne(x, y, clearance):
    if (y >= -75 - clearance) and (y <= 75 + clearance) and (x >= -475 - clearance) and (x <= -325 + clearance):
        return False
    else:
        return True

def squareTwo(x, y, clearance):
    if (y >= -75 - clearance) and (y <= 75 + clearance) and (x >= 325 - clearance) and (x <= 475 + clearance):
        return False
    else:
        return True


def squareThree(x, y, clearance):
    if (y >= 225 - clearance) and (y <= 375 + clearance) and (x >= -275 - clearance) and (x <= -125 + clearance):
        return False
    else:
        return True


def isValidStep(position, clearance):
    x = position[0]
    y = position[1]
    if circleOne(x, y, clearance) and circleTwo(x, y, clearance) and circleThree(x, y, clearance) and circleFour(x, y,
                                                                                                                 clearance) and squareOne(
            x, y, clearance) and squareTwo(x, y, clearance) and squareThree(x, y, clearance):
        return True
    else:
        return False


def showPath(STEP_OBJECT_LIST, pathValues):
    count = 0
    circle1 = plt.Circle((plotCircle1[1]), plotCircle1[0], fc=None)
    circle2 = plt.Circle((plotCircle2[1]), plotCircle2[0], fc=None)
    circle3 = plt.Circle((plotCircle3[1]), plotCircle3[0], fc=None)
    circle4 = plt.Circle((plotCircle4[1]), plotCircle4[0], fc=None)
    square1 = plt.Polygon(plotSquare1)
    square2 = plt.Polygon(plotSquare2)
    square3 = plt.Polygon(plotSquare3)
    obstacles = [circle1, circle2, circle3, circle4, square1, square2, square3]

    for item in obstacles:
        axis.add_patch(item)
    #
    # xTracepoint1 = []
    # yTracepoint2 = []
    #
    # yTracepoint1 = []
    # xTracepoint2 = []
    #
    # xTrackpoint1 = []
    # yTrackpoint1 = []
    #
    # xTrackpoint2 = []
    # yTrackpoint2 = []
    #
    # imageList = []
    #
    # framerate = 50
    # for itr in range(1, len(STEP_OBJECT_LIST)):
    #     try:
    #         startTrace = STEP_OBJECT_LIST[itr * framerate].parent
    #         xTracepoint1 = startTrace.position[0]
    #         yTracepoint1 = startTrace.position[1]
    #         xTracepoint2 = STEP_OBJECT_LIST[itr * framerate].position[0] - startTrace.position[0]
    #         yTracepoint2 = STEP_OBJECT_LIST[itr * framerate].position[1] - startTrace.position[1]
    #         axis.quiver(xTracepoint1, yTracepoint1, xTracepoint2, yTracepoint2, units='xy', scale=1, color='blue')
    #         plt.savefig("./images/frame" + str(count) + ".png", dpi = 200)
    #         imageList.append("images/frame" + str(count) + ".png")
    #         # print(len(STEP_OBJECT_LIST))
    #         print("count:", count)
    #         count = count + 1
    #     except:
    #         break
    #
    # for itr in range(1, len(pathValues)):
    #     try:
    #         xTrackpoint1 = pathValues[itr][0]
    #         yTrackpoint1 = pathValues[itr][1]
    #         xTrackpoint2 = pathValues[itr + 1][0] - pathValues[itr][0]
    #         yTrackpoint2 = pathValues[itr + 1][1] - pathValues[itr][1]
    #         axis.quiver(xTrackpoint1, yTrackpoint1, xTrackpoint2, yTrackpoint2, units='xy', scale=1, color='red')
    #         plt.savefig("./images/frame" + str(count) + ".png", dpi=200)
    #         imageList.append("images/frame" + str(count) + ".png")
    #         print("count:", count)
    #         count = count + 1
    #     except:
    #         break
    #
    # output = cv2.VideoWriter("Simulation_Video.avi", cv2.VideoWriter_fourcc(*'XVID'), 20.0, (500, 300))
    # for image in imageList:
    #     display = cv2.imread(image)
    #     display = cv2.resize(display, (500, 300))
    #     output.write(display)
    # output.release()

    plt.show()

