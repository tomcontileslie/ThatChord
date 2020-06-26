###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                                  print.py  ##
##                                                                           ##
##  This script provides functions which take a list of frets and some       ##
##  graphical parameters, and output various human-readable forms of         ##
##  diagrams.                                                                ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################


from errors import err

def text(frets, height = 5, margin = 3, head = "=", string = "|", press = "O", muted = "x"):
    """
    CREATES A STRING TO BE PRINTED
    
    frets is a list where the first entry is the fret pressed on the leftmost
    chord, etc. -1 means string is not played.
    
    in the absence of a wide reach in the frets pressed, the n. of frets of the
    diagram is the variable 'height'.
    
    margin is the number of white spaces before the first string.
    
    head is the appearance of the header.
    
    string is the appearance of untouched strings.
    
    press is the appearance of a pressed fret.
    
    muted is the mark at the top of a muted string.
    """
    # number of strings
    n = len(frets)
    
    # first, determine whether to print the header.
    # lo is the lowest fret printed.
    if max(frets) <= 5 or min([i for i in frets if i != 0 and i != -1]) < 3:
        header = True
        lo     = 1
    else:
        header = False
        lo     = min([i for i in frets if i != 0 and i != -1])
    
    # hi is the highest fret printed.
    # first argument in the max is the minimum size, 
    hi = max(lo + height - 1, max(frets))
    
    # initialise output string.
    out = " " * margin
    
    # there is an empty line at the top with x's if any strings are not played
    for i in frets:
        if i == -1:
            out += muted + " "
        else:
            out += "  "
    
    # draw header if needed.
    if header:
        out += "\n " * margin + head * (2 * n - 1)
    
    # start drawing the frets. There is a special case for the lowest one if
    # no header is displayed, since we'll need to indicate what fret we're on.
    for line in range(lo, hi + 1):
        out += "\n"
        if line == lo and not header:
            num = str(lo)
            # ensure line number is not too long to print
            if len(num) >= margin:
                err("fermat")
            out += " " * (margin - len(num) - 1) + num + " "
        else:
            # in this case the line has nothing special
            out += " " * margin
        
        for i in frets:
            if i == line:
                out += press + " "
            else:
                out += string + " "
        
    
    return out