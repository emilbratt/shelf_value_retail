import csv
import barcode
from barcode.writer import ImageWriter
from PIL import Image



print('Chose barcode standard')
print(barcode.PROVIDED_BARCODES) # prints out compatible barcode types
barChoice = input() # by typing in correctly you set the type and store it in the variable
barType = barcode.get_barcode_class(barChoice) # this imports that excact type into generator
print(barType)
print('Press 1 for SVG or 2 for PNG?')
fileformatChoice = input()
print('Type name of file')
nameFile = input() # name of the csv file to import (only name not the .csv extention)
if fileformatChoice == '1':
    with open("%s.csv" % nameFile) as readCSV:
        reader = csv.reader(readCSV) # open csv file and store into reader
        for row in reader: # for every row in reader do:
            x = ("".join(row)) # converting each row from list to a string
            barValue = barType(x) # store the raw value of barcode
            print(barValue) # print out the raw value
            fileName = barValue.save('./output/%s' % x) # save the barcode as .svg in folder "output"
            print(fileName)


elif fileformatChoice == '2':
    with open("%s.csv" % nameFile) as readCSV:
        reader = csv.reader(readCSV) # open csv file and store into reader
        for row in reader: # for every row in reader do:
            x = ("".join(row)) # converting each row from list to a string
            barValue = barType(x, writer=ImageWriter()) # store the raw value of barcode
            print(barValue) # print out the raw value
            fileName = barValue.save('./output/%s' % x) # sav ethe barcode as .png in folder "output"
            convertMonochrome = Image.open(fileName).convert('LA') # open the same png file using the filename stored and convert to monochrome
            convertMonochrome.save(fileName) # save the new monochome png and overwrite the existing one
            print(fileName) # print out the filename
