__author__ = 'Arman Singh'
PATH = "E:\Users\Arman Singh\Pictures/107_FUJI"
import os

os.chdir(PATH)
contents = os.listdir(PATH)
with open("E:\Users\Arman Singh\Pictures/107_FUJI\Web Viewer.html","w") as curfile:
  curfile.write("<body>")
  for currentFile in contents:
    if os.path.isfile(os.path.join(PATH, currentFile)):
        curfile.write("<a href ="+"\"file:///" + "E:\Users\Arman Singh\Pictures/107_FUJI/" + currentFile + "\" >")
        curfile.write(currentFile[:-4])
        curfile.write("</a>")
        curfile.write("<br/>")
        curfile.write("\n")
  curfile.write("</body>")