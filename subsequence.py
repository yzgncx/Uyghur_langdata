#!/usr/bin/python3.4
import sys, csv, re

#===========================#
# Consonant and Vowel lists #
#===========================#
CONSONANTS = ['p','b','t','d','C','J','k','g','q','G','P','m','n','N','f','s','z','S','Z','x','h','r','l','j','w']
CONS_REGEX = re.compile('['+''.join(CONSONANTS)+']')
VOWELS = ['i','I','o','O','u','y','a','e']
VOWELS = re.compile(''.join(CONSONANTS))
# Vowel Sequences
#
def vowel_seq(infile, outfile):
    vowel_seqs = []
    with open(infile) as csvfile:
        dr = csv.DictReader(csvfile)
        for key in dr:
            vowel_seqs.append(CONS_REGEX.sub('', key['word']))
    print(vowel_seqs)

def main():
    infile = sys.argv[1]
    outfile = sys.argv[2]
    vowel_seq(infile, outfile)

if __name__ == "__main__":
    main()