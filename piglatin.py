# Piglatin game

# Prints game directions to the screen
print('''
    Welcome to the Piglatin game!
    ''')

print('''
    Rules:

    Please enter one word (no spaces) that is at least three characters.

    For words that begin with consonant sounds, all letters before
    the initial vowel are placed at the end of the word sequence.
    ''')

print('''
    For words that begin with consonant clusters (multiple consonants that
    form one sound), the whole sound is added to the end.
    ''')

print('''
    For words that being with vowel sounds, just add "ay" to the end.
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

        #piglatin translation for vowels
        if word[0] in vowels:
            piglatin_translation = word + 'ay'
            print('The piglatin translation for \'{}\' is \'{}\''.format(word, piglatin_translation))

        #piglatin translation for consonant sounds
        else:
            if word[1] in vowels:
                first_letter = word[0]
                new_string = word[1:]
                piglatin_translation = new_string + first_letter + 'ay'
                print('The piglatin translation for \'{}\' is \'{}\''.format(word, piglatin_translation))

            #piglatin translation for consonant clusters
            else:
                cluster = word[:2]
                new_string = word[2:]
                piglatin_translation = new_string + cluster + 'ay'
                print('The piglatin translation for \'{}\' is \'{}\''.format(word, piglatin_translation))

if __name__ == '__main__':
    translator('ship')
