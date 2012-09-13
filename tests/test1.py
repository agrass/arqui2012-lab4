# -*- coding: UTF-8 -*-

import sys
# para Python 2.6 o inferior, utilizamos unittest2
if sys.hexversion < 0x2070000:
    import unittest2 as unittest
else:
    import unittest

import main # el módulo a probar

class TestPolisher(unittest.TestCase):

    def test_fail(self):
        self.assertEqual(True, True)