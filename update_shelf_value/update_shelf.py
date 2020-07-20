import pyodbc
from gpiozero import LED
from time import sleep
import csv
from datetime import datetime
from datetime import timedelta
# remember to connect LED on GPIO 17
# this script is by no means finnished, thogh it still works
# I will fix some of the if statements and some other minor things

# this script is made for my retail store and will not be compatible with yours
# unless you change some some important values

# values you need to change resides on these linse:
# 45
# 72-78
# 122-126
# 148-152



# setting auto increment for registering scan values from 1 and up
autoIncrement = 0

# Set the variable for GPIO nr 17. See docs with map over GPIO for raspberry pi 3
led = LED(17)

# get datetime to use with file being stored after scannng items and shelf_values
getDate = datetime.now()
getDateYMD = getDate.strftime("%Y%m%d")
with open(r'%s_Values_scanned.csv' % getDateYMD,'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['        ''Reading values start'])

with open(r'%s_List_barcodes_scanned.csv' % getDateYMD,'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['        ''Barcode start'])


while True:

    try: # Specifying the ODBC driver, server name, database, username, password
        cnxn = pyodbc.connect(

            'DRIVER={FreeTDS};SERVER=192.168.1.22;PORT=1433;DATABASE=DB_name;UID=username;PWD=passwordfordatabase;TDS_Version=7.4;'

        )
        while True:
            # Create a cursor from the connection

            cursor = cnxn.cursor()

            # GPIO.cleanup(17)
            led.blink(0.2,0.5)

            print('\nScan Barcode')

            scanBarcode = input()

            if scanBarcode[1].isdecimal() and scanBarcode != '' and scanBarcode != '0': # Continue if integer and not empty



# 1st sql connection is for retreiving article id for item being s_Values_scanned
# replace: the tables and columns to the correct names for your sql server
# if you have the article id and the barcode in the same table or the barcode
# works as the article id itself, you dont really need this sql query
# you can then just store the barcode itself in a variable and use it in the next sql query

                sql1 = '''

        SELECT Article.articleId

        FROM (Article

        FULL JOIN ArticleEAN ON Article.articleId = ArticleEAN.articleId)

        WHERE ArticleEAN.eanCode=(?)'''
                rows = cursor.execute(sql1, scanBarcode)
                articleIdInput = cursor.fetchval()

                autoIncrement = autoIncrement+1
                getDate = datetime.now()
                getDateHMS = getDate.strftime("%H%M%S")
                splitNr = 2
                splitTime = [getDateHMS[i:i+splitNr] for i in range(0, len(getDateHMS), splitNr)]

                with open(r'%s_Values_scanned.csv' % getDateYMD,'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Read nr: '+str(autoIncrement)])
                    writer.writerow(['Time for read: '+splitTime[0]+':'+splitTime[1]+':'+splitTime[2]])
                    writer.writerow(['Barcode scanned: '+scanBarcode])
                    writer.writerow(['Retrieved article id: '+str(articleIdInput)])

                with open(r'%s_List_barcodes_scanned.csv' % getDateYMD,'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([scanBarcode,splitTime[0]+':'+splitTime[1]+':'+splitTime[2]])

            elif scanBarcode == '0':
                break

            else:

        	    break

            led.blink(0.05,0.2)
            print('Scan Shelf_value')

            scanStorageShelf = input()

            if scanStorageShelf != '0': # Continue if not 0


# 2nd sql connection is for updating. Here we set shelf value
# into the StorageShelf column in the table articleStock
# the WHERE claus in the line 3 is super important.
# if you decide do any manual queries for testing and rewriting this script,
# do not omit the WHERE clause!!!

        	    sql2 = '''

        UPDATE articleStock

        SET StorageShelf =(?)

        WHERE articleId =(?)'''

        	    cursor.execute(sql2, scanStorageShelf, articleIdInput)

        	    cnxn.commit()



            elif scanStorageShelf == '0':

        	    break

            else:

        	    break




# 3rd connection is just for requesting value that was stored and compare it to value sent.
            sql3 = '''

        SELECT articleStock.StorageShelf

        FROM articleStock

        WHERE articleId=(?)'''

            rows = cursor.execute(sql3, articleIdInput)

            newShelfValue = cursor.fetchval()

            #print('Verdien: '+newShelfValue+' er blitt lagret')
            if newShelfValue == scanStorageShelf:
                with open(r'%s_Values_scanned.csv' % getDateYMD,'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Shelf_value scanned: '+scanStorageShelf])
                    writer.writerow(['Shelf_value registered: '+newShelfValue])
                    writer.writerow([' '])


            else:
                led.blink(0.01,0.05)
                sleep(3)
                break





            # close connection

            cursor.close()

        # remove cursor
        cnxn.close()

    except pyodbc.OperationalError:
        led.off()
        print('Cant connect to database, re-trying..')
        sleep(1)
