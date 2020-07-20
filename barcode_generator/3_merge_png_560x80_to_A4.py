import glob
import os
from PIL import Image, ImageDraw
from natsort import natsorted

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

# Store the image file names in a list as long as they are png
images = [f for f in os.listdir(subDirectory) if os.path.splitext(f)[-1] == '.png']

# images.sort(reverse=True)
readNumberFiles = len(images)-1



# the while loope iterates from last index to first index, thus we
# have to reverse order the list for it to start with the first index
images = natsorted(images, reverse=True)
print(str(readNumberFiles)+'\n')

saveimage2480x3508=1

pasteLeft = 50
pasteTop = 10


iterateNumber = 19

newBlank = 0

# open a blank 1240x1754 image to put the finished cropped image
image2480x3508 = Image.new('RGB', (1240,1754), (255, 255, 255))

while readNumberFiles != -1:

    if iterateNumber == 0:
        iterateNumber= 19

        pasteLeft = pasteLeft + 630
        pasteTop = 10
        print('check')
    else:
        if newBlank == 38:
            newBlank = 0
            iterateNumber= 19
            pasteLeft = 50
            pasteTop = 10
            saveimage2480x3508 = saveimage2480x3508+1

            # open another blank 330x100 image to put the finished cropped image
            image2480x3508 = Image.new('RGB', (1240,1754), (255, 255, 255))

        print(images[readNumberFiles])

        openBarcode = Image.open((images[readNumberFiles])) # open barcode image
        print('barcode: '+openBarcode.format, openBarcode.size, openBarcode.mode) # print info of image

        image2480x3508.paste(openBarcode, (pasteLeft,pasteTop)) # use paste() and pasting the values into imageCropPaste same image
        # paste values represents: (pxiels from left, pixels from top)

        image2480x3508.save(str(saveimage2480x3508)+'.png')

        pasteTop = pasteTop + 92
        print('Pixels from top: '+str(pasteTop))
        print('Pixels from left: '+str(pasteLeft))
        readNumberFiles = readNumberFiles-1
        iterateNumber = iterateNumber-1
        newBlank = newBlank +1
        print(iterateNumber)
        print(readNumberFiles)
        print(newBlank)
