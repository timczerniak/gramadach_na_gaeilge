VOWELS = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']
BROAD_VOWELS = ['a', 'á', 'o', 'ó', 'u', 'ú']
FADA_VOWELS = ['á', 'é', 'í', 'ó', 'ú']
PERSONAL_PRONOUNS = {
    (1, None, False): 'mé',
    (2, None, False): 'tú',
    (3, 'm',  False): 'sé',
    (3, 'f',  False): 'sí',
    (1, None, True):  'sinn',
    (2, None, True):  'sibh',
    (3, None, True):  'siad',
}


def is_vowel(letter):
    return letter in VOWELS


def is_broad(letter):
    return letter in BROAD_VOWELS


def ends_broad(word):
    x = 1
    while 1:
        letter = word[-x]
        if is_vowel(letter):
            return is_broad(letter)
        x += 1


def remove_last_diphthong(word):
    x = 1
    ending = ""
    while 1:
        letter = word[-x]
        if is_vowel(letter):
            break
        else:
            ending += letter
        x += 1
    x += 1
    while 1:
        letter = word[-x]
        if not is_vowel(letter):
            break
        x += 1
    return word[:-x+1] + ending[::-1]


def num_syllables(focal):
    syllable_count = 0
    in_syllable = False
    for letter in focal:
        if is_vowel(letter) and not in_syllable:
            in_syllable = True
            syllable_count += 1
        if not is_vowel(letter) and in_syllable:
            in_syllable = False
    return syllable_count


def get_personal_pronoun(person, gender, plural):
    return PERSONAL_PRONOUNS[(person, gender, plural)]


def seimhiu(word):
    if word[0] in ['b', 'c', 'd', 'f', 'g', 'm', 'p', 's', 't']:
        return word[0] + 'h' + word[1:]
    else:
        return word