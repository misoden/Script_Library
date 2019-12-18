# -*- coding: utf-8 -*-
"""
Author:
@ misoden
CSV to Pipe Delimited
"""

import csv

inFile = input('Please enter input file name: ')
outFile = input('Please enter output file name:')

# Update file path as needed
with open(f'C:/temp/{inFile}.csv', 'rt') as fin, \
      open(f'C:/temp/{outFile}.txt', 'wt',newline='') as fout:
    reader = csv.DictReader(fin)
    writer = (dict((k, v.strip()) for k, v in row.items() if v) for row in reader)
    writer = csv.DictWriter(fout, reader.fieldnames, delimiter='|', quoting=csv.QUOTE_NONE, escapechar=' ')
    writer.writeheader()
    writer.writerows(reader)


    
