###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                                 errors.py  ##
##                                                                           ##
##  This file should be loaded by most other files and contains all error    ##
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
    if reason == "input" or reason == 1:
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
    
    # REASON 3: UNRECOGNISED CHORD QUALITY
    if reason == "quality" or reason == 3:
        import dicts
        out = """Unrecognised chord quality. Currently supported chord """    \
            + """qualities are: """ + str(list(dicts.qualities.keys()))       \
            + """. These  are case-sensitive. You can also put alterations """\
            + """in parentheses."""
        raise ChordError(out)
        
    # REASON 4 (FERMAT'S ERROR): MARGIN TOO SMALL TO PRINT LINE NUMBER
    if reason == "fermat" or reason == 4:
        out = """In attempting to print a chord, one line number to be """    \
            + """displayed was too long compared to the default margin size"""\
            + """. Ensure ThatChord is not printing chords absurdly high """  \
            + """on the fretboard, and that the margin is defined to be """   \
            + """suitably large (ideally 3 or more)."""
        raise ChordError(out)
    
    # REASON 5: TOO FEW FRETS FOR ANY POSSIBILITIES
    if reason == "frets" or reason == 5:
        out = """The number of frets is too low for one of your """           \
            + """instrument strings to have any valid positions. Try """      \
            + """changing the number of frets, changing the chord, or """     \
            + """allowing more muted strings."""
        raise ChordError(out)
    
    raise ChordError