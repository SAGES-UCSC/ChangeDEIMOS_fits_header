#!/usr/bin/env python
# Filename: modifyHeader_date.py

# Written by Nicola Pastorello - 29/01/15
#

import numpy, pyfits


nameFitsFile = '3N4474.fits'
newDate = '2015-03-12'
inputFile = pyfits.open(nameFitsFile)



# Identify which extension has to be changed

layer, namecol = '', ''
for ii in inputFile:
  for jj in ii.header.keys():
    if ii.header[jj] == 'Date_Use':
      if layer == '' and namecol == '':
        layer, namecol = ii, jj
      else:
        print "Duplicates"
        dummy = raw_input('Column name "Date_Use" in multiple extensions.')

layer.data['Date_Use'] = newDate

flag = True
while flag:
  answer = raw_input('Do you want to overwrite previous file? (y/n) ')
  if answer[0] == 'y' or answer[0] == 'Y':
	inputFile.writeto(nameFitsFile); flag = False
  elif answer[0] == 'n' or answer[0] == 'N': 
   inputFile.writeto(nameFitsFile[:-4]+'bis.fits'); flag = False
  else:
   print 'Wrong answer dude...'


print "Observing date changed. Vince stinks, Nicola rocks!"