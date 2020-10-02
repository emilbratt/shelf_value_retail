Written: 20.07.2020 Emil B. Børsting
1. Get python..

If linux, python is already installed.
Download and install pip3.

If Windows, download python from python website.
Download and install pip3

2. Get modules needed for scripts
Pillow
https://pypi.org/project/Pillow/
docs.
https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

natsort
https://pypi.org/project/natsort/
docs.
https://natsort.readthedocs.io/en/master/howitworks.html

python-barcode
https://pypi.org/project/python-barcode/
docs.
https://python-barcode.readthedocs.io/en/latest/barcode.html


Creating barcodes:
I made a test list of shelf values in:
/barcode_generator/template.csv

Open /barcode_generator/template.Calc to edit it if you want to,
but keep the format as x-x-x or x-x-xx.
Save the file as .csv in the same directory as the template.Calc

Open 1_generate_barcodes_from_csv.py
	type in the name of barcode standard you want to use
		for exapmle you can type: code128 and then press enter
        to chose code128
	chose PNG if you want to be able to resize
	type in name of csv but skip the ".csv" part
        for example template to test the csv file that is
        already there
	watch it create all barcodes listed in the csv file..

If you chose png then you can use the other scripts to  resize the barcodes and also put them into
an A4 sized image file for ease of printing to paper.
Remember that you have first to do the resize to 560x80.
Then place them in A4 sheets after. (See script 2 and 3).

Open 2_resize_raw_size_png_to_560x80
	watch it convert and place the text of barcode to a smaller more "neat" format

Open 3_merge_png_560x80_to_A4.py
	watch it put all barcodes onto a size A4 png sheet(s)
