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
        
    # REASON 6: NO CHORDS FOUND
    if reason == "nosols" or reason == 6:
        out = """There are no ways of playing the requested chord on this """ \
            + """instrument, though your chord was correctly understood. """  \
            + """Try increasing the number of frets or reducing the number """\
            + """of important notes."""
        raise ChordError(out)
    
    # REASON 7: INVALID INPUT TYPE
    if reason == "input type" or reason == 7:
        out = """Invalid input type: in the settings file, please set the """ \
            + """variable input_type to be DIRECT, TERMINAL or CONSOLE."""
        raise ChordError(out)
    
    # REASON 8: INVALID OUTPUT FORMAT
    if reason == "output format" or reason == 8:
        out = """Invalid output format: in the settings file, please set """  \
            + """the variable output_format to be TEXT or PNG."""
        raise ChordError(out)
    
    # REASON 9: INVALID OUTPUT METHOD
    if reason == "output method" or reason == 9:
        out = """Invalid output method: in the settings file, please set """  \
            + """the variable output_method to be PRINT, SPLASH or NONE."""
        raise ChordError(out)
    
    # REASON 10: INVALID SAVE METHOD
    if reason == "save method" or reason == 10:
        out = """Invalid save method: in the settings file, please set the """\
            + """variable save_method to be SINGLE, LIBRARY or NONE."""
        raise ChordError(out)
    
    # REASON 11: INCOMPATIBLE OUTPUT SETTINGS
    if reason == "incompatible output" or reason == 11:
        out = """You have chosen incompatible values of output_format and """ \
            + """output_method. See settings.py to correct this."""
        raise ChordError(out)
    
    raise ChordError(str(reason))
