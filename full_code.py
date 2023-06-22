from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import array, matmul
from math import sin, cos, radians
from random import randint
import time
# --------------------------------------------------------------------------------------------------------------------------






def zoneFinder(x0,y0,x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    
    if (abs(dx) > abs(dy)): # This is zone: 0,3,4,7
        if(dx>=0 and dy>=0):
            return [0,x0,y0,x1,y1]
        elif (dx <= 0 and dy >= 0):
            return [3,-x0,y0,-x1,y1]
        elif (dx >= 0 and dy <= 0):
            return [7, x0,-y0,x1,-y1]
        elif (dx <= 0 and dy <= 0):
            return [4, -x0,-y0,-x1,-y1]
    else:
        if (dx>=0 and dy>=0):
            return [1, y0,x0,y1,x1]
        elif (dx <= 0 and dy >= 0):
            return [2, y0,-x0,y1,-x1]
        elif (dx <= 0 and dy <= 0):
            return [5, -y0,-x0,-y1,-x1]
        elif (dx >= 0 and dy <= 0):
            return [6, -y0,x0,-y1,x1]



def midPoint(X1,Y1,X2,Y2): # This is the midpoint algorithm
  allpointsArray = [] # An array to hold all of the digits from start to end
  dx = X2 - X1
  dy = Y2 - Y1

  d = 2*(dy)-dx
  dne = 2* (dy-dx)
  de = 2* dy
  x = X1
  y = Y1

  allpointsArray.append([x,y])

  while (x < X2):

    
    if(d < 0):
      x+=1
      d = d + de

    else:
      x = x + 1  
      y=y+1
      d = d + dne

    allpointsArray.append([x,y])
  return allpointsArray # This will give an array of converted zones, which we need to convert back to original zone


def zoneConverter(wholeArray, zone): # This is to convert back to the previous zone
    newArray = []

    for i in wholeArray:
        if zone == 0:
            newArray.append(i)
        elif zone == 1:
            newArray.append([i[1], i[0]])
        elif zone == 2:
            newArray.append([-i[1], i[0]])
        elif zone == 3:
            newArray.append([-i[0], i[1]])
        elif zone == 4:
            newArray.append([-i[0], -i[1]])
        elif zone == 5:
            newArray.append([-i[1], -i[0]])
        elif zone == 6:
            newArray.append([i[1], -i[0]])
        elif zone == 7:
            newArray.append([i[0], -i[1]])
        
    
    return newArray

def draw8WayCircle(x,y,a=0,b=0):
    array_8way = []
    array_8way.append([x+a, y+b])
    array_8way.append([y+a, x+b])
    array_8way.append([-x+a, y+b])
    array_8way.append([-y+a, x+b])
    array_8way.append([-x+a, -y+b])
    array_8way.append([-y+a, -x+b])
    array_8way.append([x+a, -y+b])
    array_8way.append([y+a, -x+b])

    return array_8way


def drawCircle(r, a=0,b=0):
    x = r
    y = 0
    d = 1 - r
    full_circle_array = []
    while (y <= x):
        if (d < 0):
            d=d+(2 * y+3)
            y=y+1
        else:
            d=d+(2 * y-2 * x+5)
            x=x-1
            y=y+1
        full_circle_array += draw8WayCircle(x, y,a,b)
    return full_circle_array

def fastDrawing(newlinedrawArray,r,g,b):
    glColor3f(r, g, b)
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    for i in newlinedrawArray: # [[x0,y0],[x1,y1],[x3,y3]]
        glVertex2f(i[0],i[1])
    glEnd()



def slowDrawing(newlinedrawArray,r,g,b, howSlow): # for animation
    glColor3f(r, g, b)
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    elapesed_ms = glutGet(GLUT_ELAPSED_TIME) #run time
    counter = 50
    for i in newlinedrawArray: # the program will wait and won't run until 50ms has passed
        if elapesed_ms > counter:
            glVertex2f(i[0],i[1])
            counter += howSlow 
            glutPostRedisplay() # for buffer refresh
    # penDraw(newlinedrawArray[0][0], newlinedrawArray[0][1])
    glEnd()






def testDraw(x0,y0,x1,y1, r=255,g=255, b=255): # testdraw = full midpoint line draw
    # glColor3f(r, g, b)
    # glPointSize(5) #pixel size. by default 1 thake
    # glBegin(GL_POINTS)
    newPoints = zoneFinder(x0,y0,x1,y1) 
    zone = newPoints[0] # [3,-x0,y0,-x1,y1]
    # print(newPoints)
    linedrawArray = midPoint(newPoints[1],newPoints[2],newPoints[3],newPoints[4]) # here at 0 index we have the zone, and index 1 to 4 we have x0,y0,x1,y1
    newlinedrawArray = zoneConverter(linedrawArray, zone) # we are passing the zone

    # elapesed_ms = glutGet(GLUT_ELAPSED_TIME)

    # counter = 50

    # for i in newlinedrawArray:
    #     if elapesed_ms > counter:
    #         glVertex2f(i[0],i[1])
    #         counter += 10
    #         glutPostRedisplay()

    # for i in newlinedrawArray:
        
    #     glVertex2f(i[0],i[1])

    #     glutPostRedisplay()

    return newlinedrawArray
 

    # glEnd()


# --------------------------------------------------------------------------------------------------------------------------
def iterate(): # Teacher gave it
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()



# ---------------- Animation Loop --------------------
# totalLoop = 0
# j = 10
# def loop(value):
#     global totalLoop, j
#     if totalLoop < 10:
#         penDraw(j)
#         totalLoop += 1
#         print(totalLoop)
#         glutTimerFunc(1000, loop, 0)
#         glutPostRedisplay()
#         totalLoop += 10
#         j += 10

    

# ---------------- Animation Loop Starts --------------------

# j = 10
# def penDraw():
#     global j
#     testDraw(110+j,400,120+j,600) # pen right side
#     testDraw(140+j,400,145+j,600) # pen left side
#     testDraw(120+j,600,145+j,600) # pen upper bar
#     j += 10

# def penDraw(x0, y0):
#     elapesed_ms = glutGet(GLUT_ELAPSED_TIME)
#     counterLast = 500
#     j = 0
#     for i in range(100):
#         if i == 0:
#             oneSideArray = testDraw(x0+i,y0,x0+i,y0*1.5) # pen right side
#             fastDrawing(oneSideArray, 255, 255, 255)
#             # testDraw(140+i,400,145+i,600) # pen left side
#             # testDraw(120+i,600,145+i,600) # pen upper bar
#             glutPostRedisplay()
#             counterLast += 10
#         else:
#             if elapesed_ms > counterLast:
#                 # For erasing
#                 oneSideArray = testDraw(x0+j,y0,x0+j,y0*1.5) # pen right side
#                 fastDrawing(oneSideArray, 0, 0, 0)
                
#                 # testDraw(140+j,400,145+j,600,0,0,0) # pen left side

#                 # testDraw(120+j,600,145+j,600,0,0,0) # pen upper bar
#                 glutPostRedisplay()

#                 # For drawing
#                 oneSideArray = testDraw(x0+i,y0,x0+i,y0*1.5) # pen right side
#                 fastDrawing(oneSideArray, 255, 255, 255)
#                 # testDraw(140+i,400,145+i,600) # pen left side
#                 # testDraw(120+i,600,145+i,600) # pen upper bar
#                 glutPostRedisplay()
#                 j+= 1
#                 counterLast += 10

def penDraw(penMoveArray, howFast):
    penMoveArray = penMoveArray
    x1 = penMoveArray[0][0]
    y1 = penMoveArray[0][1]
    elapesed_ms = glutGet(GLUT_ELAPSED_TIME)
    counterLast = 100 # 100ms so that the pen will start 50ms after the start of drawing line
    for k in range(len(penMoveArray)-1):
        x0 = penMoveArray[k][0]
        y0 = penMoveArray[k][1]
        
        if k == 0:
            oneSideArray = testDraw(x0,y0-10,x0,y0-100) # pen right side
            fastDrawing(oneSideArray, 255, 255, 255)

            glutPostRedisplay()
            # counterLast += howFast


        if k > 0:
            if elapesed_ms > counterLast:
                # For erasing

                oneSideArray = testDraw(x1,y1-10,x1,y1-100) # pen right side
                fastDrawing(oneSideArray, 0, 0, 0)
                
                glutPostRedisplay()

                # For drawing
                oneSideArray = testDraw(x0,y0-10,x0,y0-100) # pen right side
                fastDrawing(oneSideArray, 255, 255, 255)
                counterLast += howFast
                glutPostRedisplay()
                

        x1 = x0
        y1 = y0
    oneSideArray = testDraw(x1,y1-10,x1,y1-100) # for erasing the last pen
    fastDrawing(oneSideArray, 0, 0, 0)

# ---------------- Animation Loop Ends --------------------

# ---------------- Paper Print Start --------------------
def paperPrint(xb, yb, xt, yt,paperStretch):
    # Drawing the page
    rightSidePageArray = testDraw(xt,yt,xb,yb) # right side
    

    leftSidePageArray = testDraw(paperStretch*xt,yt,paperStretch*xb,yb) # left side

     
    topSidePageArray = testDraw(xt,yt,paperStretch*xt,yt) # top side


    bottomSideDrawArray = testDraw(xb,yb,paperStretch*xb,yb) # bottom side


    totalPaperDrawArray = rightSidePageArray + leftSidePageArray + topSidePageArray + bottomSideDrawArray # The array will consist all the paper
    fastDrawing(totalPaperDrawArray, 255, 255, 255) # this will draw all the papers using the array above in rgb: (255,255,255) or in white


# ================ Paper Print Ends =====================


# ------------------   Alphabets Starts -------------------------

def DrawAlphabet_A(x_axis, y_axis):
    backA = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topA = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    toprightA = testDraw(x_axis+50, y_axis-75, x_axis+50, y_axis-25)
    midA = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-50)

    total_A = backA + topA + midA + toprightA
    return total_A

