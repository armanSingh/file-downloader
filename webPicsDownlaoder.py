__author__ = 'Arman Singh'
import urllib
import os

PICS_PATH = "" #add the raw path to the download directory
URL = "" #add the url here

def downloadPics(linkPics):
    fileNumber = 0
    for currentPic in linkPics:
        fileNumber = fileNumber + 1
        print("Downloading file number : %d",fileNumber)
        urllib.urlretrieve(URL+currentPic,currentPic)

def returnProperLinks(linkPics):
    properLinks = []
    for currentLink in linkPics:
        if currentLink.find(".jpg") != -1:
            properLinks.append(currentLink)
            properLinks.append(currentLink)
    return properLinks

def returnLinks(html):
    stringToFind = '<a href='
    endPos = 0
    linkPics=[]
    while 1:
        startPos = html.find(stringToFind,endPos)
        if(startPos == -1):
            break
        startPos = html.find('"', startPos)
        endPos = html.find('"', startPos+1)
        link = html[startPos+1:endPos]
        linkPics.append(link)

    return returnProperLinks(linkPics)
def getLinks():

    html = urllib.urlopen(URL)
    html = html.read()
    print("Page retrieved....")
    linkPics = returnLinks(html)
    print("Links retrieved....")
    downloadPics(linkPics)
    print("Pics Downloaded....")


if not os.path.exists(PICS_PATH):
    os.mkdir(PICS_PATH)
os.chdir(PICS_PATH)
print("Source Directory changed....")
getLinks()

