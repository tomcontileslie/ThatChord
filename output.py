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

import os
import platform # To differentiate between platforms
# import error messages
from errors import err

def text(
         frets_in,
         
         # filename to save under
         name = "noname",
         title = "",
         
         # graphical parameters, will be passed as **kwgrargs
         height = 5,
         margin = 3,
         head = "=",
         string = "|",
         press = "O",
         muted = "x",
         left = False,
         top = True,
         stringstarts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # for all nstrings
         
         # input/output arguments, will be passed as **kwioargs
         output_method = "PRINT",
         save_method = "NONE",
         save_loc = "diagrams",
        ):
    
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
    
    # at the very top, print the title, provided top is True.
    if top:
        out = " " * margin + title + "\n"
    else:
        out = ""
    
    # first, determine whether to print the header.
    # lo is the lowest fret printed.
    if max(frets) <= height or min([i for i in frets if i != 0 and i != -1]) < 3:
        header = True
        lo     = 1
    else:
        header = False
        lo     = min([i for i in frets if i != 0 and i != -1])
    
    # hi is the highest fret printed.
    # first argument in the max is the minimum size, 
    hi = max(lo + height - 1, max(frets))
    
    # initialise output string.
    out += " " * margin
    
    # there is an empty line at the top with x's if any strings are not played
    # xs also if the requested fret is below the start of the string
    # e.g. banjo
    for i in range(len(frets)):
        if frets[i] < stringstarts[i]: # i.e. either -1 or banjo situation
            out += muted + " "
        else:
            out += "  "
    
    # draw header if needed. only draw above strings that start at 0.
    if header:
        # we need to have some free space in the margin.
        if not margin >= 1:
            err("fermat")
        
        out += "\n" + " " * (margin - 1)
        
        # now print headers where needed. They link up if the prev string also
        # had a header.
        curr = False
        for i in range(len(frets)):
            # shuffle along the neck.
            last, curr = curr, stringstarts[i] == 0
            if curr:
                if last:
                    # link up this string with previous
                    out += head * 2
                else:
                    # previous string had no head, just draw head over current
                    out += " " + head
            else:
                # no header necessary, current string does not go to top
                out += "  "
    
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
        
        # draw pressed notes and strings, checking whether we are below the
        # start of the string each time (e.g. banjo).
        for i in range(len(frets)):
            if stringstarts[i] < line:
                if frets[i] == line:
                    out += press + " "
                else:
                    out += string + " "
            else:
                # in this case we're below the start of the string.
                # print nothing.
                out += "  "
    
    # Print the title here if top is False.
    if not top:
        out += "\n\n" + " " * margin + title
    
    # Print if requested.
    if output_method == "PRINT":
        print(out)

    # two possible save methods, if any are supplied.
    if save_method == "SINGLE":
        filename = os.path.join(save_loc, "ThatChordTemp.txt")
    elif save_method == "LIBRARY":
        filename = os.path.join(save_loc, "ThatChord" + name + ".txt")
        
    if save_method == "SINGLE" or save_method == "LIBRARY":

        try:
            if not os.path.isdir(save_loc):
                os.makedirs(save_loc)
            with open(filename, "w") as f:
                f.write(out)
        except OSError:
            err("file not found")
        except FileNotFoundError:
            err("file not found")
    
    # If asked to splash, do so now that the file is saved.
    if output_method == "SPLASH":
        if platform.system() == "Linux":
            os.system("xdg-open " + filename)
        else:
            os.system("open " + filename)
    
    # If not asked to do anything, return value.
    if output_method == "NONE":
        return out


def img(
        frets_in,
        
        # filename to save under if necessary
        name = "noname",
        # header to print on actual image
        title = "",
        
        # graphical parameters: not all used, need to be same as for text.
        # will be passed as **kwgrargs.
        height = 5,
        margin = 3,
        head = "=",
        string = "|",
        press = "O",
        muted = "x",
        left = False,
        top = True,
        stringstarts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # for big nstrings
        
        # input/output arguments, will be passed as **kwioargs
        output_method = "SPLASH",
        save_method = "NONE",
        save_loc = "diagrams/",
        ):
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
    if max(frets) <= height or min([i for i in frets if i != 0 and i != -1]) < 3:
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
    
    # draw header if needed. If we have banjo-style strings we can chop
    # off either side of the header.
    if header:
        leftchop, rightchop   = 0, 0
        leftcheck, rightcheck = True, True
        i = 0
        while (leftcheck or rightcheck) and i < n:
            if stringstarts[i] > 0 and leftcheck:
                leftchop += 1
            else:
                leftcheck = False
            if stringstarts[n - i - 1] > 0 and rightcheck:
                rightchop += 1
            else:
                rightcheck = False
            i += 1
        
        # leftchop and rightchop should now have values defining how many
        # strings off either side are missing at the neck.
        # strings missing in the middle are not supported currently.
        h1 = ((leftchop + 1) * 20, 19 + b)
        h2 = ((n - rightchop) * 20, 19 + b)
        drw.line([h1, h2], width = 3)
    # otherwise, need a fret number
    else:
        k = len(str(lo))
        fx = 12 - 5 * k
        fy = 25 + b
        drw.text((fx, fy), str(lo))
    
    # Draw vertical lines. Start at stringstart and go all the way to h.
    # if, somehow, the string starts higher than the part drawn, then don't
    # draw at all.
    for i in range(n):
        stringlo = stringstarts[i] - lo + 1
        # only draw if starts in range
        if stringlo < lo + h:
            if stringlo < 0:
                # then we start at 0, do not draw earlier
                stringlo = 0
            l1 = ((i + 1) * 20, (stringlo + 1) * 20 + b)
            l2 = ((i + 1) * 20, (h + 1) * 20 + b)
            drw.line([l1, l2], width = 1)

    # Draw horizontal lines. As for the header, at each horizontal step we
    # chop off left and right.
    for i in range(h + 1):
        # calculate the corresponding fret, e.g. if i = 1 and lo = 3 we are
        # on fret 4.
        fret = i + lo
        leftchop, rightchop   = 0, 0
        leftcheck, rightcheck = True, True
        j = 0
        while (leftcheck or rightcheck) and j < n:
            if stringstarts[j] > fret - 1 and leftcheck:
                leftchop += 1
            else:
                leftcheck = False
            if stringstarts[n - j - 1] > fret - 1 and rightcheck:
                rightchop += 1
            else:
                rightcheck = False
            j += 1
        
        l1 = ((leftchop + 1) * 20, (i + 1) * 20 + b)
        l2 = ((n - rightchop) * 20, (i + 1) * 20 + b)
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
    # so that frets too low on the short banjo string are muted, empty strings
    # are correct, and also so that everything shifts if there is no header.
    fretsn = []
    for i in range(n):
        if frets[i] < stringstarts[i]:
            fretsn.append(-1)
        elif frets[i] == stringstarts[i]:
            fretsn.append(0)
        else:
            fretsn.append(frets[i] - lo + 1)
    
    # now add marks
    for i in range(n):
        mark(i, fretsn[i])
    
    # if output is requested
    if output_method == "SPLASH":
        img.show()
    
    # two possible save methods, if any are supplied.
    if save_method == "SINGLE":
        filename = os.path.join(save_loc, "ThatChordTemp.png")
    elif save_method == "LIBRARY":
        filename = os.path.join(save_loc, "ThatChord" + name + ".png")
        
    if save_method == "SINGLE" or save_method == "LIBRARY":
        try:
            # create the folder if it doesn't exist
            if not os.path.isdir(save_loc):
                os.makedirs(save_loc)
            img.save(filename)
        except OSError:
            err("file not found")
