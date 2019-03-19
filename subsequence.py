#!/usr/bin/python3.4
import sys, csv, re

#===========================#
# Consonant and Vowel lists #
#===========================#
CONSONANTS = ['p','b','t','d','C','J','k','g','q','G','P','m','n','N','f','s','z','S','Z','x','h','r','l','j','w']
VOWELS = ['i','I','o','O','u','y','a','e']


CONS_REGEX = re.compile('['+''.join(CONSONANTS)+']')
VOWELS_REGEX = re.compile('['+''.join(VOWELS)+']')
NONVOWELS_REGEX = re.compile('[^'+(''.join(VOWELS))+']')

def bigrams(s):
#    print(list(zip(*(s[i:] for i in range(2)))))
    return(list(zip(*(s[i:] for i in range(2)))))

# Vowel bigrams
# Hopefully written to be extensible to other sequence lengths if I find it compelling
def vowel_bigrams(infile, outfile):
    vowel_seqs = []
    bigram_counts = {}
    with open(infile) as csv_input:
        dr = csv.DictReader(csv_input)
        for key in dr:
            vowel_seqs.append(NONVOWELS_REGEX.sub('', key['word']))
    for seq in vowel_seqs:
        bigram_list = bigrams(seq)
        for tup in bigram_list:
            if tup in bigram_counts:
                bigram_counts[tup] += 1
            else:
                bigram_counts[tup] = 1

    with open(outfile, 'w') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerow(['V1', 'V2', 'count'])
        for key in bigram_counts: # val is a list [wordcount, doc-count]
            writer.writerow([key[0], key[1], bigram_counts[key]])


#    print(vowel_seqs)

def main():
    infile = sys.argv[1]
    outfile = sys.argv[2]
    vowel_bigrams(infile, outfile)

if __name__ == "__main__":
    main()