def DrawAlphabet_B(x_axis, y_axis):
    backB = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topB = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-40)
    midtopB = testDraw(x_axis+50, y_axis-40,x_axis+25, y_axis-50)
    midbotB = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-60)
    botB = testDraw(x_axis+50, y_axis-60,x_axis+25, y_axis-75)

    total_B = backB + topB + midtopB + midbotB + botB
    return total_B

def DrawAlphabet_C(x_axis, y_axis):
    backC = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topC = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    botC = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)


    total_C = backC + topC + botC
    return total_C

def DrawAlphabet_D(x_axis, y_axis):
    backD = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topD = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-50)
    botD = testDraw(x_axis+50, y_axis-50,x_axis+25, y_axis-75)
    

    total_D = backD + topD + botD
    return total_D

def DrawAlphabet_E(x_axis, y_axis):
    backE = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topE = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    midE = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-50)
    botE = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)

    total_E = backE + topE + midE + botE
    return total_E

def DrawAlphabet_F(x_axis, y_axis):
    backF = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topF = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    midF = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-50)

    total_F = backF + topF + midF
    return total_F

def DrawAlphabet_G(x_axis, y_axis):
    backG = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topG = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    botG = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    midupG = testDraw(x_axis+50, y_axis-75,x_axis+50, y_axis-50)
    midhalfG = testDraw(x_axis+50, y_axis-50,x_axis+40, y_axis-50)


    total_G = backG + topG + botG + midupG + midhalfG
    return total_G

