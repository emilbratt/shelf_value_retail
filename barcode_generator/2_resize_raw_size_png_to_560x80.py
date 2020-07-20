import glob
import os
from PIL import Image, ImageDraw
from PIL import ImageFont



print('1 = barcodes reside in "sorted_barcodes"\n2 = barcodes reside in "output"')
print('Type 1 or 2 then press enter')
folderChoice = int(input())

if folderChoice == 1:
    # folderName = input('name of subfolder inside sorted_barcodes: ')
    folderName = input('Foldername inside sorted_barcodes: ')
    currentPath = os.getcwd() # store current path in variable
    subDirectory = os.path.join(currentPath, 'sorted_barcodes', folderName)
    os.chdir(subDirectory)
elif folderChoice == 2:
    currentPath = os.getcwd()
    subDirectory = os.path.join(currentPath, 'output')
    os.chdir(subDirectory)

# Store the image file names in a list as long as they are png`s
images = [f for f in os.listdir(subDirectory) if os.path.splitext(f)[-1] == '.png']

for fileName in images:
    # imageCropOut = Image.open(fileName) # open image to crop out barcode readble value
    openBarcode = Image.open(fileName) # open same imgage to have cropped part pasted
    image560x80 = Image.new('RGB', (560,80), (255, 255, 255)) # open another blank 590x100 image to put the finished cropped image
    print('Barcode: '+fileName) # print info of image

    imageRes = openBarcode.size
    imgResHorizontal = imageRes[0]
    imgResVertical = imageRes[1]
    print('Width: '+str(imageRes[0]))
    print('Height: '+str(imageRes[1]))


    boxCrop = (0, 80, (imgResHorizontal), 160) # crop 10 px from left to 260 px from left and 260 px from top to 270 px from top
    # boxCrop values represents: (pixels from left, pixels from top, res crop horizontal, res crop vertiacl)
    croppedRegion = openBarcode.crop(boxCrop) # using the crop() and stare the cropped object in croppedRegion
    image560x80.paste(croppedRegion, (250,0)) # use paste() and pasting the values into imageCropPaste same image
    # paste values represents: (pxiels from left, pixels from top)



    # get a font
    fontUsed = ImageFont.truetype("arial.ttf", 72)
    # get a drawing context
    textInput = ImageDraw.Draw(image560x80)

    # draw text
    textInput.text((0,0), fileName[0:-4], font=fontUsed, fill=(0, 0, 0))

    # image560x80.show()

    image560x80.save(fileName)




    # input()
