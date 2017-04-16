# Piglatin translator
# translates english to Piglatin

print('''
    Welcome to the Piglatin game!
    ''')

print('''
    Rules:

    Please enter the phrase you would like to translate, without punctuation

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
    # Starts by splitting the string into a list of strings
    # Checks that each string is long enough to translate. If not, adds the un-
    # translated string to the translated_phrases string.
    # If the word is three characters or longer, translator determines
    # whether the word starts with a consonant, consonant cluster or vowel.
    # If the word starts with a vowel, call volwel translate.
    # If the word starts with a consonant, call consonant_translate
    # If the word starts with a consonant cluster, call cluster_translate.

    word_list = sentence.split(' ')
    translated_phrase = ''

    for word in word_list:

        if len(word) < 3:
            translated_phrase = translated_phrase + word + ' '

        else:
            word = word.lower()
            vowels = ['a', 'e', 'i', 'o', 'u', 'y']

            if word[0] in vowels:
                piglatin_translation = vowel_translate(word)
                translated_phrase = translated_phrase + piglatin_translation

            else:
                if word[1] in vowels:
                    piglatin_translation = consonant_translate(word)
                    translated_phrase = translated_phrase + piglatin_translation

                else:
                    piglatin_translation = cluster_translate(word)
                    translated_phrase = translated_phrase + piglatin_translation

    return translated_phrase


def vowel_translate(word):
    return word + 'ay '


def consonant_translate(word):
    first_letter = word[0]
    new_string = word[1:]
    return new_string + first_letter + 'ay '


def cluster_translate(word):
    cluster = word[:2]
    new_string = word[2:]
    return new_string + cluster + 'ay '


if __name__ == '__main__':
    print(translator(input('Please enter the phrase you would like to translate: ')))
