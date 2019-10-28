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

    def test_present_tense(self):
        v = Verb('bris')
        self.assertEqual(v.present_tense(1),              'brisim')
        self.assertEqual(v.present_tense(2),              'briseann tú')
        self.assertEqual(v.present_tense(3, gender='m'),  'briseann sé')
        self.assertEqual(v.present_tense(3, gender='f'),  'briseann sí')
        self.assertEqual(v.present_tense(1, plural=True), 'brisimid')
        self.assertEqual(v.present_tense(2, plural=True), 'briseann sibh')
        self.assertEqual(v.present_tense(3, plural=True), 'briseann siad')
        v = Verb('fan')
        self.assertEqual(v.present_tense(1),              "fanaim")
        self.assertEqual(v.present_tense(2),              "fanann tú")
        self.assertEqual(v.present_tense(3, gender='m'),  "fanann sé")
        self.assertEqual(v.present_tense(3, gender='f'),  "fanann sí")
        self.assertEqual(v.present_tense(1, plural=True), "fanaimid")
        self.assertEqual(v.present_tense(2, plural=True), "fanann sibh")
        self.assertEqual(v.present_tense(3, plural=True), "fanann siad")
        v = Verb('rith')
        self.assertEqual(v.present_tense(1),              'rithim')
        self.assertEqual(v.present_tense(2),              'ritheann tú')
        self.assertEqual(v.present_tense(3, gender='m'),  'ritheann sé')
        self.assertEqual(v.present_tense(3, gender='f'),  'ritheann sí')
        self.assertEqual(v.present_tense(1, plural=True), 'rithimid')
        self.assertEqual(v.present_tense(2, plural=True), 'ritheann sibh')
        self.assertEqual(v.present_tense(3, plural=True), 'ritheann siad')
        v = Verb('dóigh')
        self.assertEqual(v.present_tense(1),              'dóim')
        self.assertEqual(v.present_tense(2),              'dónn tú')
        self.assertEqual(v.present_tense(3, gender='m'),  'dónn sé')
        self.assertEqual(v.present_tense(3, gender='f'),  'dónn sí')
        self.assertEqual(v.present_tense(1, plural=True), 'dóimid')
        self.assertEqual(v.present_tense(2, plural=True), 'dónn sibh')
        self.assertEqual(v.present_tense(3, plural=True), 'dónn siad')
        v = Verb('léigh')
        self.assertEqual(v.present_tense(1),              'léim')
        self.assertEqual(v.present_tense(2),              'léann tú')
        self.assertEqual(v.present_tense(3, gender='m'),  'léann sé')
        self.assertEqual(v.present_tense(3, gender='f'),  'léann sí')
        self.assertEqual(v.present_tense(1, plural=True), 'léimid')
        self.assertEqual(v.present_tense(2, plural=True), 'léann sibh')
        self.assertEqual(v.present_tense(3, plural=True), 'léann siad')
        v = Verb('suigh')
        self.assertEqual(v.present_tense(1),              'suím')
        self.assertEqual(v.present_tense(2),              'suíonn tú')
        self.assertEqual(v.present_tense(3, gender='m'),  'suíonn sé')
        self.assertEqual(v.present_tense(3, gender='f'),  'suíonn sí')
        self.assertEqual(v.present_tense(1, plural=True), 'suímid')
        self.assertEqual(v.present_tense(2, plural=True), 'suíonn sibh')
        self.assertEqual(v.present_tense(3, plural=True), 'suíonn siad')
        v = Verb('imir')
        self.assertEqual(v.present_tense(1),              "imrím")
        self.assertEqual(v.present_tense(2),              "imríonn tú")
        self.assertEqual(v.present_tense(3, gender='m'),  "imríonn sé")
        self.assertEqual(v.present_tense(3, gender='f'),  "imríonn sí")
        self.assertEqual(v.present_tense(1, plural=True), "imrímid")
        self.assertEqual(v.present_tense(2, plural=True), "imríonn sibh")
        self.assertEqual(v.present_tense(3, plural=True), "imríonn siad")
        v = Verb('sábháil')
        self.assertEqual(v.present_tense(1),              'sábhálaim')
        self.assertEqual(v.present_tense(2),              'sábhálann tú')
        self.assertEqual(v.present_tense(3, gender='m'),  'sábhálann sé')
        self.assertEqual(v.present_tense(3, gender='f'),  'sábhálann sí')
        self.assertEqual(v.present_tense(1, plural=True), 'sábhálaimid')
        self.assertEqual(v.present_tense(2, plural=True), 'sábhálann sibh')
        self.assertEqual(v.present_tense(3, plural=True), 'sábhálann siad')
        v = Verb('ceangail')
        self.assertEqual(v.present_tense(1),              'ceanglaím')
        self.assertEqual(v.present_tense(2),              'ceanglaíonn tú')
        self.assertEqual(v.present_tense(3, gender='m'),  'ceanglaíonn sé')
        self.assertEqual(v.present_tense(3, gender='f'),  'ceanglaíonn sí')
        self.assertEqual(v.present_tense(1, plural=True), 'ceanglaímid')
        self.assertEqual(v.present_tense(2, plural=True), 'ceanglaíonn sibh')
        self.assertEqual(v.present_tense(3, plural=True), 'ceanglaíonn siad')