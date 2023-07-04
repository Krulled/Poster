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
            Mercari = d(text= "Mercari")
            sell = d(resourceId = "components_bottomTabBar_sellTab", description = "Sell, tab, 3 of 5")
            listingCreate = d(text = "List an item")
            check = d(text = "Sell an item", resourceId = "components_navigation_headerTitle")
            
            
            if(folder.exists == True):
                folder.click()
                time.sleep(3)
                
            if(Mercari.exists == True):
                Mercari.click()
                time.sleep(3)
            
            if(sell.exists == True):
                sell.click()
                time.sleep(3)
            
            if(listingCreate.exists == True):
                listingCreate.click()
                time.sleep(3)
                
            if(check.exists == True):
                Mstarting = False
                Muploading = True
            
        while Muploading == True:
            
            check = d(resourceId = "components_navigation_headerTitle")
            uploadCamerea = d(resoureId = "listingScreen_uploadPhotoButton")
            library = d(resourceId = "cameraScreen_libraryButton")
            next1 = d(text = "Next")
            if(check.exists == True):
                #something with uploading
                if(uploadCamerea.exists == True):
                    uploadCamerea.click()
                    time.sleep(3)
                    if(library.exists == True):
                        library.click()
                        time.sleep(3)
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