from unittest import TestCase
from all_prefixes import all_prefixes


class TestAllPrefixes(TestCase):
    def test_all_prefixes(self):
        self.assertEquals({'w', 'wo', 'wor', 'word'}, all_prefixes('word'), "fail")
        self.assertEquals({'UkrainCtholc', 'Uk', 'UkrainCth', 'UkrainCtho',
                           'UkrainCthol', 'UkrainCtholcves', 'Ukrai', 'U',
                           'Ukra', 'UkrainCt', 'UkrainC', 'UkrainCtholcv',
                           'UkrainCtholcvesy', 'Ukr', 'Ukrain', 'UkrainCtholcve'},
                          all_prefixes('UkrainianCatholicUniversity'), "fail")
        self.assertEquals(set(), all_prefixes(''), "fail")
        self.assertEquals({'alw', 'alwys', 'alwys ', 'a', 'alwys n',
                           'al', 'alwy', 'alwys nf'}, all_prefixes('always wanna fly'), "fail")
