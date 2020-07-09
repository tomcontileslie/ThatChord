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


# import error messages
from errors import err

def text(frets_in, height = 5, margin = 3, head = "=", string = "|", press = "O",\
         muted = "x", output_method = "PRINT", save_method = "NONE",          \
         save_loc = "diagrams/", name = "noname", left = False):
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
    frets = frets_in.copy()
    if left:
        frets.reverse()
        
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
        out += "\n" + " " * margin + head * (2 * n - 1)
    
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
    
    # only output options are PRINT or NONE. Print if requested.
    if output_method == "PRINT":
        print(out)
    
    # two possible save methods, if any are supplied.
    if save_method == "SINGLE":
        filename = save_loc + "ThatChordTemp.txt"
    if save_method == "LIBRARY":
        filename = save_loc + "ThatChord" + name + ".txt"
        
    if save_method == "SINGLE" or save_method == "LIBRARY":
        try:
            f = open(filename, "w")
        except FileNotFoundError:
            err("file not found")
        f.write(out)
        f.close()


def img(frets_in, title = "", top = False, height = 5, output_method = "SPLASH", \
        save_method = "NONE", save_loc = "diagrams/", name = "noname",        \
        left = False):
    """
    CREATES A SMALL PNG IMAGE (each pixel is one bit).
    
    frets is the list of pressed frets. 0 for nothing, -1 for mute.
    
    if a title is supplied, it is printed below the grid unless "top"
    is true, in which case more space is made above the grid.
    
    height is the minimum hight of the grid.
    
    The size of each square in the grid is 20 pixels.
    """
    from PIL import Image, ImageDraw
    
    frets = frets_in.copy()
    if left:
        frets.reverse()
    
    n = len(frets)
    
    # first, determine whether to print the header.
    # lo is the lowest fret printed.
    if max(frets) <= 5 or min([i for i in frets if i != 0 and i != -1]) < 3:
        header = True
        lo     = 1
    else:
        header = False
        lo     = min([i for i in frets if i != 0 and i != -1])
    
    # h is the number of frets printed.
    h = max(lo + height - 1, max(frets)) - lo + 1
    
    # determine extra space
    if top:
        b = 10
    else:
        b = 0
    
    # dimensions of output
    wid = (n + 1) * 20
    hgh = (h + 2) * 20 + b
    
    # create new image, white bg
    img = Image.new("1", (wid, hgh), color = "white")
    drw = ImageDraw.Draw(img)
    
    # draw header if needed
    if header:
        h1 = (20, 19 + b)
        h2 = (n * 20, 19 + b)
        drw.line([h1, h2], width = 3)
    # otherwise, need a fret number
    else:
        k = len(str(lo))
        fx = 12 - 5 * k
        fy = 25 + b
        drw.text((fx, fy), str(lo))
    
    # Draw vertical lines
    for i in range(n):
        l1 = ((i + 1) * 20, 20 + b)
        l2 = ((i + 1) * 20, (h + 1) * 20 + b)
        drw.line([l1, l2], width = 1)

    # Draw horizontal lines
    for i in range(h + 1):
        l1 = (20, (i + 1) * 20 + b)
        l2 = (n * 20, (i + 1) * 20 + b)
        drw.line([l1, l2], width = 1)

    # make a function for circles and crosses
    def mark(string, fret, r = 5):
        """
        r is the radius.
        string numbering starts at 0.
        fret numbering starts at 1 and -1 is also okay.
        xc, yc are coordinates of centre of mark
        """
        # if no fret is pressed, then do nothing.
        if fret == 0:
            return
        
        xc = (string + 1) * 20
        if fret > 0:
            yc = fret * 20 + 10 + b
            drw.ellipse([(xc - r, yc - r), (xc + r, yc + r)], fill = "black")
        else:
            yc = 11 + b
            drw.line([(xc - 4, yc - 4), (xc + 3, yc + 3)], width = 2)
            drw.line([(xc - 3, yc + 3), (xc + 4, yc - 4)], width = 2)
    
    # add a title if supplied
    if title:
        if top:
            tx = 20
            ty = 3

        else:
            tx = 20
            ty = (h + 1) * 20 + 3 + b
        drw.text((tx, ty), title)
    
    # the one thing we need to do before adding marks is shift everything
    # if there is no header.
    if not header:
        fretsn = []
        for note in frets:
            if not (note == 0 or note == -1):
                fretsn.append(note - lo + 1)
            else:
                fretsn.append(note)
    else:
        fretsn = frets
    
    # now add marks
    for i in range(n):
        mark(i, fretsn[i])
    
    # if output is requested
    if output_method == "SPLASH":
        img.show()
    
    # two possible save methods, if any are supplied.
    if save_method == "SINGLE":
        filename = save_loc + "ThatChordTemp.png"
    if save_method == "LIBRARY":
        filename = save_loc + "ThatChord" + name + ".png"
        
    if save_method == "SINGLE" or save_method == "LIBRARY":
        try:
            img.save(filename)
        except OSError:
            err("file not found")
