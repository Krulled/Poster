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


AStarting = True
AUploading = False
AInputting = False
Arestarting = False

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
alias = a[8]
SKU = a[9]
       
while(True): 
        while AStarting == True:
            #check if the variable for alias is true
            print("starting")
            folder = d(text = "Poster")
            A = d(text= "alias")
            Search = d(resourceId = "org.alias:id/navSearch")
            serarchTab = d(text = "Brand, Name, SKU", resourceId = "org.alias:id/searchBarEditText")
            searchResult = d(text = SKU, resourceId = "org.alias:id/searchResultSku")
            sell = d(text = "SELL", package = "org.alias")
            startlisting = d(text = "Start Listing", resourceId = "org.alias:id/pdpStartListingButton")
            sizing = d(text = size, resourceId = "org.alias:id/selectableGridItemText")
            selectIC = d(text = "SELECT ITEM CONDITION")
            new = d(text = "NEW", package = "org.alias")
            used = d(text = "USED", package = "org.alias")
            nextL = d(text = "Next", resourceId = "org.alias:id/")
            packagingC = d(text = "SELECT PACKAGING CONDITION", resourceId = "org.alias:id/headerTitle")
            price = d(resourceId = "org.alias:id/priceSelectorPriceTextView")
            
            
            if(folder.exists == True):
                folder.click()
                time.sleep(5)
            
            if(A.exists == True):
                A.click()
                time.sleep(5)
                
            if(serarchTab.exists == True):
                serarchTab.click()
                time.sleep(5)
                
                        
            if(serarchTab.exists == True):
                serarchTab.click()
                dr.shell(f'input text "{SKU}"')
                time.sleep(5)
                
            if(searchResult.exists == True):
                searchResult.click()
                time.sleep(5)
            
            if(sell.exists == True):
                sell.click()
                time.sleep(5)
            
            if(startlisting.exists == True):
                startlisting.click()
                time.sleep(5)
                
            if(sizing.exists == True):
                sizing.click()
                time.sleep(5)
            
            if(selectIC.exists == True):
                selectIC.click()
                time.sleep(5)
                if(conditionS == "N"):
                    new.click()
                    time.sleep(5)
                if(conditionS == "U"):
                    used.click()
                    time.sleep(5)
                d.swipe(600,1100, 600, 300)
            
            if(nextL.exists == True):
                nextL.click()
                time.sleep(5)


            if(packagingC.exists == True):
                packagingC.click()
                time.sleep(5)
                gB = d(text = "Good Box", resourceId = "org.alias:id/selectableGridItemText")
                if(gB.exists == True):
                    gB.click()
                    time.sleep(5)
                
            if(price.exists == True):
                price.click()
                time.sleep(5)
                dr.shell(f'input text "{priceData}"')
                time.sleep(1)
                d.press.back()
                
            
            
            
            if(check.exists == True):
                AStarting = False
                AUploading = True
            
        while AUploading == True:
            
            check = d(resourceId = "marketplace_camera_roll_android_back_button")
            next1 = d(text = "Next")
            if(check.exists == True):
                #something with uploading
                postparser.FBgetPhotos(index)
                if(next1.exists == True):
                    next1.click()
                    time.sleep(5)
                    print("finished uploading")
                    AUploading = False
                    AInputting = True
            
            
        while AInputting == True:
            print("input")
            time.sleep(5)
            title = d(text = "Title")
            price = d(text = "Price")
            searchData = d(text = "Search", resourceId = "abstract_typeahead_text_input")
            
            if(title.exists == True):
                title.click()
                time.sleep(5)
                dr.shell(f'input text "{titleForPost}"')
                time.sleep(1)
                d.press.back()
            
            if(price.exists == True):
                price.click()
                time.sleep(5)
                dr.shell(f'input text "{priceData}"')
                time.sleep(1)
                d.press.back()
            
            
            #category
            cateogry = d(text = "Category")
            backArrow = d(description = "Back")
            CSA = d(text = "Clothing, Shoes & Accessories")
            menShoe = d(text = "Men's Shoes")
            womenShoe = d(text = "Women's Shoes")
            typeOfShoe = d(text = "Fashion Sneakers")
            #play around with save
            save = d(text = "Save", className = "android.widget.TextView")
            if(cateogry.exists == True):
                cateogry.click()
                time.sleep(5)
            while(CSA.exists == False):
                if(backArrow.exists == True):
                    backArrow.click()
                    time.sleep(5)
            if(CSA.exists == True):
                    CSA.click()
                    time.sleep(3)
                    if(c == "M"):
                            menShoe.click()
                            time.sleep(4)
                    if(c == "W"):
                            womenShoe.click()
                            time.sleep(4)
                    if(typeOfShoe.exists == True):
                        typeOfShoe.click()
                        time.sleep(5)
                    if(save.exists == True):
                        save.click()
                        time.sleep(5)
                    

                    d.swipe(600,300, 600, 1100, steps = 3)
                    time.sleep(5)
                    d.swipe(600,1100, 600, 300)
                    time.sleep(5)
            
            #sizing
            sizeM = d(text = "Men's Shoe Size")
            sizeW = d(text = "Women's Shoe Size")            
            if(sizeM.exists == True):
                    time.sleep(5)
                    sizeM.click()
            if(sizeW.exists == True):
                    sizeW.click()
                    time.sleep(5)
            if(searchData.exists == True):
                    searchData.click()
                    time.sleep(5)
                    dr.shell(f'input text "{size}"')
                    size = d(text= str(size), className = "android.widget.TextView")
                    if(size.exists == True):
                        size.click()
                        time.sleep(5)
                        d.swipe(600,300, 600, 1100, steps = 3)
                        time.sleep(5)
                        d.swipe(600,1100, 600, 300)
                        time.sleep(5)
            
            #brands
            brandForFB = d(text = "Brand")            
            if(brandForFB.exists == True):
                brandForFB.click()
                time.sleep(5)
                if(searchData.exists == True):
                    searchData.click()
                    time.sleep(5)
                    dr.shell(f'input text "{brand}"')
                    pickBrand = d(text = brand, className = "android.widget.TextView")
                    if(pickBrand.exists == True):
                        pickBrand.click()
                        time.sleep(5)
                time.sleep(5)
                d.swipe(600,300, 600, 1100, steps = 3)
                time.sleep(5)
                d.swipe(600,1100, 600, 300)
                        
            
            
            #condition
            condition = d(text = "Condition")
            new = d(text = "New")
            usedLN = d(text = "Used - Like New")
            
            if(condition.exists == True):
                condition.click()
                time.sleep(5)
                if(conditionS == "U"):
                    usedLN.click()
                if(conditionS == "N"):
                    new.click()
            
            #description
            #test?
            desc = d(text = "Description")            
            if(desc.exists == True):
                eachLine = description.split("|")
                print(eachLine[0])
                desc.click()
                time.sleep(3)
                length = len(eachLine)
                for i in range(length):
                    dr.shell(f'input text "{eachLine[i]}"')
                    dr.shell('input keyevent 66')
                time.sleep(1)
                d.press.back()
                time.sleep(3)
                
                d.swipe(600,300, 600, 1100, steps = 3)
                time.sleep(5)
                d.swipe(600,1100, 600, 300, steps = 2)
                time.sleep(5)
            
            
            ##Continue rest
            collection = d(text = "Sneaker Collection")
            #type the kind of shoe
            
            #listing in other places
            #test?
            listOP = d(text = "List in more places")
            checkBox = d(className = "android.widget.CheckBox", checked = False)
            done = d(text = "Done")
            if(listOP.exists == True):
                listOP.click()
                time.sleep(5)
                while(checkBox.exists == True):
                    checkBox.click()
                    d.swipe(600,600, 600, 500)
                if(done.exists == True):
                    done.click()
                    time.sleep(5)
                
            nextTab = d(text = "Next", className = "android.widget.TextView")
            
            if(nextTab.exists == True):
                nextTab.click()
                time.sleep(5)
                
            
            deli = d(text = "Delivery method")
            pOnly = d(text = "Local pickup only")
            publish = d(text = "Publish", className = "android.widget.Button")
            
            
            #add this when facebook verifies your profile
            SandP = d(text = "Shipping & local pickup")
            sOnly = d(text = "Shipping only")
            method = d(text = "Choose shipping method")
            label = d(text = "Use a prepaid shipping label")
            ownLabel = d(text = "Use your own shipping label")
            shippingrate = d(text = "Shipping rate")
            updated = d(text = "Update")
            
                            
            if(deli.exists == True):
                deli.click()
                time.sleep(5)
                if(pOnly.exists == True):
                    pOnly.click()
                    time.sleep(5)
                if(publish.exists == True):
                    publish.click()
                    time.sleep(5)
                    AInputting = False
                    Arestarting = True
                        
                                    
            
            
        while Arestarting == True:
            closing = d(text = "Close all")
            Youtube = d(text = "YouTube")
            d.press("recent")
            time.sleep(3)
            if(closing.exists == True):
                closing.click()
                time.sleep(10)
                OUrestarting = False
                Alias = True