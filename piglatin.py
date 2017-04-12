# Piglatin game

# Prints game directions to the screen
print('''
    Welcome to the Piglatin game!
    ''')
print('''
    Rules:

    Please enter a word that is three characters or longer.

    For words that begin with consonant sounds, all letters before
    the initial vowel are placed at the end of the word sequence. Then, "ay" is
    added, as in the following examples:

    "pig" = "igpay"
    "Latin" = "Atinlay"
    "banana" = "ananabay"
    "wet" = "etway"
    "too" = "ootay"
    ''')
print('''
    For words that begin with consonant clusters (multiple consonants that
    form one sound), the whole sound is added to the end. For example:

    "cheers" = "eerschay"
    "sheesh" = "eshay"
    "smile" = "ilesmay"
    "thanks" = "anksthay"
    ''')
print('''
    For words that being with vowel sounds, just add "ay" to the end.
    For example:
    "eat" = "eatay"
    "omelet" = "omeletay"
    "are" = "areay"
    "egg" = "eggay"
    ''')



def translator(word):
    '''when passed a string, translates string to piglatin'''

    #make sure the word is long enough to translate
    if len(word) < 3:
        print('please use a longer word')

    #check if the word starts with consonant, consonant cluster or vowel
    else:
        word = word.lower()
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']

        if word[0] in vowels:
            piglatin_translation = word + 'ay'
            print('The piglatin translation for \'{}\' is \'{}\''.format(word, piglatin_translation))
        else:
            if word[1] in vowels:
                first_letter = word[0]
                new_string = word[1:]
                piglatin_translation = new_string + first_letter + 'ay'
                print('The piglatin translation for \'{}\' is \'{}\''.format(word, piglatin_translation))
            else:
                print('word starts with consonant cluster')



translator('Hips')
