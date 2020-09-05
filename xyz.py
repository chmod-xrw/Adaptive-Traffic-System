#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:40:31 2019

@author: kunj
"""

#
#import tkinter as tk
from tkinter import *
#root = tk.Tk()
#
#canvas=Canvas(width=300,height=300)
#canvas.pack()
#l=Label(canvas,text='xyz')
#l.pack()
#l.config(text='asdfadf')
#canvas.create_window(100,100,window=l)
#mainloop()
#




import time
import cv2
from PIL import Image   
from imageai.Detection import ObjectDetection
import os
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')






execution_path=os.getcwd()
detector=ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path,"yolo.h5"))
detector.loadModel()

#total_frames = cap.get(7)
import tkinter as tk 
root = tk.Tk()
screen_width = root.winfo_screenwidth();
screen_height = root.winfo_screenheight();
canvas = tk.Canvas(root, width=screen_width, height=screen_height, borderwidth=0, highlightthickness=0 ,bg="white")
canvas.pack()

x,y=screen_width,screen_height
mid_x = int(screen_height/2);
mid_y = int(screen_width/2);
offset_y=100
offset_x=50
r = 40

''' graphical user interface'''

# labels
l1 = Label(canvas,text='0')
l2 = Label(canvas,text='0')
l3 = Label(canvas,text='0')
l4 = Label(canvas,text='0')

l1.pack()
l2.pack()
l3.pack()
l4.pack()


canvas.create_line(screen_width/2,0,screen_width/2,screen_height)
canvas.create_line(0,screen_height/2,screen_width,screen_height/2)
list_red = []
list_yellow=[]
list_green=[]



canvas.create_window(mid_x-200,200,window=l1)
canvas.create_window(screen_width-200,200,window=l2)
canvas.create_window(mid_y-30,mid_x+30,window=l3)
canvas.create_window(screen_width-30,mid_x+30,window=l4)


# 1st
list_red.append(canvas.create_oval(100-r , 100-r , 100+r , 100+r , fill="gray83", outline="#000", width=4))
list_yellow.append(canvas.create_oval(100-r , 200-r , 100+r , 200+r , fill="gray83", outline="#000", width=4))                  
list_green.append(canvas.create_oval(100-r , 300-r , 100+r , 300+r , fill="gray83", outline="#000", width=4))                   
# 2nd
list_red.append(canvas.create_oval(mid_y-r+offset_y , 100-r , mid_y+r+offset_y,100+r , fill="gray83", outline="#000", width=4))
list_yellow.append(canvas.create_oval(mid_y-r+offset_y , 200-r , mid_y+r+offset_y,200+r , fill="gray83", outline="#000", width=4))                   
list_green.append(canvas.create_oval(mid_y-r+offset_y , 300-r , mid_y+r+offset_y,300+r , fill="gray83", outline="#000", width=4))
#3rd                   
list_red.append(canvas.create_oval(100-r, mid_x+100-r-offset_x , 100+r , mid_x+100+r-offset_x , fill="gray83", outline="#000", width=4))
list_yellow.append(canvas.create_oval(100-r, mid_x+200-r-offset_x , 100+r , mid_x+200+r-offset_x , fill="gray83", outline="#000", width=4))                   
list_green.append(canvas.create_oval(100-r, mid_x+300-r-offset_x , 100+r , mid_x+300+r-offset_x , fill="gray83", outline="#000", width=4))                   
#4th                   
list_red.append(canvas.create_oval(mid_y-r+offset_y , mid_x+100-r-offset_x , mid_y+r+offset_y , mid_x+100+r-offset_x, fill="gray83", outline="#000", width=4))
list_yellow.append(canvas.create_oval(mid_y-r+offset_y , mid_x+200-r-offset_x , mid_y+r+offset_y , mid_x+200+r-offset_x, fill="gray83", outline="#000", width=4))
list_green.append(canvas.create_oval(mid_y-r+offset_y , mid_x+300-r-offset_x , mid_y+r+offset_y , mid_x+300+r-offset_x , fill="gray83", outline="#000", width=4))
    

def reCount(file_name):
	
	# Prabhu "path" pradashit karo 
	
    image_obj =Image.open(r"D:/detection/" + file_name)
    width,height = image_obj.size
    cropped_image_V_1 = image_obj.crop((0, 0, width/2, height))
    cropped_image_V_2 = image_obj.crop((width/2, 0, width, height))
    cropped_image_V_1.save('cropped3.jpg')
    cropped_image_V_2.save('cropped4.jpg')	
    detectionsv1=detector.detectObjectsFromImage(os.path.join(execution_path,"cropped3.jpg"),execution_path+"/"+"h1.jpg")
    detectionsv2=detector.detectObjectsFromImage(os.path.join(execution_path,"cropped4.jpg"),execution_path+"/"+"h2.jpg")
    return(len(detectionsv1)+len(detectionsv2))

cap0 = cv2.VideoCapture(r"D:\detection\all\0.mp4")
cap1 = cv2.VideoCapture(r"D:\detection\all\1.mp4")
cap2 = cv2.VideoCapture(r"D:\detection\all\2.mp4")
cap3 = cv2.VideoCapture(r"D:\detection\all\3.mp4")


past=0
canvas.itemconfig(list_green[0],fill="green")
canvas.itemconfig(list_red[1],fill="red")
canvas.itemconfig(list_red[2],fill="red")
canvas.itemconfig(list_red[3],fill="red")
root.update()


a=[0]*4
val=[0]*4
side=0
time.sleep(5)
x=100
while(x<2000):    
    side=(side+1)%4
    if(max(a)>2):
        side=a.index(max(a))
        #print("Green after long time : ",side)
        a[side]=0
        canvas.itemconfig(list_red[side],fill="gray83")
        canvas.itemconfig(list_yellow[side],fill="yellow")
        canvas.itemconfig(list_green[past],fill="gray83")
        canvas.itemconfig(list_red[past],fill="red")
        root.update()
        time.sleep(5)
        canvas.itemconfig(list_yellow[side],fill="gray83")
        canvas.itemconfig(list_green[side],fill="green")  
        root.update()
        time.sleep(5)
        past=side
        continue
    
    #count no of vehical from image
    cap0.set(1, x)
    ret, frame = cap0.read()
    cv2.imwrite("frane.jpg", frame)
    cap1.set(1, x)
    ret, frame = cap1.read()
    cv2.imwrite("frane1.jpg", frame)
    cap2.set(1, x)
    ret, frame = cap2.read()
    cv2.imwrite("frane2.jpg", frame)
    cap3.set(1, x)
    ret, frame = cap3.read()
    cv2.imwrite("frane3.jpg", frame)

    val[0]=reCount("frane.jpg")
    val[1]=reCount("frane1.jpg")
    val[2]=reCount("frane2.jpg")
    val[3]=reCount("frane3.jpg")
    #print(val)
    
''' are you lost baby girl? '''
    
    l1.config(text=str(val[0]))
    engine.say("there are currently" +str(val[0])+ "vehicles in lane 1")
    engine.runAndWait()
    a1=open(r'D:\detection\vehicles_info\lane1.txt',"a")
    a1.write(str(val[0]))
    a1.write("\n")
    a1.close()
    l2.config(text=str(val[1]))
    engine.say("there are currently" +str(val[1])+ "vehicles in lane 2")
    engine.runAndWait()
    a2=open(r'D:\detection\vehicles_info\lane2.txt',"a")
    a2.write(str(val[1]))
    a2.write("\n")
    a2.close()
    l3.config(text=str(val[2]))
    engine.say("there are currently" +str(val[2])+ "vehicles in lane 3")
    engine.runAndWait()
    a3=open(r'D:\detection\vehicles_info\lane3.txt',"a")
    a3.write(str(val[2]))
    a3.write("\n")
    a3.close()
    l4.config(text=str(val[3]))
    engine.say("there are currently" +str(val[3])+ "vehicles in lane 4")
    engine.runAndWait()
    a4=open(r'D:\detection\vehicles_info\lane4.txt',"a")
    a4.write(str(val[3]))
    a4.write("\n")
    a4.close()
    newside=val.index(max(val))
    #print("Green after long time : ",newside)
    a[newside]=0
    newside=newside+4
    index =newside%4
    if(past!=index):
        canvas.itemconfig(list_red[index],fill="gray83")
        canvas.itemconfig(list_yellow[index],fill="yellow")
        canvas.itemconfig(list_green[past],fill="gray83")
        canvas.itemconfig(list_red[past],fill="red")
        root.update()
        time.sleep(5)
        canvas.itemconfig(list_yellow[index],fill="gray83")
        canvas.itemconfig(list_green[index],fill="green")
        root.update()
        f=index
        f=f+1
        engine.say("lane ready to go is" +str(f))
        engine.runAndWait()
    else:
        root.update()
        e=index
        e=e+1
        engine.say("lane ready to go is" +str(e))
        engine.runAndWait()
        time.sleep(5)  
        
    past=index
    for i in range(side,newside+1):
        if((i%4)!=(newside%4)):
            a[i%4]=a[i%4]+1
    side=newside%4
    past=(side)%4
    x=x+100
canvas.destroy()
for file in os.listdir(execution_path):
    if file.endswith('.jpg'):
        os.remove(file)
				
'''what are you waiting forrr....run me like you do ra ra run me like you do'''
