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

def translator(sentence):
    '''when passed a string, translates string to piglatin'''
    # Checks that the input string is long enough to translate. Then determines
    # whether the word starts with a consonant, consonant cluster or vowel.
    # if the word starts with a vowel, the translator adds 'ay' to the end of
    # the word. If the word starts with a consonant, translator emoves the first
    # letter of the word, and adds it to the end of the word along with 'ay'.
    # if the word starts with a consonant cluster, the consonant cluster is
    # removed from the beginning of the word and appended to the end of the
    # string along with 'ay'

    word_list = sentence.split(' ')
    translated_phrase = ''

    for word in word_list:

        if len(word) < 3:
            translated_phrase = translated_phrase + word + ' '

        else:
            word = word.lower()
            vowels = ['a', 'e', 'i', 'o', 'u', 'y']

            if word[0] in vowels:
                piglatin_translation = word + 'ay '
                translated_phrase = translated_phrase + piglatin_translation

            else:
                if word[1] in vowels:
                    first_letter = word[0]
                    new_string = word[1:]
                    piglatin_translation = new_string + first_letter + 'ay '
                    translated_phrase = translated_phrase + piglatin_translation

                else:
                    cluster = word[:2]
                    new_string = word[2:]
                    piglatin_translation = new_string + cluster + 'ay '
                    translated_phrase = translated_phrase + piglatin_translation

    return translated_phrase

if __name__ == '__main__':
    print(translator(input('Please enter the phrase you would like to translate: ')))