def DrawAlphabet_H(x_axis, y_axis):
    backH = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    frontH = testDraw(x_axis+50, y_axis-25,x_axis+50, y_axis-75)
    midH = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-50)


    total_H = backH + frontH + midH
    return total_H

def DrawAlphabet_I(x_axis, y_axis):
    topI = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    midI = testDraw(x_axis+38, y_axis-25,x_axis+38, y_axis-75)
    botI = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    

    total_I = topI + midI + botI
    return total_I

def DrawAlphabet_J(x_axis, y_axis):
    topJ = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    frontJ = testDraw(x_axis+50, y_axis-25,x_axis+50, y_axis-75)
    botJ = testDraw(x_axis+50, y_axis-75, x_axis+25, y_axis-75)
    leftupJ = testDraw(x_axis+25, y_axis-75,x_axis+25, y_axis-50)

    total_J = topJ + frontJ + botJ + leftupJ
    return total_J

def DrawAlphabet_K(x_axis, y_axis):
    backK = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    midtopK = testDraw(x_axis+50, y_axis-25,x_axis+25, y_axis-50)
    midbotK = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-75)

    total_K = backK + midtopK + midbotK
    return total_K

def DrawAlphabet_L(x_axis, y_axis):
    backL = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    botL = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)

    total_L = backL + botL
    return total_L

def DrawAlphabet_M(x_axis, y_axis):
    backM = testDraw(x_axis+25, y_axis-75, x_axis+25, y_axis-25)
    frontM = testDraw(x_axis+50, y_axis-25,x_axis+50, y_axis-75)
    midlefttM = testDraw(x_axis+25, y_axis-25,x_axis+38, y_axis-50)
    midrightM = testDraw(x_axis+38, y_axis-50,x_axis+50, y_axis-25)

    total_M = backM +  midlefttM + midrightM + frontM
    return total_M

