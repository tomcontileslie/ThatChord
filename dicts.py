###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                                  dicts.py  ##
##                                                                           ##
##  "notes" converts letters to note numbers.                                ##
##                                                                           ##
##  "qualities" is a large list of possible chord qualities. The default is  ##
##  to map each quality to the corresponding chord with root C. The notes    ##
##  are then shifted in interpret.py. Qualities with parentheses need not    ##
##  be entered (bar a few exceptions which are not picked up by the regex)   ##
##  since altered notes are handled in interpret.py.                         ##
##  There are so many chord qualities! Feel free to suggest more!            ##
##  Formatting: enter the "most important" notes first. Usually only the     ##
##  root matters but I would recommend the first two entries being 0, 7 on   ##
##  most chords. In some cases, the algorithm will try to match these to     ##
##  lower strings.                                                           ##
##                                                                           ##
##  "alterations" converts each degree into a 2-tuple. The first element is  ##
##  the 'flat' element to be sharpened if the alteration is > 0. The second  ##
##  is the 'sharp' element to be flattened if the alt is < 0.                ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################


notes = {
        "C"  : 0,
        "D"  : 2,
        "E"  : 4,
        "F"  : 5,
        "G"  : 7,
        "A"  : 9,
        "B"  : 11,

        "c"  : 0,
        "d"  : 2,
        "e"  : 4,
        "f"  : 5,
        "g"  : 7,
        "a"  : 9,
        "b"  : 11,
        }

qualities = {
        None       : [0, 7, 4],
        ""         : [0, 7, 4],
        "M"        : [0, 7, 4],
        "maj"      : [0, 7, 4],
        "Maj"      : [0, 7, 4],
        
        "m"        : [0, 7, 3],
        "Min"      : [0, 7, 3],
        "min"      : [0, 7, 3],
        "-"        : [0, 7, 3],
        
        "sus2"     : [0, 2, 7],
        "Sus2"     : [0, 2, 7],
        
        "sus4"     : [0, 5, 7],
        "sus"      : [0, 5, 7],
        "Sus4"     : [0, 5, 7],
        "Sus"      : [0, 5, 7],
        
        "5"        : [0, 7],
        
        "mb6"      : [0, 7, 3, 8],
        "minb6"    : [0, 7, 3, 8],
        
        "m6"       : [0, 7, 3, 9],
        "min6"     : [0, 7, 3, 9],
        "Min6"     : [0, 7, 3, 9],
        
        "6"        : [0, 7, 4, 9],
        "add6"     : [0, 7, 4, 9],
        "Add6"     : [0, 7, 4, 9],
        "add13"    : [0, 7, 4, 9],
        "Add13"    : [0, 7, 4, 9],
        
        "m7"       : [0, 7, 3, 10],
        "min7"     : [0, 7, 3, 10],
        "Min7"     : [0, 7, 3, 10],
        
        "7"        : [0, 7, 10, 4],
        
        "M7"       : [0, 7, 4, 11],
        "maj7"     : [0, 7, 4, 11],
        "Maj7"     : [0, 7, 4, 11],
        "delta"    : [0, 7, 4, 11],
        "Delta"    : [0, 7, 4, 11],
        
        "9"        : [0, 2, 7, 4, 10],
        
        "M9"       : [0, 2, 7, 4, 11],
        "Maj9"     : [0, 2, 7, 4, 11],
        "maj9"     : [0, 2, 7, 4, 11],
        
        "add9"     : [0, 7, 2, 4],
        "Add9"     : [0, 7, 2, 4],
        "Madd9"    : [0, 7, 2, 4],
        "MAdd9"    : [0, 7, 2, 4],
        
        "madd9"    : [0, 2, 7, 3],
        "mAdd9"    : [0, 2, 7, 3],
        
        "11"       : [0, 5, 7, 10, 2, 4],
        
        "M11"      : [0, 2, 7, 5, 4, 11],
        "maj11"    : [0, 2, 7, 5, 4, 11],
        "Maj11"    : [0, 2, 7, 5, 4, 11],
        
        "mMaj11"   : [0, 2, 7, 5, 3, 11],
        "-M11"     : [0, 2, 7, 5, 3, 11],
        "mM11"     : [0, 2, 7, 5, 3, 11],
        
        "m11"      : [0, 2, 7, 5, 3, 10],
        "-11"      : [0, 2, 7, 5, 3, 10],
        "min11"    : [0, 2, 7, 5, 3, 10],
        
        "add11"    : [0, 7, 5, 4],
        "Add11"    : [0, 7, 5, 4],

        "13"       : [0, 9, 7, 4, 10, 2, 5],

        "m13"      : [0, 9, 7, 3, 10, 2, 5],
        "min13"    : [0, 9, 7, 3, 10, 2, 5],
        "Min13"    : [0, 9, 7, 3, 10, 2, 5],

        "M13"      : [0, 9, 7, 3, 11, 2, 5],
        "maj13"    : [0, 9, 7, 3, 11, 2, 5],
        "Maj13"    : [0, 9, 7, 3, 11, 2, 5],

        "dim"      : [0, 3, 6],
        "Dim"      : [0, 3, 6],
        
        "dim7"     : [0, 3, 6, 9],
        "Dim7"     : [0, 3, 6, 9],
        
        "aug"      : [0, 4, 8],
        "Aug"      : [0, 4, 8],
        "+"        : [0, 4, 8],
        
        "7sus4"    : [0, 5, 7, 10],
        "7Sus4"    : [0, 5, 7, 10],
        "7sus"     : [0, 5, 7, 10],
        "7Sus"     : [0, 5, 7, 10],
        
        "7sus2"    : [0, 2, 7, 10],
        "7Sus2"    : [0, 2, 7, 10],
        
        "aug7"     : [0, 4, 8, 10],
        "Aug7"     : [0, 4, 8, 10],
        "+7"       : [0, 4, 8, 10],
        "7aug"     : [0, 4, 8, 10],
        "7Aug"     : [0, 4, 8, 10],
        "7+"       : [0, 4, 8, 10],
        
        "mM7"      : [0, 7, 3, 11],
        "minM7"    : [0, 7, 3, 11],
        "mm7"      : [0, 7, 3, 11],
        
        "augmaj7"  : [0, 4, 8, 11],
        "Augmaj7"  : [0, 4, 8, 11],
        "augMaj7"  : [0, 4, 8, 11],
        "AugMaj7"  : [0, 4, 8, 11],
        "augM7"    : [0, 4, 8, 11],
        "AugM7"    : [0, 4, 8, 11],
        "M7#5"     : [0, 4, 8, 11],
        "M7+5"     : [0, 4, 8, 11],
        "+M7"      : [0, 4, 8, 11],
        "+maj7"    : [0, 4, 8, 11],
        "+Maj7"    : [0, 4, 8, 11],
        
        "add#9"    : [0, 7, 4, 3],
        "Madd#9"   : [0, 7, 4, 3],

        "13sus4"   : [0, 7, 9, 5, 10, 2]
        }

alterations = {
        1  : (0,  0),
        2  : (2,  2),
        3  : (3,  4),
        4  : (5,  5),
        5  : (7,  7),
        6  : (9,  9),
        7  : (10, 11),
        9  : (2,  2),
        11 : (5,  5),
        13 : (9,  9)
        }
