#!/usr/bin/python3.4

# arabic digraphs
MAP_1a = {
    'ئې' : 'é',
    'ئى' : 'i',
    'ئۆ' : 'ö',
    'ئۈ' : 'ü',
    'ئو' : 'o',
    'ئۇ' : 'u',
    'ئا' : 'a',
    'ئە' : 'e'
}

MAP_1b = {
    'ب' : 'b',
    'پ' : 'p',
    'ت' : 't',
    'ج' : 'j',
    'چ' : 'ch',
    'خ' : 'x',
    'د' : 'd',
    'ر' : 'r',
    'ز' : 'z',
    'س' : 's',
    'ش' : 'sh',
    'غ' : 'gh',
    'ف' : 'f',
    'ق' : 'q',
    'ك' : 'k',
    'گ' :'g',
    'ڭ' : 'ng',
    'ل' : 'l',
    'م' : 'm',
    'ن' : 'n',
    'ھ' : 'h',
    'و' : 'o',
    'ۆ' : 'ö',
    'ا' : 'a',
    'ۇ' : 'u',
    'ۈ' : 'ü',
    'ې' : 'é',
    'ى' : 'i',
    'ە' : 'e',
    'ۋ' : 'w',
    'ي' : 'y'
}



# Some sounds in the Uyghur Latin script are represented as digraphs.
# As a result, there are ambiguities between certain character sequences.
# MAP_1 produces this ambiguous form, with digraphs and non-ascii chars.
# MAP_2, below, produces an unambiguous Latinization of the Uyghur Arabic
# script.  In addition to the removal of dirgaphs, all non-ascii symbols
# are removed.   

# arabic digraphs
MAP_2a = {
    'ئى' : 'i',
    'ئې' : 'I',
    'ئو' : 'o', 
    'ئۆ' : 'O', # vowel /ö/
    'ئۈ' : 'y', # vowel /y/
    'ئۇ' : 'u',
    'ئا' : 'a',
    'ئە' : 'e'
}

MAP_2b = {
    'ب' : 'b',
    'پ' : 'p',
    'ت' : 't',
    'ج' : 'J', # voiced alveo-palatal affricate
    'چ' : 'C', # unvoiced alveo-palatal affricate
    'خ' : 'x',
    'د' : 'd',
    'ر' : 'r',
    'ز' : 'z',
    'س' : 's',
    'ش' : 'S', # alveo-palatal fricative
    'غ' : 'G', # uvular stop
    'ف' : 'f',
    'ق' : 'q',
    'ك' : 'k',
    'گ' :'g',
    'ڭ' : 'N', # velar nasal
    'ل' : 'l',
    'م' : 'm',
    'ن' : 'n',
    'ھ' : 'h', 
    'و' : 'o',
    'ۆ' : 'O', # front mid round vowel
    'ا' : 'a',
    'ۇ' : 'u',
    'ۈ' : 'U', # front high round vowel
    'ې' : 'I', # bar-i? 
    'ى' : 'i',
    'ە' : 'e',
    'ۋ' : 'w',
    'ي' : 'j' # glide /j/
    }


# works over strings for now.  might extend to files (TODO)
def arabic_to_ULY(s):
    output = s
    for key in MAP_1a:
        output = output.replace(key, MAP_1a[key])
    for key in MAP_1b:
        output = output.replace(key, MAP_1b[key])
    return output

# works over strings for now.  might extend to files (TODO)
def arabic_to_ASCII(s):
    output = s
    for key in MAP_2a:
        output = output.replace(key, MAP_2a[key])
    for key in MAP_2b:
        output = output.replace(key, MAP_2b[key])
    return output