def DrawAlphabet_N(x_axis, y_axis):
    backN = testDraw(x_axis+25, y_axis-75, x_axis+25, y_axis-25)
    midN = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-75)
    frontN = testDraw(x_axis+50, y_axis-75, x_axis+50, y_axis-25)
    
    total_N = backN +  midN  + frontN
    return total_N

def DrawAlphabet_O(x_axis, y_axis):
    backO = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topO = testDraw(x_axis+50, y_axis-25, x_axis+25, y_axis-25)
    botO = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    frontO = testDraw(x_axis+50, y_axis-75, x_axis+50, y_axis-25)


    total_O = topO + backO +  botO + frontO
    return total_O

def DrawAlphabet_P(x_axis, y_axis):
    backP = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topP = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    toprightP = testDraw(x_axis+50, y_axis-25, x_axis+50, y_axis-50)
    midP = testDraw(x_axis+50, y_axis-50, x_axis+25, y_axis-50,)

    total_P = backP + topP + toprightP + midP 
    return total_P

def DrawAlphabet_Q(x_axis, y_axis):
    backQ = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topQ = testDraw(x_axis+50, y_axis-25, x_axis+25, y_axis-25)
    botQ = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    frontQ = testDraw(x_axis+50, y_axis-75, x_axis+50, y_axis-25)
    small_lineQ = testDraw(x_axis+45, y_axis-70, x_axis+55, y_axis-80)


    total_Q = topQ + backQ +  botQ + frontQ + small_lineQ
    return total_Q

def DrawAlphabet_R(x_axis, y_axis):
    backR = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    topR = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-40)
    midtopR = testDraw(x_axis+50, y_axis-40,x_axis+25, y_axis-50)
    midbotR = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-75)

    total_R = backR + topR + midtopR + midbotR
    return total_R

def DrawAlphabet_S(x_axis, y_axis):
    backS = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-50)
    topS = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    midS = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-50)
    botS = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    rightmidS = testDraw(x_axis+50, y_axis-75,x_axis+50, y_axis-50)

    total_S = backS + topS + midS + botS + rightmidS
    return total_S

def DrawAlphabet_T(x_axis, y_axis):
    topT = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    midT = testDraw(x_axis+38, y_axis-25,x_axis+38, y_axis-75)

    total_T = topT + midT
    return total_T

def DrawAlphabet_U(x_axis, y_axis):
    backU = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    botU = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    frontU = testDraw(x_axis+50, y_axis-75, x_axis+50, y_axis-25)


    total_U = backU +  botU + frontU
    return total_U

def DrawAlphabet_V(x_axis, y_axis):
    leftV = testDraw(x_axis+25, y_axis-25,x_axis+38, y_axis-75)
    rightV = testDraw(x_axis+38, y_axis-75,x_axis+50, y_axis-25)

    total_V = leftV + rightV
    return total_V

def DrawAlphabet_W(x_axis, y_axis):
    backW = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-75)
    botW = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    frontW = testDraw(x_axis+50, y_axis-75, x_axis+50, y_axis-25)
    middleW = testDraw(x_axis+38, y_axis-75,x_axis+38, y_axis-50)


    total_W = backW + frontW + botW + middleW
    return total_W

def DrawAlphabet_X(x_axis, y_axis):
    midX1 = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-75)
    midX2 = testDraw(x_axis+50, y_axis-25,x_axis+25, y_axis-75)

    total_X = midX1 + midX2
    return total_X

def DrawAlphabet_Y(x_axis, y_axis):
    midY1 = testDraw(x_axis+25, y_axis-25,x_axis+25, y_axis-50)
    midY2 = testDraw(x_axis+50, y_axis-25,x_axis+50, y_axis-50)
    midY = testDraw(x_axis+25, y_axis-50,x_axis+50, y_axis-50)
    botY = testDraw(x_axis+38, y_axis-75,x_axis+38, y_axis-50)

    total_Y = midY1 + midY2 + botY + midY
    return total_Y

def DrawAlphabet_Z(x_axis, y_axis):
    topZ = testDraw(x_axis+25, y_axis-25,x_axis+50, y_axis-25)
    midZ = testDraw(x_axis+50, y_axis-25,x_axis+25, y_axis-75)
    botZ = testDraw(x_axis+25, y_axis-75,x_axis+50, y_axis-75)
    

    total_Z = topZ + midZ + botZ
    return total_Z




