import os
import PIL
from PIL import Image

outputPath = "./output"
inputPath = "./input"

dir_list = os.listdir(inputPath)

fileCount = dir_list.__len__()

print("fileCount: " + str(fileCount))

name = input("Wat is de label?")
newSize = 500
maxSize = 500
i = 0

for dir in dir_list:
    oldImage = PIL.Image.open(inputPath + "/" + dir)
    oldImage.thumbnail((500,500), PIL.Image.Resampling.LANCZOS)

    widthOfset = int((maxSize - oldImage.size[0]) / 2)
    heightOfset = int((maxSize - oldImage.size[1]) / 2)

    newImage = PIL.Image.new("RGB", (maxSize, maxSize), (255, 255, 255))
    newImage.paste(oldImage, (widthOfset, heightOfset))

    newImage.save(outputPath + "/" + name + str(i) + ".jpg")
    i += 1

