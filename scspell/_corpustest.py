#!/usr/bin/env python

"""Unit tests for _corpus.py"""

import unittest

import _corpus


class ExactMatchCorpusTestCase(unittest.TestCase):
    def setUp(self):
        self.emc_empty = _corpus.ExactMatchCorpus(_corpus.DICT_TYPE_NATURAL,
                                                  '', [])

    def testEmptyEMC(self):
        emc = self.emc_empty
        assert emc.match("applesauce") is False
        assert emc.is_dirty() is False

        emc.add("applesauce")
        assert emc.is_dirty() is True
        assert emc.match("apple") is False
        assert emc.match("applesauce") is True
        assert emc.match("applesauces") is False


class PrefixMatchCorpusTestCase(unittest.TestCase):
    def setUp(self):
        self.pmc_empty = _corpus.PrefixMatchCorpus(_corpus.DICT_TYPE_NATURAL,
                                                   '', [])

    def testEmptyPMC(self):
        pmc = self.pmc_empty
        assert pmc.match("applesauce") is False
        assert pmc.is_dirty() is False

        pmc.add("applesauce")
        assert pmc.is_dirty() is True
        assert pmc.match("apple") is True
        assert pmc.match("applesauce") is True
        assert pmc.match("applesauces") is False


if __name__ == "__main__":
    unittest.main()
