import cv2
import numpy

img=cv2.imread('images\landscape.png')


#drawing a circle on an image
#cv2.circle(image, center_coordinates, radius, color, thickness)

circle=cv2.circle(img,(420,270),100,(255,218,185),70) 
cv2.imshow('circle',circle)
cv2.waitKey(5000)



#drawing a rectangle on an image
#cv2.rectangle(image, start_point, end_point, color, thickness)

rect=cv2.rectangle(img,(100,100),(500,250),(255,0,0),-1)
cv2.imshow('rectangle',rect)
cv2.waitKey(5000)



#drawing a line on an image
#cv2.line(image, start_point, end_point, color, thickness)

line=cv2.line(img,(50,500),(800,50),(0,255,0),25)
cv2.imshow('line',line)
cv2.waitKey(5000)



#drawing an arrowed line on an image
#cv2.arrowedLine(image, start_point, end_point, color, thickness)

aline=cv2.arrowedLine(img,(600,200),(100,300),(255,255,0),10)
cv2.imshow('arrowed line',aline)
cv2.waitKey(5000)



#write text on image
#cv2.putText(image, text, org, font, fontScale, color, thickness)

text=cv2.putText(img,'Hello',(600,400),cv2.FONT_ITALIC,2,(0,0,0),5)
cv2.imshow('text',text)
cv2.waitKey(5000)



#cv2.fillpoly(Image,End_Points,Color)

points=numpy.array([[(420,350),(530,430),(500,500),(360,500),(310,430)]])

poly=cv2.fillPoly(img,pts=[points],color=(76,0,153))
cv2.imshow('pentagon',poly)
cv2.waitKey(5000)