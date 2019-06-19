import sys, csv, re
import arabic_to_latin

def main(argv):
    affixes = []
    affixes_arabic = []

    with open(argv[0], 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            for item in row:
                for affix in item.split('-'):
                    if affix.strip():
                        affixes.append(affix.strip())
#            affixes.append(row)
    
    affixes.sort(key=len, reverse=True)
    
    for affix in affixes:
        affixes_arabic.append(arabic_to_latin.ULY_to_arabic_greedy(affix))

    print(affixes)
    print('\n')
    print(affixes_arabic)


    return


if __name__ == '__main__':
    main(sys.argv[1:])