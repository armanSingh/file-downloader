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

def findFirstNumber(aLink):
    cur = 0
    for i in aLink:
        if i.isdigit():
            return cur
        cur = cur+1
    return cur

def refineLinks(allLinks):
    refinedlinks=[]
    curPos = 0
    allLen = allLinks.__len__()
    while curPos < allLen:
        matchFrom = allLinks[curPos]
        index = findFirstNumber(matchFrom)
        j=curPos+1
        finalString = ""
        while j < allLen and allLinks[j][0:index+1] in allLinks[curPos][0:index+1]:
            finalString = allLinks[j]
            j = j+1
        curPos = j
        refinedlinks.append(finalString)

    #####################################################
    return refinedlinks

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

def findDirectory(html, newURL):
    properLinks = []
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
    for currentLink in linkPics:
        if currentLink[-1] == '/' and currentLink[0] != '/':
            print(newURL, currentLink)
            properLinks.append(newURL+currentLink)
    if properLinks.__len__() == 0:
        return -1
    return properLinks

def getLinks():

    directoryList = []
    allLinks = []
    directoryList.append(URL)
    for i in directoryList:
        html = urllib.urlopen(i)
        html = html.read()
        newCollection = findDirectory(html, i)
        linkPics = returnLinks(html)
        #print linkPics.__len__(), directoryList.__len__(), allLinks.__len__()
        for currentLink in linkPics:
            allLinks.append(currentLink)
        if newCollection != -1:
            for elem in newCollection:
                 directoryList.append(elem)
    finalLinks = refineLinks(allLinks)
    print allLinks.__len__(),finalLinks.__len__()
    refineLinks(allLinks)
    with open("Links.txt",'w') as curFile:
        for i in finalLinks:
            curFile.write(i)
            curFile.write("\n")

    #################################
    downloadPics(allLinks)
    #################################

def setProxy():
    proxy = urllib2.ProxyHandler({'http':'http://edcguest:edcguest@172.31.100.26:3128'})
    auth = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

if __name__ == '__main__':
    if not os.path.exists(PICS_PATH):
        os.mkdir(PICS_PATH)
    os.chdir(PICS_PATH)
    print    os.getcwd()
    print("Source Directory changed....")
    getLinks()
