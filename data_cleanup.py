#!/usr/bin/python

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

def remove_unwanted(wordcounts_dict):
    return

# deprecated? leaving this in for the time being in case it becomes useful again.
"""def normalize_alphabet(wordcounts_dict):
    ng = re.compile(r'ng[bptjxdrzsfqkglmnhwvyc]', re.UNICODE) #ng followed by a consonant
    gh = re.compile(r'gh', re.UNICODE)
    ch = re.compile(r'ch', re.UNICODE)
    zh = re.compile(r'zh', re.UNICODE)
    eh = re.compile(r'[éë]', re.UNICODE)
    gs = re.compile(r"'", re.UNICODE)
    for key in wordcounts_dict:
        new_key = key.lower()
        new_key = ng.sub('N', new_key)
        new_key = gh.sub('G', new_key)
        new_key = ch.sub('C', new_key)
        new_key = zh.sub('Z', new_key)
        new_key = eh.sub('E', new_key)
        new_key = gs.sub('P', new_key)
        wordcounts_dict[new_key] = wordcounts_dict.pop(key)
"""

""" a bit space-inefficient -- involves making a full copy
    of the dict.  
"""
def normalize_alphabet(wordcounts_dict):
    tmp = {}
    for key in wordcounts_dict:
        tmp[key] = arabic_to_ASCII(key)
    for old_key, new_key in tmp.items():
        wordcounts_dict[new_key] = wordcounts_dict.pop(old_key)
        
# Several sounds are represented as digraphsnormalize_alphabet in the latin orthography
# This causes some problems; some digraphs are indistinguishable from
# consonant clusters.  The arabic script doesn't have this problem.

def main():
    tokenized = []
    wordcounts = []
    textwordcounts = {}
    infilename = sys.argv[1]
    with open(infilename) as csvfile:
        dr = csv.DictReader(csvfile)
        for row in dr:
            tokenized.append(tokenize(row['title']))
    for text in tokenized:
        wordcounts.append(count(text))
    for count_dict in wordcounts:
        for key in count_dict:
            if key in textwordcounts:
                textwordcounts[key][0] += count_dict[key]   # increment word count
                textwordcounts[key][1] += 1                 # increase doc count
            else:
                textwordcounts[key] = [1,1]                 # [wordcount=1, documentcount=1]    

    remove_unwanted(textwordcounts)
    normalize_alphabet(textwordcounts)

    for x in textwordcounts: 
        print(x)
        print(textwordcounts[x])
#    for word in tokenized:
#        print word
#    for l in wordcounts:
#        print l


if __name__ == "__main__":
    main()