# ==================   Alphabets Ends ==========================

# ------------------   Frame Draw Starts -------------------------

random_emoji_eye_picker = 0
random_emoji_mouth_picker = 0

def frameDraw(frame_radius, frame_x_axis, frame_y_axis, stickEye, r=245,g=222,b=179):
    intialCircleFrame = drawCircle(frame_radius, frame_x_axis,frame_y_axis)
    # Head draw
    headUpper = testDraw(frame_x_axis-60, frame_y_axis+50, frame_x_axis+60, frame_y_axis+50)
    headLower = testDraw(frame_x_axis-60, frame_y_axis-50, frame_x_axis+60, frame_y_axis-50)
    headRight = testDraw(frame_x_axis+60, frame_y_axis+50, frame_x_axis+60, frame_y_axis-50)
    headLeft = testDraw(frame_x_axis-60, frame_y_axis+50, frame_x_axis-60, frame_y_axis-50)
    headDraw = headUpper + headLower + headRight + headLeft
    fastDrawing(headDraw, r,g,b)

    # body frame draw
    middlebodyDraw = testDraw(frame_x_axis, frame_y_axis-100, frame_x_axis, frame_y_axis-50)
    rightHandDraw = testDraw(frame_x_axis, frame_y_axis-50, frame_x_axis+40, frame_y_axis-80)
    LeftHandDraw = testDraw(frame_x_axis, frame_y_axis-50, frame_x_axis-40, frame_y_axis-80)

    fullBodyDraw = middlebodyDraw + rightHandDraw + LeftHandDraw
    fastDrawing(fullBodyDraw, r,g,b)

    #Emoji Draw
    figuireEyes = [
        [[frame_x_axis-15, frame_y_axis+15, frame_x_axis-40, frame_y_axis+15],[frame_x_axis+15, frame_y_axis+15, frame_x_axis+40, frame_y_axis+15]],
            [[frame_x_axis-25, frame_y_axis+20, frame_x_axis-25, frame_y_axis],[frame_x_axis+25, frame_y_axis+20, frame_x_axis+25, frame_y_axis]]]
    RighteyeDraw = testDraw(figuireEyes[stickEye][0][0], figuireEyes[stickEye][0][1], figuireEyes[stickEye][0][2], figuireEyes[stickEye][0][3]) #eyepicker, righteye/lefteye,
    LefteyeDraw = testDraw(figuireEyes[stickEye][1][0], figuireEyes[stickEye][1][1], figuireEyes[stickEye][1][2], figuireEyes[stickEye][1][3])
    # RighteyeDraw = testDraw(frame_x_axis-25, frame_y_axis+20, frame_x_axis-25, frame_y_axis) #eyepicker, righteye/lefteye,
    #LefteyeDraw = testDraw(frame_x_axis+25, frame_y_axis+20, frame_x_axis+25, frame_y_axis)

    twoEyes = RighteyeDraw + LefteyeDraw
    fastDrawing(twoEyes, r,g,b)

    mouthDraw = testDraw(frame_x_axis-25, frame_y_axis-20, frame_x_axis+25, frame_y_axis-20)

    fastDrawing(mouthDraw, r,g,b)
    fastDrawing(intialCircleFrame, 128,0,0)


# ==================   Frame Draw Ends  ==========================


# ------------------   Alphabets Drawer -------------------------

