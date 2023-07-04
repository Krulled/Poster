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


IGstarting = True
IGuploading = False
IGinputting = False
IGrestarting = False

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

while(true):
    while(IGstarting == True):
            Instagram = d(text= "Instagram")
            Creation = d(rresourceId = "com.instagram.android:id/creation_tab")
            Story =d(text = "STORY", resourceId = "com.instagram.android:id/cam_dest_story")
            galleryPreview =d(resourceId = "com.instagram.android:id/gallery_preview_button")
            check =d(text = "Add to story", resourceId = "com.instagram.android:id/gallery_title")
            
            if(Instagram.exists == True):
                Instagram.click()
                time.sleep(4)
                
            if(Creation.exists == True):
                Creation.click()
                time.sleep(4)
                
            if(Story.exists == True):
                Story.click()
                time.sleep(4)
                
            if(galleryPreview.exists == True):
                galleryPreview.click()
                time.sleep(4)
                
            if(check.exists == True):
                IGstarting = False
                IGuploading = True
        
    while(IGuploading == True):
            #uploading 
            galleryMenu = d(resourceId = "com.instagram.android:id/gallery_folder_menu")
            galleryPick = d(text = "IG stories", resourceId = "com.instagram.android:id/folder_picker_text_view")
            if(galleryMenu.exists == True):
                galleryMenu.click()
                time.sleep(4)
            if(galleryPick.exists == True):
                galleryPick.click()
                time.sleep(4)
            postparser.IGPickOut()
            
            