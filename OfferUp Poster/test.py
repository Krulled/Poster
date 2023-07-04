## functions
import postparser
import time
import datetime
import random

## necessary imports
from uiautomator import Device
d = Device('R58R746PGVD')
from ppadb.client import Client
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
dr = devices[0]


Mstarting = True
Muploading = False
MInputting = False
Mrestarting = False

index = postparser.getPost()
a = postparser.parsePic()
titleForPost = a[0]
priceData = a[1]
description = a[2]
conditionS = a[3]
brand = a[4]
color = a[5]
size = a[6]
c = a[7]
       
while(True): 
        while Mstarting == True:
            print("starting")
            folder = d(text = "Poster")
            FB = d(text= "Facebook")
            MP = d(description = "Marketplace, tab 4 of 6")
            sell = d(text = "Sell")
            listingCreate = d(text = "Create Listing")
            items = d(text= "Items", className = "android.widget.Button")
            addPhoto = d(text = "Add photos / video")
            check = d(resourceId = "marketplace_camera_roll_android_back_button")
            
            
        while Muploading == True:
            
            check = d(resourceId = "marketplace_camera_roll_android_back_button")
            next1 = d(text = "Next")
            if(check.exists == True):
                #something with uploading
                postparser.FBgetPhotos(index)
                if(next1.exists == True):
                    next1.click()
                    time.sleep(5)
                    print("finished uploading")
                    Muploading = False
                    MInputting = True
            
            
        while MInputting == True:
            print("inputting")
                        
                                    
            
            
        while Mrestarting == True:
            closing = d(text = "Close all")
            Youtube = d(text = "YouTube")
            d.press("recent")
            time.sleep(3)
            if(closing.exists == True):
                closing.click()
                time.sleep(10)
                Mrestarting = False
                Ebay = True