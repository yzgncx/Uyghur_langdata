#!/usr/bin/python3.4

import sys
import csv, re
from arabic_to_latin import arabic_to_ASCII 


def tokenize(text):
    remove = re.compile(
            r'''(?x) 
            "
            |\-+
            |[0-9]+
            |,+
            |\.+
            |\?+
            |!+
            |:+
            |;+
            |\#
            |@
            |\(
            |\)
            |‹
            |›
            |«
            |»
            |،
            |؟
            ''', re.UNICODE
        )

    tokens = remove.sub(' ', text).split()
    return tokens

def count(tokenized_text):
    wordcount = {}
    for token in tokenized_text:
        if token in wordcount:
            wordcount[token] += 1
        else:
            wordcount[token] = 1
    return wordcount


# Currently removes all words that appear in only one document.
# This is probably really heavy-handed, but it does seem to get rid
# of some noise in the data.
#
def remove_unwanted(wordcounts_dict):
    tmp_copy = dict(wordcounts_dict)
    for key in tmp_copy:
        if tmp_copy[key][1] <= 1:
            del wordcounts_dict[key]
    return

# a bit space-inefficient -- involves making a full copy
# of the dict.  
def normalize_alphabet(wordcounts_dict):
    translate = {}
    for key in wordcounts_dict:
        translate[key] = arabic_to_ASCII(key)
    for old_key, new_key in translate.items():
        wordcounts_dict[new_key] = wordcounts_dict.pop(old_key)
        

# Several sounds are represented as digraphsnormalize_alphabet in the latin orthography
# This causes some problems; some digraphs are indistinguishable from
# consonant clusters.  The arabic script doesn't have this problem.
def output_csv(wordcounts_dict, outfile):  
    with open(outfile, 'w') as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(['word', 'count', 'doc-count'])
        for key in wordcounts_dict: # val is a list [wordcount, doc-count]
            writer.writerow([key, wordcounts_dict[key][0], wordcounts_dict[key][1]])


def main():
    tokenized = []
    wordcounts = []
    textwordcounts = {}
    infile = sys.argv[1]
    outfile = sys.argv[2]

    with open(infile) as csvfile:
        n_texts = 0
        dr = csv.DictReader(csvfile)
        for row in dr:
            tokenized.append(tokenize(row['text']))
            n_texts += 1

        print("total texts:" + str(n_texts))

    for text in tokenized:
        wordcounts.append(count(text))
    for count_dict in wordcounts:
        for key in count_dict:
            if key in textwordcounts:
                textwordcounts[key][0] += count_dict[key]   # increment word count
                textwordcounts[key][1] += 1                 # increase doc count
            else:
                textwordcounts[key] = [1,1]                 # [wordcount=1, documentcount=1]    

    total_tokens = 0
    total_words = 0
    for key in textwordcounts:
        total_tokens += textwordcounts[key][0]
        total_words += 1 #There's a better way to do this, but I don't remember the function.  Sorry future me.
    print("total unfiltered tokens: " + str(total_tokens))
    print("total unique unfiltered words: " + str(total_words))

    remove_unwanted(textwordcounts)
    total_tokens = 0
    total_words = 0
    for key in textwordcounts:
        total_tokens += textwordcounts[key][0]
        total_words += 1 #There's a better way to do this, but I don't remember the function.  Sorry future me.

    print("total tokens post-filter: " + str(total_tokens))
    print("total unique words post-filter: " + str(total_words))


    normalize_alphabet(textwordcounts)
    output_csv(textwordcounts, outfile)

#    for x in textwordcounts: 
#        print(x)
#        print(textwordcounts[x])



if __name__ == "__main__":
    main()