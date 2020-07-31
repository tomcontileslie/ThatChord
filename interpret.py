###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                              interpret.py  ##
##                                                                           ##
##  This file takes an input string in the form of a chord, e.g. "Asus4" or  ##
##  "Cmaj7(b5)", and converts it to a list of numbers representing notes.    ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################


# import error messages
from errors import err

# we'll need reg exps for this bit
import re

# we'll also need dictionaries from other files
import dicts

# Define regexp for structure of input string
structure =   r"([a-gA-G][b#]?)"       \
            + r"(\d*[ac-zA-Z\+]*\d*)" \
            + r"(\(([b#]+\d+)+\))?"    \
            + r"(/([a-gA-G][b#]?))?$"


# Define handly helper functions
def pm(s):
    """
    pm stands for plus/minus. This returns -1 for "b", +1 for "#", and 0 for
    anything else.
    """
    if s == "b":
        return - 1
    if s == "#":
        return + 1
    return 0

def hv(n):
    """
    Heaviside-style function used for alterations depending on whether the
    notes are being sharpened or flattened.
    """
    if n < 0:
        return 1
    if n > 0:
        return 0

# our main function
def interpret(ss):
    """
    takes a string and returns a list of numbers. 0 = C; 1 = C#; ...; 11 = B.
    """
    
    # start by removing extra symbols
    s = ss.translate({ord(c) : None for c in " ,._;:|><*"})
    
    # create copies of the dicts to avoid changes bleeding over
    notes = dict(dicts.notes)
    alterations = dict(dicts.alterations)
    qualities = dict(dicts.qualities)
    
    # match to regexp
    m = re.match(structure, s)
    if not m:
        err(1)
    W, X, Y, Z = m.group(1), m.group(2), m.group(3), m.group(6)
    
    try:
        out = qualities[X].copy()
    except KeyError:
        err(1)
    
    # deal with any alterations here.
    # TODO is this the best way to deal with alterations? Do we need to take
    # more context into accout, e.g. major/minor?
    if Y:
        Y = Y[1 : -1] # remove parentheses from match
        while Y != "":
            m = re.match(r"([b#]+)(\d+)", Y) # first remaining alteration
            
            # extract important information from alteration
            alt = sum([pm(i) for i in m.group(1)]) # so bb becomes -2
            num = int(m.group(2))
            try:
                pair = alterations[num]
            except KeyError:
                err(2)
            
            # establish what notes need to be added and removed
            if alt == 0:
                # someone entered "b#"... why?? Do nothing in this case.
                pass
            else:
                note_rem = pair[hv(alt)]          # remove this note
                note_add = (note_rem + alt) % 12  # add this note
                if pair[0] in out:
                    out.remove(pair[0])
                if pair[1] in out:
                    out.remove(pair[1])
                if not note_add in out:
                    out.append(note_add)
                # TODO definitely if alterations are >= 2 in either direction,
                # the strategy for removing notes should be different
            Y = Y[m.end():] # remove this alteration
    
    # Scale everything to the correct key
    root = notes[W[0]] + pm(W[1 : 2])
    out = [(root + n) % 12 for n in out]
    
    if Z:
        # a bass note was supplied
        bass = (notes[Z[0]] + pm(Z[1 : 2])) % 12
        if bass in out:
            # move bass to front
            out.remove(bass)
        # in either case, bass note is at front
        out = [bass] + out
            
    # TODO test that alterations work
    
    return out