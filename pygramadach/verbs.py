from .tools import *


class Verb(object):
    
    def __init__(self, root, conjugation=None):
        
        self.root = root
        self.conjugation = conjugation
        if self.conjugation == None:
            if num_syllables(root) == 1 or root[-3:] in ['áil', 'áin']:
                self.conjugation = 1
            else:
                self.conjugation = 2
        
    def subjunctive(self, plural=False):
        
        irregulars = {
            'bí': 'bígí',
            'faigh': 'faighigí',
            'tabhair': 'tugaigí',
            'tar': 'tagaigí',
        }
        
        if plural == False:
            return self.root
        else:
            if self.root in irregulars:
                return irregulars[self.root]
            elif self.conjugation == 1:
                if self.root[-3:] in ['áil', 'áin']:
                    return self.root[:-3] + 'á' + self.root[-1] + 'aigí'
                elif self.root[-3:] == 'igh':
                    if self.root[-4] in FADA_VOWELS:
                        return self.root[:-3] + 'igí'
                    else:
                        return self.root[:-3] + 'ígí'
                else:
                    if ends_broad(self.root):
                        return self.root + 'aigí'
                    else:
                        return self.root + 'igí'
            elif self.conjugation == 2:
                if self.root[-3:] == 'igh':
                    return self.root[:-3] + 'ígí'
                elif self.root[-2:] in ['il', 'in', 'ir', 'is']:
                    shortened_root = remove_last_diphthong(self.root)
                else:
                    shortened_root = self.root
                if ends_broad(shortened_root):
                    return shortened_root + 'aigí'
                else:
                    return shortened_root + 'igí'

    def past_tense(self, person, gender=None, plural=False):
        past_root = seimhiu(self.root)
        if is_vowel(past_root[0]) or past_root[:2] == 'fh':
            past_root = "d'" + past_root
        if (person, plural) == (1, True):
            if self.conjugation == 1:
                if past_root[-3:] == 'igh':
                    if past_root[-4] in FADA_VOWELS:
                        if is_broad(past_root[-4]):
                            return past_root[:-3] + 'mar'
                        else:
                            return past_root[:-3] + 'amar'
                    else:
                        return past_root[:-3] + 'íomar'
                elif past_root[-3:] == 'áil':
                    return past_root[:-2] + 'lamar'
                else:
                    if ends_broad(past_root):
                        return past_root + 'amar'
                    else:
                        return past_root + 'eamar'
            elif self.conjugation == 2:
                if past_root[-3:] == 'igh':
                    return past_root[-3:] + 'íomar'
                elif past_root[-2:] in ['il', 'in', 'ir', 'is']:
                    past_root = remove_last_diphthong(past_root)
                if ends_broad(past_root):
                    return past_root + 'aíomar'
                else:
                    return past_root + 'íomar'
        else:
            return past_root + ' ' + get_personal_pronoun(person, gender, plural)