###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                            MAIN TEST FILE  ##
##                                                                           ##
##  This file contains tests to be run via pytest that check that various    ##
##  subprocesses of ThatChord are running correctly. Some tests check        ##
##  assertions that do not necessarily have to be true for the code to be    ##
##  working: for example, one test ensures that the ukulele ranking          ##
##  system places the [0, 0, 0, 3] chord for C first.                        ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################

# Move out of testing folder (for imports)
import sys
sys.path.append(sys.path[0] + "/..")

# Testing module
import pytest

# Import ThatChord-specific error class
from errors import ChordError

# Import ThatChord functions for testing
import interpret
import find
import settings
import rank

class TestInterpret:

    # GARBAGE INPUTS
    def test_interpret_nonsensicalinputs(self):
        # Tests that nonsensical inputs return errors.
        for garbage in ["Hmaj7",
                        "C#yeet",
                        "Dmin(b0)",
                        "Fbm/H",
                        "WXYZ",
                        "",
                        "G////",
                        "   "
                        ]:
            with pytest.raises(ChordError):
                interpret.interpret(garbage)

    # BASIC CHORDS
    # NB.: order of notes is important, but subject to change from a musical
    # standpoint that I cannot predict. So we just check sets.
    def test_interpret_basicinputs_01(self):
        assert set(interpret.interpret("C")) == {0, 4, 7}
    def test_interpret_basicinputs_02(self):
        assert set(interpret.interpret("Dm")) == {2, 5, 9}
    def test_interpret_basicinputs_03(self):
        assert set(interpret.interpret("F#7")) == {1, 4, 6, 10}
    def test_interpret_basicinputs_04(self):
        assert set(interpret.interpret("B5")) == {6, 11}
    def test_interpret_basicinputs_05(self):
        assert set(interpret.interpret("eb6")) == {0, 3, 7, 10}

    # ALTERATIONS
    def test_interpret_alterations_01(self):
        assert set(interpret.interpret("C7(#5)")) == {0, 4, 8, 10}
    def test_interpret_alterations_02(self):
        assert set(interpret.interpret("C9(#7)")) == {0, 2, 4, 7, 11}
    def test_interpret_alterations_03(self):
        assert set(interpret.interpret("D(##5)")) == {2, 6, 11}
    def test_interpret_alterations_04(self):
        assert set(interpret.interpret("C#(b#bb#b3)")) == {1, 3, 8}
    def test_interpret_alterations_05(self):
        assert set(interpret.interpret("bb(#b5)")) == set(interpret.interpret("bb"))
    def test_interpret_alterations_06(self):
        assert set(interpret.interpret("Gm(#6)")) == {2, 5, 7, 10}
    
    # BASS NOTES
    def test_interpret_bass_01(self):
        assert set(interpret.interpret("Dsus2/C")) == {0, 2, 4, 9}
    def test_interpret_bass_02(self):
        assert interpret.interpret("E7/B")[0] == 11

class TestFind:
    
    # TEST ON SMALL INPUTS
    def test_find_smallinput(self):
        # Only one way of playing Cmaj on uke neck with 3 frets
        assert find.find([0, 4, 7],
                         [7, 0, 4, 9],
                         3,
                         [0, 0, 0, 0]) == [[0, 0, 0, 3]]
    
    # CHECK NO CHORDS ARE PROPOSED WITH FRETS BELOW STRINGSTARTS
    def test_find_stringstarts(self):
        options = find.find([7, 2, 9],
                            [7, 2, 7, 11, 2],
                            15,
                            [5, 0, 0, 0, 0])
        for opt in options:
            assert opt[0] >= 5
    
    # CHECK THERE IS AN ERROR IF NO CHORDS ARE POSSIBLE
    def test_find_nooptions(self):
        with pytest.raises(ChordError):
            find.find([0, 4, 7],
                      [7, 0, 4, 9],
                      2,
                      [0, 0, 0, 0])
    
    # BASIC CHECK HIGH UP NECK
    def test_find_highneck(self):
        assert [10, 9, 8, 8] in find.find(interpret.interpret("F"),
                                          [7, 0, 4, 9],
                                          12,
                                          [0, 0, 0, 0])
    
    # CHECK THAT IF MUTE IS ALLOWED, MUTED CHORDS ARE FOUND
    def test_find_mute_01(self):
        def muteworks():
            options = find.find([0, 4, 7],
                                [4, 9, 2, 7, 11, 4],
                                15,
                                [0, 0, 0, 0, 0, 0],
                                nmute = 2,
                                important = 6
                                )
            for opt in options:
                if opt[0] == -1 and opt[1] == -1:
                    return True
            return False
        assert muteworks()
    
    # CHECK THAT IF MUTE IS NOT ALLOWED, MUTED CHORDS ARE NOT FOUND
    def test_find_mute_02(self):
        def muteworks():
            options = find.find([0, 4, 7],
                                [4, 9, 2, 7, 11, 4],
                                15,
                                [0, 0, 0, 0, 0, 0],
                                nmute = 0,
                                important = 6
                                )
            for opt in options:
                if opt[0] == -1 and opt[1] == -1:
                    return False
            return True
        assert muteworks()
    
    # CHECK THAT ONLY C'S WORKS FOR CMAJ IF ONLY 1 NOTE IS IMPORTANT
    def test_find_smallimportant(self):
        assert [5, 0, 8, 3] in find.find([0, 4, 7],
                                         [7, 0, 4, 9],
                                         12,
                                         [0, 0, 0, 0],
                                         nmute = 0,
                                         important = 1)

class TestRank:
    
    # because we can't define custom settings outside of settings.py, for now
    # this just tests that the default setting (soprano ukulele) produces
    # reasonable results for basic chords with an obvious best choice.
    # TODO change settings so the entries can be overwritten.
    def test_rank_basicuke_01(self):
        # tests that C major is what you would expect.
        options = find.find([0, 4, 7],
                            settings.tuning,
                            settings.nfrets,
                            settings.stringstarts,
                            settings.nmute,
                            settings.important)
        options.sort(key = lambda x : rank.rank(x,
                                                [0, 4, 7],
                                                settings.tuning,
                                                settings.order,
                                                settings.ranks,
                                                settings.stringstarts))
        assert options[0] == [0, 0, 0, 3]
    
    def test_rank_basicuke_02(self):
        # tests that A minor is what you would expect.
        options = find.find([9, 4, 0],
                            settings.tuning,
                            settings.nfrets,
                            settings.stringstarts,
                            settings.nmute,
                            settings.important)
        options.sort(key = lambda x : rank.rank(x,
                                                [9, 4, 0],
                                                settings.tuning,
                                                settings.order,
                                                settings.ranks,
                                                settings.stringstarts))
        assert options[0] == [2, 0, 0, 0]
