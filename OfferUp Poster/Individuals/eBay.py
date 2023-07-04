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


EStarting = True
EUploading = False
EInputting = False
Erestarting = False

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
print(SKU)
       
while(True): 
        while EStarting == True:
            print("starting")
            folder = d(text = "Poster")
            eBay = d(text= "eBay")
            searching = d(text = "Search on eBay")
            jordanMen = d(textContains = "jordan", resourceId = "com.ebay.mobile:id/search_suggestion_text")
            AG = d(text= "I Authenticity Guarantee")
            item = d(text = "Item", packageName = "com.ebay.mobile")
            solt = d(text = "Sell One Like This", resourceId = "com.ebay.mobile:id/cta_button")
            check = d(text = "Listing summary")        
            #check if the variable for alias is true
            if(folder.exists == True):
                folder.click()
                time.sleep(5)
                
            if(eBay.exists == True):
                eBay.click()
                time.sleep(5)
                
            if(searching.exists == True):
                searching.click()
                time.sleep(5)
                dr.shell(f'input text "Jordans"')
                time.sleep(5)
                if(jordanMen.exists == True):
                    jordanMen.click()
                    time.sleep(5)
                if(AG.exists == True):
                    AG.click()
                    time.sleep(5)
            
            if(item.exists == True):
                time.sleep(5)
                print("in loop")
                while(solt.exists == False):
                    d.swipe(600,1100, 600, 300)
                    time.sleep(2)
                    
                if(solt.exists == True):
                    solt.click()
                    time.sleep(5)
            
            if(check.exists == True):
                EStarting = False
                EUploading = True
            
        while EUploading == True:
            print("uploading")
            addPhotos = d(description = "Add photos", packageName = "com.ebay.mobile")
            selectAlbum = d(description = "Select from gallery", packageName = "com.ebay.mobile")
            gallery = d(text = "Gallery", resourceId = "android:id/title")
            albums = d(text = "Albums")
            Doned = d(text = "Done", resourceId = "com.sec.android.gallery3d:id/action_done")
            backed = d(description = "Navigate up", packageName = "com.ebay.mobile")
            check = d(text = "Listing summary")  
            
            if(addPhotos.exists == True):
                addPhotos.click()
                time.sleep(5)
                
            if(selectAlbum.exists == True):
                selectAlbum.click()
                time.sleep(5)
            
            if(gallery.exists == True):
                gallery.click()
                time.sleep(5)
                
            if(albums.exists == True):
                albums.click()
                time.sleep(5)
                postparser.PMgetphotos(index)
            
            if(Doned.exists == True):
                Doned.click()
                time.sleep(15)
                if(backed.exists == True):
                    backed.click()
                    time.sleep(5)
                    if(check.exists == True):
                        EUploading = False
                        EInputting = True
            
                
            
        while EInputting == True:
            print("inputting")
            #Title
            Title = d(resourceId = "com.ebay.mobile:id/title_content", packageName = "com.ebay.mobile")
            titleMessage = d(resourceId = "com.ebay.mobile:id/title_view", packageName = "com.ebay.mobile")
            titleMessaged = d(text ="Write a descriptive title, 0 of 80 characters entered", resourceId = "com.ebay.mobile:id/title_view", packageName = "com.ebay.mobile")
            
            
            if(Title.exists == True):
                Title.click()
                time.sleep(5)
                if(titleMessage.exists == True):
                    titleMessage.click()
                    time.sleep(5)
                    while(titleMessaged.exists == False):
                        print("loop")
                        titleMessage.click()
                        dr.shell(f'input keyevent 67')
                    time.sleep(1)
                    dr.shell(f'input text "{titleForPost}"')
                    time.sleep(5)
                    time.sleep(5)
                    d.press.back()
                    time.sleep(2)
                    d.press.back()
            
            #item specifics
            specifics = d(resourceId = "com.ebay.mobile:id/details_tap_target")
            if(specifics.exists == True):
                specifics.click()
                time.sleep(5)
                specificsInWork = True
                
                while(specificsInWork == True):
                
                    #Condition
                    conditioned = d(text = "Condition", resourceId = "com.ebay.mobile:id/label")
                    newCondition = d(text = "New with box", resourceId = "com.ebay.mobile:id/listing_form_condition_value_button")
                    usedCondition = d(text = "Pre-owned", resourceId = "com.ebay.mobile:id/listing_form_condition_value_button")
                    
                    if(conditioned.exists == True):
                        conditioned.click()
                        time.sleep(3)
                        if(conditionS == "N"):
                            newCondition.click()
                            time.sleep(3)
                        if(conditionS == "U"):
                            usedCondition.click()
                            time.sleep(3)
                            
                    
                    #brand
                    branded = d(text = "Brand", resourceId = "com.ebay.mobile:id/label")
                    
                    if(branded.exists == True):
                        branded.click()
                        time.sleep(5)
                        searchforBrand = d(text = "Search for Brand")
                        if(searchforBrand.exists == True):
                            searchforBrand.click()
                            time.sleep(5)
                            dr.shell(f'input text "{brand}"')
                            time.sleep(5)
                            shoeBrand = d(text = brand, resourceId = "com.ebay.mobile:id/listing_form_aspect_value_button")
                            if(shoeBrand.exists == True):
                                shoeBrand.click()
                                time.sleep(5)
                                
                        
                    
                    #Shoe Size
                    usSS = d(text = "US Shoe Size", resourceId = "com.ebay.mobile:id/label")
                    if(usSS.exists == True):
                        usSS.click()
                        time.sleep(5)
                        searchforSize = d(text = "Search for US Shoe Size")
                        if(searchforSize.exists == True):
                            searchforSize.click()
                            time.sleep(5)
                            dr.shell(f'input text "{size}"')
                            time.sleep(5)
                            shoeSize = d(text = size, resourceId = "com.ebay.mobile:id/listing_form_aspect_value_button")
                            if(shoeSize.exists == True):
                                shoeSize.click()
                                time.sleep(5)
                    
                    
                    #Style (not needed)
                    
                    #Color (not added)
                    coloring = d(text = "Color", resourceId = "com.ebay.mobile:id/label")
                    
                    
                    #Department (not needed)
                    
                    department = d(text = "Department", resourceId = "com.ebay.mobile:id/label")
                    if(department.exists == True):
                        department.click()
                        unisex = d(text = "Unisex Adults")
                        time.sleep(5)
                        if(unisex.exists == True):
                            unisex.click()
                            time.sleep(5)
                            d.swipe(600,1100, 600, 300)
                    
                    #Type (not needed)
                    
                    type = d(text = "Type", resourceId = "com.ebay.mobile:id/label")
                        
                    
                    #Style Code?
                    
                    styleCode = d(text = "Style Code", resourceId = "com.ebay.mobile:id/label")
                    searchForSC = d(text = "Search for Style Code")
                    if(styleCode.exists == True):
                        styleCode.click()
                        time.sleep(5)
                        if(searchForSC.exists == True):
                            Skuing = d(text = SKU, resourceId = "com.ebay.mobile:id/listing_form_add_text")
                            searchForSC.click()
                            time.sleep(3)
                            dr.shell(f'input text "{SKU}"')
                            if(Skuing.exists == True):
                                Skuing.click()
                                time.sleep(5)
                    #Model
                    productLine = d(text= "Product Line")
                    searchProduct = d(text = "Search for Product Line")
                    branding = d(textContains = brand, resourceId = "com.ebay.mobile:id/listing_form_aspect_value_button")
                    
                    if(productLine.exists == True):
                        productLine.click()
                        time.sleep(5)
                        if(searchProduct.exists == True):
                            searchProduct.click()
                            time.sleep(5)
                            dr.shell(f'input text "{brand}"')
                            time.sleep(5)
                            if(branding.exists == True):
                                branding.click()
                                time.sleep(5)
                                
                    #UK Shoe Size (Clear)
                    UKss = d(text = "UK Shoe Size")
                    clearSelected = d(text = "Clear selected")
                    if(UKss.exists == True):
                        UKss.click()
                        time.sleep(5)
                        if(clearSelected.exists == True):
                            clearSelected.click()
                            time.sleep(5)
                            d.press.back()
                            
                    
                    #model
                    model = d(text = "Model")
                    words=titleForPost.split()
                    k=words[0]+" "+ words[1]
                    modelNumber = k
                    if(model.exists == True):
                        model.click()
                        time.sleep(5)
                        searchForModel = d(text = "Search for Model")
                        if(searchForModel.exists == True):
                            searchForModel.click()
                            time.sleep(5)
                            dr.shell(f'input text "{modelNumber}"')
                            time.sleep(5)
                            shoeModel = d(textContains = modelNumber, resourceId = "com.ebay.mobile:id/listing_form_aspect_value_button")
                            if(shoeModel.exists == True):
                                    shoeModel.click()
                                    time.sleep(5)
                                    d.swipe(600,1100, 600, 300)
                    
                    #release year (Clear)
                    release = d(text = "Release Year")
                    clearSelected = d(text = "Clear selected")
                    if(release.exists == True):
                        release.click()
                        time.sleep(5)
                        if(clearSelected.exists == True):
                            clearSelected.click()
                            time.sleep(5)
                            d.press.back()
                    
                    
                    #EU (Clear)
                    
                    EUss = d(text = "EU Shoe Size")
                    clearSelected = d(text = "Clear selected")
                    if(EUss.exists == True):
                        EUss.click()
                        time.sleep(5)
                        if(clearSelected.exists == True):
                            clearSelected.click()
                            time.sleep(5)
                        d.press.back()
                        #finished
                        time.sleep(3)
                        d.press.back()
                            
                    listingSummary = d(text = "Listing summary")
                    if(listingSummary.exists == True):
                        d.swipe(600,1100, 600, 200)
                        specificsInWork = False
                
            
            
            #Description
            descriptionTab = d(resourceId = "com.ebay.mobile:id/description_tap_target")
            
            if(descriptionTab.exists == True):
                    descriptionTab.click()
                    time.sleep(5)
                    dr.shell(f'input keycombination 113 29 && input keyevent 67')
                    time.sleep(1)
                    dr.shell(f'input text "{description}"')
                    time.sleep(5)
                    d.press.back()
            
            #Pricing
            
            pricingTab = d(resourceId = "com.ebay.mobile:id/pricing_tap_target")
            if(pricingTab.exists == True):
                pricingTab.click()
                auctioon = d(textContains = "Auction", checked = True)
                if(auctioon.exists == True):
                    auctioon.click()
                    time.sleep(5)
                binPricing = d(resourceId = "com.ebay.mobile:id/bin_price")
                if(binPricing.exists == True):
                                        priceForShoe = int(priceData) + 30
                                        StringPrice = str(priceForShoe)
                                        binPricing.click()
                                        time.sleep(5)
                                        dr.shell(f'input keycombination 113 29 && input keyevent 67')
                                        time.sleep(1)
                                        dr.shell(f'input text "{StringPrice}"')
                                        time.sleep(5)
                                        d.press.back()
                                        time.sleep(2)
                                        d.press.back()
                                        time.sleep(3)
                                        d.swipe(600,1100, 600, 300)
                
            #Shipping (covered by authentication)
            
            
            #check if listed and then restart
            clickListing = d(text = "List your item")
            noThanks = d(text = "No Thanks")
            nowLive = d(text = "Your listing is now live.")
            viewIt = d(text = "View listing")
            if(clickListing.exists == True):
                clickListing.click()
                time.sleep(5)
                if(noThanks.exists == True):
                    noThanks.click()
                    time.sleep(5)
                if(viewIt.exists == True or nowLive.exists == True):
                    Erestarting = True
                    EInputting = False


           
        while Erestarting == True:
            closing = d(text = "Close all")
            Youtube = d(text = "YouTube")
            d.press("recent")
            time.sleep(3)
            if(closing.exists == True):
                closing.click()
                time.sleep(10)
                Erestarting = False
                timing = True