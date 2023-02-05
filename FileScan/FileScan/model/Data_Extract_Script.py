pip install 'PyPDF2<3.0'

import PyPDF2
import os
import csv

header = ['File Name', 'Content']

f = open('/content/Extract_Text.csv', 'w')

# create the csv writer
writer = csv.writer(f)

writer.writerow(header)
# write a row to the csv file

# close the file
f.close()

for file_name in os.listdir('Research'):
  print(file_name)
  load_pdf=open(r'/content/Research/'+file_name,'rb')
  read_pdf = PyPDF2.PdfReader(load_pdf)
  page_count = read_pdf.getNumPages()
  print(page_count)
  i=0

  while i >= page_count:
    first_page = read_pdf.getPage(i)
    page_content = first_page.extractText()
    page_content = page_content.replace('\n', '')
    i=i+1
    print(page_content)
 
    data = [file_name, page_content]
    f = open('/content/Extract_Text.csv', 'a')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(data)

  # close the file
  f.close()