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


PMstarting = True
PMuploading = False
PMInputting = False
PMrestarting = False

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
        while PMstarting == True:
            print("starting")
            folder = d(text = "Poster")
            PoshMark = d(text= "Poshmark")
            sell = d(resourceId = "com.poshmark.app:id/sellTab", text = "Sell")
            listingCreate = d(resourceId = "com.poshmark.app:id/gallery")
            gallery = d(text = "Gallery")
            check = d(text = "Albums", resourceId = "com.sec.android.gallery3d:id/title")
            
            
            if(folder.exists == True):
                folder.click()
                time.sleep(3)
                
            if(PoshMark.exists == True):
                PoshMark.click()
                time.sleep(3)
            
            if(sell.exists == True):
                sell.click()
                time.sleep(3)
            
            if(listingCreate.exists == True):
                listingCreate.click()
                time.sleep(3)
                
            if(gallery.exists == True):
                gallery.click()
                time.sleep(3)
                
            if(check.exists == True):
                PMstarting = False
                PMuploading = True
            
        while PMuploading == True:
            
            check = d(text = "Albums", resourceId = "com.sec.android.gallery3d:id/title")
            next1 = d(text = "Done", resourceId = "com.sec.android.gallery3d:id/action_done")
            final = d(text = "NEXT", resourceId = "com.poshmark.app:id/nextButton")
            if(check.exists == True):
                check.click()
                #something with uploading
                postparser.PMgetphotos(index)
                    
                if(next1.exists == True):
                    next1.click()
                    time.sleep(5)
                    print("finished uploading")
                    if(final.exists == True):
                        final.click()
                        time.sleep(5)
                    if(final.exists == True):
                        final.click()
                        time.sleep(5)
                    if(final.exists == True):
                        final.click()
                        time.sleep(5)
                        PMuploading = False
                        PMInputting = True
            
            
        while PMInputting == True:
            titleDD = d(text = "What are you selling? (required)")
            descrip = d(text = "Tell shoppers about your listing (required)")
            done = d(text = "DONE")
            doneD = d(text = "Done")
            cat = d(text = "Category (required)")
            menSelect = d(text = "Men")
            womenSelect = d(text = "Women")
            shoes = d(text = "Shoes")
            sneakers = d(text = "Sneakers")
            
            
            #title
            if(titleDD.exists == True):
                titleDD.click()
                time.sleep(3)
                dr.shell(f'input text "{titleForPost}"')
                time.sleep(1)
                d.press.back()
                time.sleep(3)
                
            #desc
            if(descrip.exists == True):
                descrip.click()
                time.sleep(3)
                dr.shell(f'input text "{description}"')
                time.sleep(1)
                done.click()
                time.sleep(3)
                
            #category
            if(cat.exists == True):
                cat.click()
                time.sleep(3)
                if(menSelect.exists == True and c == "M"):
                    menSelect.click()
                    time.sleep(5)
                if(womenSelect.exists == True and c == "W"):
                    womenSelect.click()
                    time.sleep(5)
                if(shoes.exists == True):
                    shoes.click()
                    time.sleep(5)
                    if(c == "W"):
                        d.swipe(600,1100, 600, 300)
                        time.sleep(5)
                if(sneakers.exists == True):
                    sneakers.click()
                    time.sleep(5)
                if(doneD.exists == True):
                    doneD.click()
                    time.sleep(5)
                
                
            #Size
            
            sizeSelect = d(text = "Size (required)")
            sizeChoice = d(text = size)
            
            if(sizeSelect.exists == True):
                    sizeSelect.click()
                    time.sleep(3)
                    if(sizeChoice.exists == True):
                        sizeChoice.click()
                        time.sleep(5)
                    else:
                        d.swipe(600,1100, 600, 300)
                        if(sizeChoice.exists == True):
                            sizeChoice.click()
                            time.sleep(5)
                    
            
            #Brand
            
            branding = d(text = "Brand")
            brandChoice = d(text = brand, resourceId = "com.poshmark.app:id/suggestion")
            
            if(branding.exists == True):
                branding.click()
                time.sleep(5)
                dr.shell(f'input text "{brand}"')
                if(brandChoice.exists == True):
                    brandChoice.click()
                    time.sleep(5)
                    d.swipe(600,1100, 600, 300)
            
            
            #Original Price
            
            OGPricing = d(text = "Original Price (required)")
            if(OGPricing.exists == True):
                OGPricing.click()
                time.sleep(3)
                dr.shell(f'input text "{priceData}"')
                time.sleep(1)
                d.press.back()
                time.sleep(3)
            
            #Listing Price
            ListPricing = d(text = "Listing Price (required)")
            if(ListPricing.exists == True):
                ListPricing.click()
                time.sleep(3)
                dr.shell(f'input text "{priceData}"')
                time.sleep(1)
                d.press.back()
                time.sleep(3)
                
            
            #listing
            listing = d(text = "LIST")
            if(final.exists == True):
                final.click()
                time.sleep(5)
                if(listing.exists == True):
                    listing.click()
                    time.sleep(5)
                    PMInputting = False
                    PMrestarting = True                                  
            
            
        while PMrestarting == True:
            closing = d(text = "Close all")
            Youtube = d(text = "YouTube")
            d.press("recent")
            time.sleep(3)
            if(closing.exists == True):
                closing.click()
                time.sleep(10)
                PMrestarting = False
                Ebay = True