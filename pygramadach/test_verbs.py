import unittest

from .verbs import Verb


class VerbTest(unittest.TestCase):
    
    def test_detect_conjugation(self):
        cj1 = ['marcáil', 'taispeáin', 'dóigh', 'léigh', 'nigh', 'suigh',
              'bris', 'tóg']
        cj2 = ['ceannaigh', 'éirigh', 'ceangail', 'imir', 'inis']
        for verb in cj1:
            v = Verb(verb)
            self.assertEqual(v.conjugation, 1)
        for verb in cj2:
            v = Verb(verb)
            self.assertEqual(v.conjugation, 2)
    
    def test_subjunctive(self):
        cases = {
            'beir': 'beirigí',
            'bí': 'bígí',
            'déan': 'déanaigí',
            'faigh': 'faighigí',
            'feic': 'feicigí',
            'ith': 'ithigí',
            'tar': 'tagaigí',
            'téigh': 'téigí',
            'marcáil': 'marcálaigí',
            'taispeáin': 'taispeánaigí',
            'dóigh': 'dóigí',
            'léigh': 'léigí',
            'nigh': 'nígí',
            'suigh': 'suígí',
            'bris': 'brisigí',
            'tóg': 'tógaigí',
            'abair': 'abraigí',
            'tabhair': 'tugaigí',
            'ceannaigh': 'ceannaígí',
            'éirigh': 'éirígí',
            'ceangail': 'ceanglaigí',
            'imir': 'imrigí',
            'inis': 'insigí',
        }
        for verb, sbj_pl in cases.items():
            v = Verb(verb)
            self.assertEqual(v.root, verb)
            self.assertEqual(v.subjunctive(plural=False), verb)
            self.assertEqual(v.subjunctive(plural=True), sbj_pl)
    
    def test_past_tense(self):
        v = Verb('bris')
        self.assertEqual(v.past_tense(1),              'bhris mé')
        self.assertEqual(v.past_tense(2),              'bhris tú')
        self.assertEqual(v.past_tense(3, gender='m'),  'bhris sé')
        self.assertEqual(v.past_tense(3, gender='f'),  'bhris sí')
        self.assertEqual(v.past_tense(1, plural=True), 'bhriseamar')
        self.assertEqual(v.past_tense(2, plural=True), 'bhris sibh')
        self.assertEqual(v.past_tense(3, plural=True), 'bhris siad')
        v = Verb('fan')
        self.assertEqual(v.past_tense(1),              "d'fhan mé")
        self.assertEqual(v.past_tense(2),              "d'fhan tú")
        self.assertEqual(v.past_tense(3, gender='m'),  "d'fhan sé")
        self.assertEqual(v.past_tense(3, gender='f'),  "d'fhan sí")
        self.assertEqual(v.past_tense(1, plural=True), "d'fhanamar")
        self.assertEqual(v.past_tense(2, plural=True), "d'fhan sibh")
        self.assertEqual(v.past_tense(3, plural=True), "d'fhan siad")
        v = Verb('rith')
        self.assertEqual(v.past_tense(1),              'rith mé')
        self.assertEqual(v.past_tense(2),              'rith tú')
        self.assertEqual(v.past_tense(3, gender='m'),  'rith sé')
        self.assertEqual(v.past_tense(3, gender='f'),  'rith sí')
        self.assertEqual(v.past_tense(1, plural=True), 'ritheamar')
        self.assertEqual(v.past_tense(2, plural=True), 'rith sibh')
        self.assertEqual(v.past_tense(3, plural=True), 'rith siad')
        v = Verb('dóigh')
        self.assertEqual(v.past_tense(1),              'dhóigh mé')
        self.assertEqual(v.past_tense(2),              'dhóigh tú')
        self.assertEqual(v.past_tense(3, gender='m'),  'dhóigh sé')
        self.assertEqual(v.past_tense(3, gender='f'),  'dhóigh sí')
        self.assertEqual(v.past_tense(1, plural=True), 'dhómar')
        self.assertEqual(v.past_tense(2, plural=True), 'dhóigh sibh')
        self.assertEqual(v.past_tense(3, plural=True), 'dhóigh siad')
        v = Verb('léigh')
        self.assertEqual(v.past_tense(1),              'léigh mé')
        self.assertEqual(v.past_tense(2),              'léigh tú')
        self.assertEqual(v.past_tense(3, gender='m'),  'léigh sé')
        self.assertEqual(v.past_tense(3, gender='f'),  'léigh sí')
        self.assertEqual(v.past_tense(1, plural=True), 'léamar')
        self.assertEqual(v.past_tense(2, plural=True), 'léigh sibh')
        self.assertEqual(v.past_tense(3, plural=True), 'léigh siad')
        v = Verb('suigh')
        self.assertEqual(v.past_tense(1),              'shuigh mé')
        self.assertEqual(v.past_tense(2),              'shuigh tú')
        self.assertEqual(v.past_tense(3, gender='m'),  'shuigh sé')
        self.assertEqual(v.past_tense(3, gender='f'),  'shuigh sí')
        self.assertEqual(v.past_tense(1, plural=True), 'shuíomar')
        self.assertEqual(v.past_tense(2, plural=True), 'shuigh sibh')
        self.assertEqual(v.past_tense(3, plural=True), 'shuigh siad')
        v = Verb('imir')
        self.assertEqual(v.past_tense(1),              "d'imir mé")
        self.assertEqual(v.past_tense(2),              "d'imir tú")
        self.assertEqual(v.past_tense(3, gender='m'),  "d'imir sé")
        self.assertEqual(v.past_tense(3, gender='f'),  "d'imir sí")
        self.assertEqual(v.past_tense(1, plural=True), "d'imríomar")
        self.assertEqual(v.past_tense(2, plural=True), "d'imir sibh")
        self.assertEqual(v.past_tense(3, plural=True), "d'imir siad")
        v = Verb('sábháil')
        self.assertEqual(v.past_tense(1),              'shábháil mé')
        self.assertEqual(v.past_tense(2),              'shábháil tú')
        self.assertEqual(v.past_tense(3, gender='m'),  'shábháil sé')
        self.assertEqual(v.past_tense(3, gender='f'),  'shábháil sí')
        self.assertEqual(v.past_tense(1, plural=True), 'shábhálamar')
        self.assertEqual(v.past_tense(2, plural=True), 'shábháil sibh')
        self.assertEqual(v.past_tense(3, plural=True), 'shábháil siad')
        v = Verb('ceangail')
        self.assertEqual(v.past_tense(1),              'cheangail mé')
        self.assertEqual(v.past_tense(2),              'cheangail tú')
        self.assertEqual(v.past_tense(3, gender='m'),  'cheangail sé')
        self.assertEqual(v.past_tense(3, gender='f'),  'cheangail sí')
        self.assertEqual(v.past_tense(1, plural=True), 'cheanglaíomar')
        self.assertEqual(v.past_tense(2, plural=True), 'cheangail sibh')
        self.assertEqual(v.past_tense(3, plural=True), 'cheangail siad')