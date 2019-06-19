# -*- coding: utf-8 -*-
#  
#  This code must be run in python 3.X
#  Sorry.
#
#  Couldn't be bothered to handle all the unicode in 2.7

import sys, csv, re
from arabic_to_latin import arabic_to_ASCII

default_fieldnames = ['url', 'category', 'entry_eng', 'entry_ug', 'entry_ug_ar']
default_data = []

def ensure_unicode(v):
    if isinstance(v, str):
        v = v.decode('utf8')
    return unicode(v)  # convert anything not a string to unicode too

class CSV_helper:
    def __init__(self, ifile, ofile, ofile_ascii):
        self.data = default_data
        self.fieldnames = default_fieldnames
        
        with open(ifile) as csvfile:
            dr = csv.DictReader(csvfile)
            for row in dr:
                entry_eng = row['entry_eng']
                url = row['url']
                category = row['category']
                entry_ug = re.sub("\(.*\)", "", row['entry_ug'])
                entry_ug = re.sub("\s\s*\.", "", entry_ug)
                entry_ug = re.sub("-\s\s*", "", entry_ug)
                entry_ug = re.sub("\.\.*\s\s*", "", entry_ug)


                entry_ug_ar = re.sub("\(.*\)", "", row['entry_ug_ar'])


                entries_ug = [] 
                for entry in re.split(',|;', entry_ug):
                    if len(entry.strip().split(' ')) == 1:
                        entries_ug.append(entry.strip())
                entries_ug_ar = []
                for entry in re.split('،|؛', entry_ug_ar):
                    if len(entry.strip().split(' ')) == 1:
                        entries_ug_ar.append(entry.strip())
             
                if 'verb' in category:
                    for i, entry in enumerate(entries_ug):
                        if entry.endswith('maq') or entry.endswith('mek'):
                            entries_ug[i] = entry[:-3]
                    for i, entry in enumerate(entries_ug_ar):
                        if entry.endswith('ماق') or entry.endswith('مەك'):
                            entries_ug_ar[i] = entry[:-3]

                for i in range(min(len(entries_ug),len(entries_ug_ar))):
                    self.data.append({'url' : url, 'category' : category, 'entry_eng' : entry_eng, 'entry_ug' : entries_ug[i], 'entry_ug_ar' : entries_ug_ar[i]})

        with open(ofile, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            for row in self.data:
                 writer.writerow(dict((k, v) for k, v in row.items()))

        ascii_data = []
        for row in self.data:
            ascii_data.append({'category' : row['category'][4:-4], 'entry_eng' : row['entry_eng'], 'entry_ug_ASCII' : arabic_to_ASCII(row['entry_ug_ar'])})

        with open(ofile_ascii, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['category', 'entry_eng', 'entry_ug_ASCII'])
            writer.writeheader()
            for row in ascii_data:
                if '-' not in row['entry_ug_ASCII']:
                    writer.writerow(dict((k, v) for k, v in row.items()))


def main(argv):         #ifile   ofile    ofile_ascii
    helper = CSV_helper(argv[0], argv[1], argv[2])
    print("done :)")

if __name__ == '__main__':
    main(sys.argv[1:])