## functions
import postparser
import time
import datetime
import random
import configparser

## necessary imports
from uiautomator import Device
d = Device('R58R746PGVD')
from ppadb.client import Client
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
t.dr = devices[0]

filename = "num.config"
config = configparser.ConfigParser()
config.read(filename)
def parsePic():
        #parsing picture details       
        f = open("post.txt", "r")
        lines = f.readlines()
        emailContent = lines[getPost()].split(":")
        f.close()
        title = emailContent[0].strip()
        price = emailContent[1].strip()
        description =  emailContent[2].strip()
        condition = emailContent[3].strip()
        brand = emailContent[4].strip()
        color = emailContent[5].strip()
        size = emailContent[6].strip()
        category = emailContent[7].strip()
        alias = emailContent[8].strip()
        sku = emailContent[9].strip()
        return title, price, description, condition, brand, color, size, category,alias,sku
    

def getPost():
    postNum = config.getint('Changing', 'post')
    return postNum
        
def changePosts(postNum):
     postNum = postNum + 1
     if(postNum == 13):
         postNum = 1
     cnfFile = open(filename, "w")
     config.set("Changing", "post", str(postNum))
     config.write(cnfFile)
     cnfFile.close()
        
def FBgetPhotos(postNum):
    picker = d(resourceId = "marketplace_camera_roll_android_header_open_album_picker")
    shoeString = "Shoe " + str(postNum)
    shoe = d(text = shoeString)
    nextd = d(text = "Next")
    
    if(picker.exists == True):
        picker.click()
        time.sleep(5)
        
    if(shoe.exists == True):
        shoe.click()
        time.sleep(5)
        cover = random.randint(1,3)
        if(cover == 1):
            d.click(350,270)
        if(cover == 2):
            d.click(600,270)
        if(cover == 3):
            d.click(100,500)
        d.click(380,520) #4
        d.click(600,550) #5
        d.click(150,750) #6
        d.click(330,740) #7
        d.click(600,720) #8
        d.click(146,980) #9
        d.click(300,1000) #10
        d.click(580,1000) #11
        #check out later590,1000
        time.sleep(5)
        if(nextd.exists == True):
            nextd.click()
            return True
        
    if(shoe.exist == False):
        print("idk")
    
def PMgetphotos(postNum):
    picker = d(text = "Tap to see albums")
    shoeString = "Shoe " + str(postNum)
    shoe = d(text = shoeString)
    
    if(picker.exists == True):
        picker.click()
        time.sleep(5)
        
    if(shoe.exists == True):
        shoe.click()
        time.sleep(5)
    cover = random.randint(1,3)
    if(cover == 1):
        d.click(100,467)
    if(cover == 2):
        d.click(240,470)
    if(cover == 3):
        d.click(445,470)
    d.click(631,470) #4
    d.click(100,644) #5
    d.click(240,644) #6
    d.click(445,644) #7
    d.click(631,644) #8
    #d.click(570,780) #9
    #d.click(90,1000) #10
    return
    #if(postNum == 11):
        #return 300,1000
    #if(postNum == 12):
        #return 590,1000
    
def OUgetPhotos(postNum):
    picker = d(text = "Tap to see albums")
    shoeString = "Shoe " + str(postNum)
    shoe = d(text = shoeString)
    
    
    if(picker.exists == True):
        picker.click()
        time.sleep(5)
        
    if(shoe.exists == True):
        shoe.click()
        time.sleep(5)
    cover = random.randint(1,3)
    if(cover == 1):
        d.click(350,270)
    if(cover == 2):
        d.click(600,270)
    if(cover == 3):
        d.click(100,500)
    d.click(380,520) #4
    d.click(600,550) #5
    d.click(150,750) #6
    d.click(330,880) #7
    d.click(600,270) #8
    d.click(570,780) #9
    d.click(90,1000) #10
    return
    #if(postNum == 11):
        #return 300,1000
    #if(postNum == 12):
        #return 590,1000
    

def IGPickOut():
    IGNum =  config.getint('Changing', 'IG')
    openCamera = d(description = "Open camera")
    select = d(text = "Select")
    nextButton = d(text = "Next",resourceId = "com.instagram.android:id/media_thumbnail_tray_button_text")
    seperateButton = d(resourceId = "com.instagram.android:id/gallery_grid_format_separate")
    startIndex = d(resourceId = "com.instagram.android:id/thumbnail_image", index = 1)
    if(select.exists == True):
        select.click()
        d.click(360,470)
        d.click(620,470)
        d.click(97,882)
        d.click(360,882)
        d.click(620,882)
        d.click(97,1215)
        d.click(360,1215)
        d.click(620,1215)
        d.swipe(540,1236,570,765)
        time.sleep(3)
        d.click(148,1198)
        d.click(374,1198)
        if(nextButton.exists == True):
            nextButton.click()
            time.sleep(4)
        if(seperateButton.exists == True):
            seperateButton.click()
            time.sleep(4)
        d.swipe(35,1411, 507,1411)