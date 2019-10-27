import unittest

from .tools import (is_vowel, is_broad, ends_broad, remove_last_diphthong,
                    num_syllables, seimhiu)


class VerbTest(unittest.TestCase):
    
    def test_is_vowel(self):
        self.assertTrue(is_vowel('a'))
        self.assertTrue(is_vowel('e'))
        self.assertTrue(is_vowel('i'))
        self.assertTrue(is_vowel('o'))
        self.assertTrue(is_vowel('u'))
        self.assertTrue(is_vowel('á'))
        self.assertTrue(is_vowel('é'))
        self.assertTrue(is_vowel('í'))
        self.assertTrue(is_vowel('ó'))
        self.assertTrue(is_vowel('ú'))
        self.assertFalse(is_vowel('b'))
        self.assertFalse(is_vowel('c'))
        self.assertFalse(is_vowel('d'))
        self.assertFalse(is_vowel('f'))
        self.assertFalse(is_vowel('g'))
        self.assertFalse(is_vowel('h'))
        self.assertFalse(is_vowel('k'))

    def test_is_broad(self):
        self.assertTrue(is_broad('a'))
        self.assertTrue(is_broad('o'))
        self.assertTrue(is_broad('u'))
        self.assertTrue(is_broad('á'))
        self.assertTrue(is_broad('ó'))
        self.assertTrue(is_broad('ú'))
        self.assertFalse(is_broad('e'))
        self.assertFalse(is_broad('i'))
        self.assertFalse(is_broad('é'))
        self.assertFalse(is_broad('í'))

    def test_ends_broad(self):
        self.assertTrue(ends_broad('tóg'))
        self.assertTrue(ends_broad('déan'))
        self.assertTrue(ends_broad('tar'))
        self.assertFalse(ends_broad('dóigh'))
        self.assertFalse(ends_broad('imir'))
        self.assertFalse(ends_broad('ceangail'))
    
    def test_remove_last_diphthong(self):
        self.assertEqual(remove_last_diphthong('ceangail'), 'ceangl')
        self.assertEqual(remove_last_diphthong('imir'), 'imr')
        self.assertEqual(remove_last_diphthong('inis'), 'ins')
        
    def test_num_syllables(self):
        self.assertEqual(num_syllables('dóigh'), 1)
        self.assertEqual(num_syllables('imir'), 2)
        self.assertEqual(num_syllables('ceangail'), 2)
        self.assertEqual(num_syllables('ceannaigh'), 2)
        self.assertEqual(num_syllables('íoslódáil'), 3)

    def test_seimhiu(self):
        self.assertEqual(seimhiu('bris'), 'bhris')
        self.assertEqual(seimhiu('máthair'), 'mháthair')
        self.assertEqual(seimhiu('saol'), 'shaol')
        self.assertEqual(seimhiu('cur'), 'chur')
        self.assertEqual(seimhiu('pléigh'), 'phléigh')
        self.assertEqual(seimhiu('tuig'), 'thuig')
        self.assertEqual(seimhiu('labhair'), 'labhair')
        self.assertEqual(seimhiu('rith'), 'rith')
        self.assertEqual(seimhiu('imir'), 'imir')
        self.assertEqual(seimhiu('arán'), 'arán')