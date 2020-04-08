import matplotlib.pyplot as plt
# from matplotlib.patches import Ellipse
# import matplotlib.animation as animation
# from matplotlib.animation import FuncAnimation
from matplotlib.font_manager import FontProperties

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

imageList = []

axis = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-MAX_X, MAX_X), ylim=(-MAX_Y, MAX_Y))
font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_style('italic')
axis.set_xlabel('x coordinate', fontproperties=font)
axis.set_ylabel('y coordinate', fontproperties=font)


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
    if (y >= -75 - clearance) and (y <= 75 + clearance) and (x >= -475 - clearance) and (x <= -375 + clearance):
        return False
    else:
        return True


def squareTwo(x, y, clearance):
    if (y >= -75 - clearance) and (y <= 75 + clearance) and (x >= 375 - clearance) and (x <= 475 + clearance):
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


def showPath():
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
