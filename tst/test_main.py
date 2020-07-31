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

class TestInterpret:

    # GARBAGE INPUTS
    def test_interpret_nonsensicalinputs(self):
        # Tests that nonsensical inputs return errors.
        for garbage in ["Hmaj7", "C#yeet", "Dmin(b0)", "Fbm/H", "WXYZ"]:
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
        assert set(interpret.interpret(""))

    # CHECK NO DUPLICATE NOTES IN ANY CHORD