import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
plt.style.use('seaborn-pastel')
import numpy as np
import math
import cv2
import glob

MAX_X = 5
MAX_Y = 5

def solveLine(obsCoords1, obsCoords2, x, y):
    x1 = obsCoords1[0]
    y1 = obsCoords1[1]

    x2 = obsCoords2[0]
    y2 = obsCoords2[1]

    if y1 == y2:
        slope = y - y2
        return slope
    if x1 == x2:
        slope = x - x2
        return slope
    slope = (y - y2) - ((x - x2) * (y1 - y2)) / (x1 - x2)
    return slope


plotSquare1 = np.array([(-3.25, 0.75), (-4.75, 0.75), (-4.75, -0.75), (-3.25, -0.75)], dtype='float')
plotSquare2 = np.array([(3.25, 0.75), (4.75, 0.75), (4.75, -0.75), (3.25, -0.75)], dtype='float')
plotSquare3 = np.array([(-2.75, 3.75), (-1.25, 3.75), (-1.25, 2.25), (-2.75, 2.25)], dtype='float')

plotCircle1 = [(1), (0, 0)]
plotCircle2 = [(1), (-2, -3)]
plotCircle3 = [(1), (2, -3)]
plotCircle4 = [(1), (2, 3)]

square1Coords = np.array([(-3.25 - stretch, 0.75 + stretch), (-4.75 + stretch, 0.75 + stretch), (100 + stretch, 38.6 - stretch), (95 - stretch, 30 - stretch)], dtype='int')
square2Coords = np.array([(30 - stretch, 67.5 + stretch), (35 + stretch, 76 + stretch), (100 + stretch, 38.6 - stretch), (95 - stretch, 30 - stretch)], dtype='int')
square3Coords = np.array([(30 - stretch, 67.5 + stretch), (35 + stretch, 76 + stretch), (100 + stretch, 38.6 - stretch), (95 - stretch, 30 - stretch)], dtype='int')


def circleOne(x, y):
    if ((x - 0) ** 2 + (y - 0) ** 2 - 1 ** 2) <= 0:
        return False
    else:
        return True

def circleTwo(x, y):
    if ((x - (-2)) ** 2 + (y - (-3)) ** 2 - 1 ** 2) <= 0:
        return False
    else:
        return True

def circleThree(x, y):
    if ((x - 2) ** 2 + (y - (-3)) ** 2 - 1 ** 2) <= 0:
        return False
    else:
        return True

def circleFour(x, y):
    if ((x - 2) ** 2 + (y - 3) ** 2 - 1 ** 2) <= 0:
        return False
    else:
        return True

def squareOne():
    planeSquare1 = []
    for i in range(len(square1Coords)):
        if i == len(square1Coords) - 1:
            planeSquare1.append(solveLine(square1Coords[i], square1Coords[0], x, y))
            break
        planeSquare1.append(solveLine(square1Coords[i], square1Coords[i + 1], x, y))
    if (planeSquare1[0] <= 0 and planeSquare1[1] <= 0 and planeSquare1[2] >= 0 and planeSquare1[3] >= 0):
        flag = False
        return flag
    else:
        flag = True
        return flag

def squareTwo():
    planeSquare2 = []
    for i in range(len(rectangleCoords)):
        if i == len(rectangleCoords) - 1:
            planeRectangle.append(solveLine(rectangleCoords[i], rectangleCoords[0], x, y))
            break
        planeRectangle.append(solveLine(rectangleCoords[i], rectangleCoords[i + 1], x, y))
    if (planeRectangle[0] <= 0 and planeRectangle[1] <= 0 and planeRectangle[2] >= 0 and planeRectangle[3] >= 0):
        flag = False
        return flag
    else:
        flag = True
        return flag
    
def squareThree():
    planeSquare3 = []
    for i in range(len(rectangleCoords)):
        if i == len(rectangleCoords) - 1:
            planeRectangle.append(solveLine(rectangleCoords[i], rectangleCoords[0], x, y))
            break
        planeRectangle.append(solveLine(rectangleCoords[i], rectangleCoords[i + 1], x, y))
    if (planeRectangle[0] <= 0 and planeRectangle[1] <= 0 and planeRectangle[2] >= 0 and planeRectangle[3] >= 0):
        flag = False
        return flag
    else:
        flag = True
        return flag

def showPath():
    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(8.5, 6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    xTracepoint1 = []
    yTracepoint2 = []

    yTracepoint1 = []
    xTracepoint2 = []

    xTrackpoint1 = []
    yTrackpoint1 = []

    xTrackpoint2 = []
    yTrackpoint2 = []

    imageList = []

    axis = fig.add_subplot(111, aspect = 'equal', autoscale_on = False, xlim = (-MAX_X,MAX_X), ylim = (-MAX_Y, MAX_Y))
    #axis = plt.axes(xlim=(0, MAX_X), ylim=(0, MAX_Y))
    font = FontProperties()
    font.set_family('serif')
    font.set_name('Times New Roman')
    font.set_style('italic')
    axis.set_xlabel('x coordinate',  fontproperties = font)
    axis.set_ylabel('y coordinate', fontproperties = font)
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
    
    plt.show()
    
showPath()
print(circleOne(0, 0))
