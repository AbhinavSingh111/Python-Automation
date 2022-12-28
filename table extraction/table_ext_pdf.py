# to install table from pdf we need a library 'camelot-py'
# before installing camelot , install 2 dependencies --> tk , ghostscript
import camelot
import os
# import cv2
tables = camelot.read_pdf('D:\Python Automation\table extraction\ab.pdf')
print(tables)
tables.export('ab.csv',f='csv',compress=True)
tables[0].to_csv('ab.csv')

# for some reasons camelot is not working , the vs code is choosing PyPDF2 in order to handle the pdf