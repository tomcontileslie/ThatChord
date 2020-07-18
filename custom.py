###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                                 custom.py  ##
##                                                                           ##
##  Interprets custom requests by the user. Separators can be anything that  ##
##  is not a letter or number. Notes get interpreted either as numbers or    ##
##  letters.                                                                 ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################

import re
from errors import err
import dicts

# define the structure: separator followed by note
structure = r"[^A-Ga-gb#0-9]*((\d)(\d)?|[A-Ga-g][b#]?)"

# Define a handly helper function
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

def interpret(request):
    # make a copy of request which we chop notes off
    rc = request
    # initialise empty request. We will fill this note by note
    out = []
    
    m = re.match(structure, rc)
    while m:
        note = m.group(1) # extract note part of match
        # now check whether it was entered as number or letter
        try:
            # in this case it was entered as a number, trust the user and
            # convert to integer
            out.append(int(note))
        except ValueError:
            # then entered as a note, use translation dicts and pm function
            # to turn into a number
            out.append(dicts.notes[note[0]] + pm(note[1:]))
        # chop matched bit off rc, and the loop will start again if there are
        # more notes
        rc = rc[m.span()[1]:]
        m = re.match(structure, rc)
    
    # now remove duplicates but maintain order.
    seen = set()
    out2 = []
    for note in out:
        if not note in seen:
            seen.add(note)
            out2.append(note)

    if out2 == []:
        err(13)
    return out2