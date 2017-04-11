# Piglatin game

# Prints game directions to the screen
print('''
    Welcome to the Piglatin game!
    ''')
print('''
    Rules:
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