def DrawAlphabets(wholeString, x_spaces, y_spaces, howSlow, italic=False):
    global boundary_x_alphabet, boundary_y_alphabet


    wholeString_temp = wholeString[0:97]
    

    x_spaces_temp = x_spaces
    y_spaces_temp = y_spaces

    italic_space = 40

    all_alphabet_draw_array = []

    lastCounter = 0

    totalCharacterinoneLine = 14
    if wholeString == '': # If the user inputs empty string
        return 0
    indexing = 0
    while indexing < (len(wholeString_temp)):
        lastCounter += 1
        i = wholeString[indexing]
        if x_spaces_temp >= boundary_x_alphabet - 75:
            lastCounter = 0
            y_spaces_temp -= 100
            x_spaces_temp = x_spaces
            if italic == True:
                x_spaces_temp += italic_space
                italic_space += 25
            if y_spaces_temp < boundary_y_alphabet + 75:
                break
        if i == ' ':
            x_spaces_temp += 15 #A/B
            indexing += 1
        elif i == '/':
            y_spaces_temp -= 100
            x_spaces_temp = x_spaces + 25
        elif i == 'A':
            alphabet_A_array = DrawAlphabet_A(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_A_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'B':
            alphabet_B_array = DrawAlphabet_B(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_B_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'C':
            alphabet_C_array = DrawAlphabet_C(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_C_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'D':
            alphabet_D_array = DrawAlphabet_D(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_D_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'E':
            alphabet_E_array = DrawAlphabet_E(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_E_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'F':
            alphabet_F_array = DrawAlphabet_F(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_F_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'G':
            alphabet_G_array = DrawAlphabet_G(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_G_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'H':
            alphabet_H_array = DrawAlphabet_H(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_H_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'I':
            alphabet_I_array = DrawAlphabet_I(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_I_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'J':
            alphabet_J_array = DrawAlphabet_J(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_J_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'K':
            alphabet_K_array = DrawAlphabet_K(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_K_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'L':
            alphabet_L_array = DrawAlphabet_L(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_L_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'M':
            alphabet_M_array = DrawAlphabet_M(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_M_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'N':
            alphabet_N_array = DrawAlphabet_N(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_N_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'O':
            alphabet_O_array = DrawAlphabet_O(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_O_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'P':
            alphabet_P_array = DrawAlphabet_P(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_P_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'Q':
            alphabet_Q_array = DrawAlphabet_Q(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_Q_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'R':
            alphabet_R_array = DrawAlphabet_R(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_R_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'S':
            alphabet_S_array = DrawAlphabet_S(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_S_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'T':
            alphabet_T_array = DrawAlphabet_T(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_T_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'U':
            alphabet_U_array = DrawAlphabet_U(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_U_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'V':
            alphabet_V_array = DrawAlphabet_V(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_V_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'W':
            alphabet_W_array = DrawAlphabet_W(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_W_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'X':
            alphabet_X_array = DrawAlphabet_X(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_X_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'Y':
            alphabet_Y_array = DrawAlphabet_Y(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_Y_array
            x_spaces_temp += 40
            indexing += 1
        elif i == 'Z':
            alphabet_Z_array = DrawAlphabet_Z(x_spaces_temp,y_spaces_temp)
            all_alphabet_draw_array = all_alphabet_draw_array+ alphabet_Z_array
            x_spaces_temp += 40
            indexing += 1
        else:
            indexing += 1
            continue
    if italic == True:
        all_alphabet_draw_array = shearingObject(all_alphabet_draw_array, 0.3)
    penDraw(all_alphabet_draw_array, howSlow)
    slowDrawing(all_alphabet_draw_array, 255, 255, 255, howSlow)

# --------------------   Transformations Starts -----------------

preserved_x = 0
preserved_y = 0

def x_axis_shearing_fix(to_translate_array): # to_translate_array has the sheered array

    global preserved_x # preserver_x = 300

    to_convert_x = preserved_x + 50 - to_translate_array[0][0]


    to_translate_array_temp = []
    for i in range(len(to_translate_array)):

        x_axis = to_translate_array[i][0] + to_convert_x
        y_axis = to_translate_array[i][1]
        to_translate_array_temp.append([x_axis, y_axis])

    return to_translate_array_temp
    

def shearingObject(objects_to_shear,x_axis):
    initial_shear_array = array([[1, 0, 0],
                                [x_axis, 1, 0],
                                [0, 0, 1]]) 

    shear_object_array = objects_to_shear

    for i in range(len(shear_object_array)):
        shear_object_array[i].append(1)
    shear_final_array = []
    for j in shear_object_array:
        trash_variable= matmul(j, initial_shear_array)
        shear_final_array.append([(trash_variable[0]),(trash_variable[1])])
    
    translated_shear_array = x_axis_shearing_fix(shear_final_array) # to fix 
    # slowDrawing(translated_shear_array, 255, 255, 255, 50)
    return translated_shear_array


# def scalingObject(objectToScale,howMuchScale):
#     initial_scale_array = array([[howMuchScale, 0, 0],[0, howMuchScale, 0],[0, 0, 1]])

#     scale_object_array = objectToScale

#     for i in range(len(scale_object_array)):
#         scale_object_array[i].append(1)
#     scale_final_array = []
#     for j in scale_object_array:
#         trash_variable= matmul(j, initial_scale_array)
#         scale_final_array.append([(trash_variable[0]),(trash_variable[1])])
    
#     translated_scale_array = scale_final_array
#     # slowDrawing(translated_scale_array, 255, 255, 255, 50)
#     return translated_scale_array


# def rotateObject(rotationByDegree):
#     cos_rotate_value = cos(radians(rotationByDegree))
#     sin_rotate_value = sin(radians(rotationByDegree))
#     initial_rotate_array = array([[cos_rotate_value, -sin_rotate_value, 0],[sin_rotate_value, cos_rotate_value, 0],[0, 0, 1]])
#     m_180 = DrawAlphabet_M(300, 800)
#     m_180_temp = []
#     for i in range(len(m_180)):
#         m_180[i].append(1)
    
#     for j in m_180:
#         trash_variable= matmul(j, initial_rotate_array)
#         m_180_temp.append([(trash_variable[0]),(trash_variable[1])])
    

#     slowDrawing(m_180_temp, 255, 255, 255, 50)



# =================   Transformations Ends ======================

# ==================   Alphabets Drawer =========================

globalswitch = False
boundary_x_alphabet = 0
boundary_y_alphabet = 0
eyeTimeCounter = 1000

def showScreen():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    global globalswitch
    global boundary_x_alphabet, boundary_y_alphabet
    global preserved_x, preserved_y
    global userAlphabet, instant_fast_slow_input, userItalic
    global random_emoji_eye_picker, eyeTimeCounter
    
    frameDraw(100, 120, 850, 0) # (radius, x axis, y axis)

    elapsedCounter = glutGet(GLUT_ELAPSED_TIME)
    if elapsedCounter > eyeTimeCounter:
        eyeTimeCounter += 1000
        if random_emoji_eye_picker == 0:
            # This is for erasing the previous eyes
            frameDraw(100, 120, 850, 1,0,0,0)
            frameDraw(100, 120, 850, 0,0,0,0)
            frameDraw(100, 120, 850, 0)
            random_emoji_eye_picker = 1 
        elif random_emoji_eye_picker == 1:
            # This is for erasing the previous eyes
            frameDraw(100, 120, 850, 1,0,0,0)
            frameDraw(100, 120, 850, 0,0,0,0)
            frameDraw(100, 120, 850, 1)
            random_emoji_eye_picker = 0

    # Drawing the Paper
    x_bottom_paper = 300
    y_bottom_paper = 100
    x_top_paper = 300 # make x_bottom_paper and y_top_paper same so the paper will be straight
    y_top_paper = 800

    preserved_x = x_bottom_paper
    preserved_y = x_top_paper

    paperStretch = 3 # how stretch the paper will be on x axis

    boundary_x_alphabet = x_bottom_paper * paperStretch
    boundary_y_alphabet = 100

    paperPrint(x_bottom_paper,y_bottom_paper,x_top_paper,y_top_paper, paperStretch)



    # Drawing the pen
    
    # alphabet_A_array = DrawAlphabet_A(x_top_paper,y_top_paper)
    # penDraw(alphabet_A_array, 50)
    # slowDrawing(alphabet_A_array, 255, 255, 255, 50)

    


    


    DrawAlphabets(userAlphabet, x_top_paper, y_top_paper, instant_fast_slow_input, userItalic)
    

    paperPrint(x_bottom_paper,y_bottom_paper,x_top_paper,y_top_paper, paperStretch)
    x_axis_circle = 170
    y_axis_circle = 850
    x = (100, x_axis_circle, y_axis_circle)

    #rotateObject(50)
    # shearingObject(1,0.3)

    # if globalswitch == False:
    #     print(globalswitch)
    #     globalswitch = True
    # if globalswitch == True:
    #     print(globalswitch)
    #     globalswitch = False

    glutSwapBuffers()


userAlphabet = (str(input('Enter your string: '))).upper() # To take input from the user
instant_fast_slow_input = 0
userItalic = False


userItalicQuestion = (str(input('Do you want italic? Yes or no? '))).upper()
if userItalicQuestion == 'YES':
    userItalic = True

_ = (str(input('How fast do you want? Instant, fast, slow: '))).lower()
if _ == 'instant':
        instant_fast_slow_input = 0
elif _ == 'fast':
    instant_fast_slow_input = 20
elif _ == 'slow':
    instant_fast_slow_input = 50

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutMainLoop()
