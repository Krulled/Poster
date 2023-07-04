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

#loops
timing = True
parsing = False
OfferUp = False
Facebook = False
PoshMark = False
Ebay = False
Alias = False #determine through parsing

#extra vars
shipClicked = False


while True:
    
    ##Timing for when posts should be 
    while timing == True:
        now = str(datetime.datetime.now().time())
        now = timestring = now[:5] 
        if(("09:" in now) or ("10:" in now) or ("11:" in now) or ("12:" in now) or ("13:" in now) or ("14:" in now) or ("15:" in now) or ("16:" in now) or ("17:" in now)):
            if(":30" in now):
                print("time")
                timing = False
                parsing = True

            
          
    
    ##parsing post data
    while parsing == True:
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
        parsing = False
        OfferUp = True
        
    ##finished, test the loops and album parser 
    if OfferUp == True:
        OUstarting = False
        OUuploading = False
        OUinputting = False
        OUrestarting = False
        
        
        
        while OUstarting == True:
            print("starting")
            folder = d(text = "Poster")
            OF = d(text= "OfferUp")
            post = d(resourceId = "tab-bar-widget.tab.post.touchable-opacity")
            check = d(text = "Post an Item")
            
            
            if(folder.exists == True):
                folder.click()
                time.sleep(5)
                
            if(OF.exists == True):
                OF.click()
                time.sleep(5)
                
            if(post.exists == True):
                post.click()
                time.sleep(5)
                
            if(check.exists == True):
                OfferUp = False
                OUuploading = True
    
            
        ##uploading Photo to the post
        while OUuploading == True:
            
        ## edit to where it goes into album, selects cover photo and 4 other photos
            select = d(text = "Select photo")
            done = d(text = "Done")
            
            if(select.exists == True):
                select.click()
                time.sleep(5)
                postparser.OUgetPhotos(index)
                
                if(done.exists == True):
                    done.click()
                    OUuploading = False
                    OUinputting = True
              
                
        #inputting all details
        while OUinputting == True:
            title = d(resourceId = "post-flow-screen.1.listing-title.input.text-entry", className = "android.widget.EditText")
            desc = d(text = "Items with a detailed description sell faster!", className = "android.widget.EditText")
            nextB = d(text = "Next", resourceId = "post-flow-screen.1.next.button.title")
            
            #second page
            category = d(text = "Category (required)", resourceId = "post-flow.2.category.text")
            mens = d(text = "Men's shoes", resourceId = ".category.3.3.flex-row.main.text")
            womens = d(text = "Women's shoes", resourceId = ".category.3.2.flex-row.main.text")
            
            
            cond = d(text = "Condition (required)")
            n = d(text = "New", resourceId = "ucl.flex-row.main.text")
            u= d(text = "Used (normal wear)", resourceId = "ucl.flex-row.main.text")
            
            
            nextC = d(text = "Next", resourceId = "post-flow-screen.2.next.button.title")
            
            #third page
            
            price = d(text = "Price", resourceId = "post-flow-screen.3.navigation-bar.title.text")
            nextD = d(text = "Next", resourceId = "post-flow-screen.3.next.button.title")
            
            
            #final page
            post = d(text = "Post", resourceId = "post-flow-screen.4.post.button.title")
            done = d(text = "Done", resourceId = "post-flow-screen.5.done.button.title")
            
            if(title.exists == True):
                    title.click()
                    time.sleep(3)
                    title.click()
                    dr.shell(f'input text "{titleForPost}"')
                    time.sleep(1)
                    d.press.back()
                    time.sleep(3)
                
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
        
            if(nextB.exists == True):
                nextB.click()
                time.sleep(10)
                
            if(category.exists == True):
                category.click()
                time.sleep(5)
                if(mens.exists == True and womens.exists == True):
                    if(c == "M"):
                        mens.click()
                        time.sleep(4)
                    if(c == "W"):
                        womens.click()
                        time.sleep(4)
            
            if(cond.exists == True):
                cond.click()
                time.sleep(5)
                if(n.exists == True and u.exists == True):
                    if(condition == "N"):
                        n.click()
                        time.sleep(4)
                    if(condition == "U"):
                        u.click()
                        time.sleep(4)
                        
            
            if(nextC.exists == True):
                nextC.click()
                time.sleep(4)
            
            if(price.exists == True):
                dr.shell(f'input text "{priceData}"')
                time.sleep(3)
            
            if(nextD.exists == True):
                nextD.click()
                time.sleep(3)
                
                    
            if(post.exists == True):
                d.click(650,375)
                time.sleep(3)
                post.click()
                time.sleep(10)
                
            if(done.exists == True):
                done.click()
                time.sleep(10)
                inputting = False
                restarting = True
                
        ##clearing out text
        while OUrestarting == True:
            closing = d(text = "Close all")
            Youtube = d(text = "YouTube")
            d.press("recent")
            time.sleep(3)
            if(closing.exists == True):
                closing.click()
                time.sleep(10)
                OUrestarting = False
                Facebook = True
            
    #finished coding input and testing
    if Facebook == True:
        FBstarting = True
        FBuploading = False
        FBinputting = False
        FBrestarting = False
        
        while FBstarting == True:
            print("starting")
            folder = d(text = "Poster")
            FB = d(text= "Facebook")
            MP = d(description = "Marketplace, tab 4 of 6")
            sell = d(text = "Sell")
            listingCreate = d(text = "Create Listing")
            items = d(text= "Items", className = "android.widget.Button")
            addPhoto = d(text = "Add photos / video")
            check = d(resourceId = "marketplace_camera_roll_android_back_button")
            
            
            if(folder.exists == True):
                folder.click()
                time.sleep(5)
                
            if(FB.exists == True):
                FB.click()
                time.sleep(5)
                    
            if(MP.exists == True):
                MP.click()
                time.sleep(5)
                
            if(sell.exists == True):
                sell.click()
                time.sleep(5)
                
            if(listingCreate.exists == True):
                listingCreate.click()
                time.sleep(5)
                
            if(items.exists == True):
                items.click()
                time.sleep(5)
                
            if(addPhoto.exists == True):
                addPhoto.click()
                time.sleep(5)
            
            if(check.exists == True):
                FBstarting = False
                FBuploading = True
            
        while FBuploading == True:
            
            check = d(resourceId = "marketplace_camera_roll_android_back_button")
            next1 = d(text = "Next")
            if(check.exists == True):
                #something with uploading
                postparser.FBgetPhotos(index)
                if(next1.exists == True):
                    next1.click()
                    time.sleep(5)
                    print("finished uploading")
                    FBuploading = False
                    FBInputting = True
            
            
        while FBInputting == True:
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
                    FBInputting = False
                    FBrestarting = True
                        
                                    
            
            
        while FBrestarting == True:
            closing = d(text = "Close all")
            Youtube = d(text = "YouTube")
            d.press("recent")
            time.sleep(3)
            if(closing.exists == True):
                closing.click()
                time.sleep(10)
                OUrestarting = False
                PoshMark = True
                                          
            
    if PoshMark == True:
        PMrestarting = True
        PMInputting = False
        PMuploading = False
        PMrestarting = False       
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