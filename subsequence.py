#!/usr/bin/python3.4
import sys, csv, re, itertools

#===========================#
# Consonant and Vowel lists #
#===========================#
CONSONANTS = ['p','b','t','d','C','J','k','g','q','G','P','m','n','N','f','s','z','S','Z','x','h','r','l','j','w']
VOWELS = ['i','I','o','O','u','y','a','e']


CONS_REGEX = re.compile('['+''.join(CONSONANTS)+']')
NONCONS_REGEX = re.compile('[^'+''.join(CONSONANTS)+']')
VOWELS_REGEX = re.compile('['+''.join(VOWELS)+']')
NONVOWELS_REGEX = re.compile('[^'+(''.join(VOWELS))+']')


def bigrams(s):
    return(list(zip(*(s[i:] for i in range(2)))))

# Vowel bigrams
# takes as input two filenames.  The input file should be a CSV with the fieldname 'word'
# Hopefully written to be extensible to other sequence lengths if I find it compelling
def vowel_bigrams(infile, outfile):
    vowel_seqs = []
    bigram_counts = {key: 0 for key in list((itertools.product(VOWELS,VOWELS)))}
    with open(infile) as csv_input:
        dr = csv.DictReader(csv_input)
        for key in dr:
            vowel_seqs.append(NONVOWELS_REGEX.sub('', key['word']))
    for seq in vowel_seqs:
        bigram_list = bigrams(seq)
        for tup in bigram_list:
            bigram_counts[tup] += 1

    with open(outfile, 'w') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerow(['bigram', 'V1', 'V2', 'count'])
        for key in bigram_counts: # val is a list [wordcount, doc-count]
            writer.writerow([key[0]+key[1], key[0], key[1], bigram_counts[key]])  


#==========================#
# MEDIAL CONSONANT BIGRAMS #
#==========================#

def remove_initial(s):
    seq = list(s)
    for i,c in enumerate(s):
        if c in CONSONANTS:
            seq[i] = ''
        else:
            break
    return ''.join(seq)

def remove_trailing(s):
    rev = ''.join(s)[::-1]
    rev_x = remove_initial(rev)
    if not rev_x:   # can't reverse what doesn't exist 
        return rev_x
    return ''.join(rev_x)[::-1]

def medial_cons_bigrams(infile, outfile):
    clusters = []
    bigram_counts = {key: 0 for key in list((itertools.product(CONSONANTS,CONSONANTS)))}
    with open(infile) as csv_input:
        dr = csv.DictReader(csv_input)
        for row in dr:
            nomargins = remove_trailing(remove_initial(row['word'])) # remove initial and final cons
            filtered = NONCONS_REGEX.sub('', nomargins) # just to make sure I didn't miss anything
            clusters += VOWELS_REGEX.sub(' ', filtered).split()
    for seq in clusters:
        bigram_list = bigrams(seq)
        for tup in bigram_list:
            bigram_counts[tup] += 1
    
    with open(outfile, 'w') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerow(['bigram','C1', 'C2', 'count'])
        for key in bigram_counts: # val is a list [wordcount, doc-count]
            writer.writerow([key[0]+key[1], key[0], key[1], bigram_counts[key]])  


def main():
    infile = sys.argv[1]
    outfile = sys.argv[2]
    medial_cons_bigrams(infile, outfile)

if __name__ == "__main__":
    main()