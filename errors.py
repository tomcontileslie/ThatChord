###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                                 errors.py  ##
##                                                                           ##
##  This file should be loaded by all other files and contains all error     ##
##  messages that can be returned by various files.                          ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################

class ChordError(Exception):
    pass

def err(reason):
    
    # REASON 1: INVALID INPUT
    if reason == "chord" or reason == 1:
        out = """Invalid chord structure: try a chord of the form """         \
            + """WXYZ", where:\n- W is a letter A-G possibly followed """     \
            + """by "b"or "#";\n- (optional) X is a chord quality, e.g. """   \
            + """"m", "add9", "dim7", ...\n- (optional) Y is a set of """     \
            + """altered notes in parentheses, e.g. "(b7)" or "(#7b13)";\n""" \
            + """- (optional) Z is a bass note, e.g. "/D#"."""
        raise ChordError(out)
    
    # REASON 2: INVALID ALTERATION NUMBER
    if reason == "alteration" or reason == 2:
        out = """Invalid alteration: you can alter the numbers 1, 2, 3, 4, """\
            + """5, 6, 7, 9, 11, 13 only."""
        raise ChordError(out)
    
    raise ChordError