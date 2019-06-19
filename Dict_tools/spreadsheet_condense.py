#!/usr/bin/python3.4
import sys, csv, operator

default_fieldnames = ['original','stripped','in_dict','monosegmental','zero_diff']

def remove_nondorsal(key):
    return key

def main(argv):
    #first arg  = input spreadsheed
    #second arg = output spreadsheet

    # condensed_sheet structure:
    # {'stem' : {'in_dict : '', 'monosegmental' : '', zero_diff : '', 'multiple_witnesses' : ''}}
    condensed_sheet = {}
    fieldnames = default_fieldnames
    with open(argv[0]) as input_spreadsheet:
        dr = csv.DictReader(input_spreadsheet)
        fieldnames = list(dr.fieldnames)

        for row in dr:
            if row['stripped'] in condensed_sheet:
                condensed_sheet[row['stripped']]['multiple_witnesses'] = 1
            else:
                condensed_sheet[row['stripped']] = {'in_dict' : row['in_dict'], 'monosegmental' : row['monosegmental'],
                                                    'zero_diff' : row['zero_diff'], 'multiple_witnesses' : 0}
        print("done with set-ifying!")

    with open(argv[1],'w') as output_spreadsheet:
        writer = csv.DictWriter(output_spreadsheet, fieldnames=['stripped', 'type', 'in_dict', 'monosegmental', 'zero_diff'] )
        writer.writeheader() 
        for key, value in condensed_sheet.items():
            row = {'stripped' : key, 'type' : remove_nondorsal(key), 'in_dict' : value['in_dict'],
                   'monosegmental' : value['monosegmental'], 'zero_diff' : value['zero_diff']}
            writer.writerow(row)
        print("done writing output!")

    return

if __name__ == '__main__':
    main(sys.argv[1:])

    #for key, value in dict.iteritems():
    #   temp = [key,value]
    #   dictlist.append(temp)