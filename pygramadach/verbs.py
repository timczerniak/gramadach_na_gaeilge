from .tools import *


class Verb(object):
    
    def __init__(self, root, conjugation=None):
        
        self.root = root
        self.conjugation = conjugation
        if self.conjugation == None:
            if num_syllables(root) == 1 or \
                    root.endswith('áil') or root.endswith('áin'):
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
                if self.root.endswith('áil') or self.root.endswith('áin'):
                    # e.g. marcáil -> marcálaigí, taispeáin -> taispeánaigí
                    return self.root[:-3] + 'á' + self.root[-1] + 'aigí'
                elif self.root.endswith('igh'):
                    if self.root[-4] in FADA_VOWELS:
                        # e.g. dóigh -> dóigí
                        return self.root[:-3] + 'igí'
                    else:
                        # e.g. suigh -> suígí
                        return self.root[:-3] + 'ígí'
                else:
                    # all other cases
                    if ends_broad(self.root):
                        return self.root + 'aigí'
                    else:
                        return self.root + 'igí'
            elif self.conjugation == 2:
                if self.root.endswith('igh'):
                    # e.g. ceannaigh -> ceannaígí
                    return self.root[:-3] + 'ígí'
                if self.root.endswith('il') or \
                        self.root.endswith('in') or \
                        self.root.endswith('ir') or \
                        self.root.endswith('is'):
                    # e.g. ceangail -> ceanglaigí
                    shortened_root = remove_last_diphthong(self.root)
                else:
                    shortened_root = self.root
                # most cases
                if ends_broad(shortened_root):
                    return shortened_root + 'aigí'
                else:
                    return shortened_root + 'igí'

    def past_tense(self, person, gender=None, plural=False):
        past_root = seimhiu(self.root)
        
        if is_vowel(past_root[0]) or past_root.startswith('fh'):
            past_root = "d'" + past_root

        if (person, plural) == (1, True):
            # first person plural 'we'
            if self.conjugation == 1:
                if past_root.endswith('igh'):
                    if past_root[-4] in FADA_VOWELS:
                        if is_broad(past_root[-4]):
                            # e.g. dóigh -> dhómar
                            return past_root[:-3] + 'mar'
                        else:
                            # e.g. léigh -> léamar
                            return past_root[:-3] + 'amar'
                    else:
                        # e.g. suigh -> suíomar
                        return past_root[:-3] + 'íomar'
                if past_root.endswith('áil'):
                    # e.g. marcáil -> mharcálamar
                    return past_root[:-2] + 'lamar'
                # all other cases
                if ends_broad(past_root):
                    return past_root + 'amar'
                else:
                    return past_root + 'eamar'
            elif self.conjugation == 2:
                if past_root[-3:] == 'igh':
                    # e.g. ceannaigh -> cheannaíomar
                    return past_root[-3:] + 'íomar'
                if past_root.endswith('il') or \
                        past_root.endswith('in') or \
                        past_root.endswith('ir') or \
                        past_root.endswith('is'):
                    # e.g. ceangail -> cheanglaíomar
                    past_root = remove_last_diphthong(past_root)
                # most cases
                if ends_broad(past_root):
                    return past_root + 'aíomar'
                else:
                    return past_root + 'íomar'
        else:
            # not first person plural
            return past_root + ' ' + get_personal_pronoun(person, gender, plural)
    
    def present_tense(self, person, gender=None, plural=False):
        # first person singular, second person singular
        fps, sps = None, None
        
        if self.conjugation == 1:
            if self.root.endswith('igh'):
                if self.root[-4] in FADA_VOWELS:
                    if is_broad(self.root[-4]):
                        # e.g. dóigh -> dóim, dónn
                        fps, sps = self.root[:-3] + 'im', self.root[:-3] + 'nn'
                    else:
                        # e.g. léigh -> léim, léann
                        fps, sps = self.root[:-3] + 'im', self.root[:-3] + 'ann'
                else:
                    # e.g. suigh -> suím, suíonn
                    fps, sps = self.root[:-3] + 'ím', self.root[:-3] + 'íonn'
            elif self.root.endswith('áil'):
                # e.g. marcáil -> mharcálaim, marcálann
                fps, sps = self.root[:-2] + 'laim', self.root[:-2] + 'lann'
            # all other cases
            elif ends_broad(self.root):
                fps, sps = self.root + 'aim', self.root + 'ann'
            else:
                fps, sps = self.root + 'im', self.root + 'eann'

        elif self.conjugation == 2:
            if self.root[-3:] == 'igh':
                # e.g. ceannaigh -> ceannaím, ceannaíonn
                fps, sps = self.root[-3:] + 'ím', self.root[-3:] + 'íonn'
            elif self.root.endswith('il') or \
                    self.root.endswith('in') or \
                    self.root.endswith('ir') or \
                    self.root.endswith('is'):
                # e.g. ceangail -> ceanglaím, ceanglaíonn
                present_root = remove_last_diphthong(self.root)
                if ends_broad(present_root):
                    fps, sps = present_root + 'aím', present_root + 'aíonn'
                else:
                    fps, sps = present_root + 'ím', present_root + 'íonn'
            # most cases
            elif ends_broad(self.root):
                fps, sps = self.root + 'aím', self.root + 'aíonn'
            else:
                fps, sps = self.root + 'ím', self.root + 'íonn'
        
        if (person, plural) == (1, False):
            return fps
        elif (person, plural) == (1, True):
            return fps + 'id'
        else:
            return sps + ' ' + get_personal_pronoun(person, gender, plural)