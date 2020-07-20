###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                               settings.py  ##
##                                                                           ##
##  This file allows the user to specify a number of preferences. The first  ##
##  section is for instrument properties. Presets are available, always      ##
##  written in capital letters. When a preset is not recognised, the values  ##
##  underneath are taken.                                                    ##
##  The settings after that are for input/output modes, and graphical        ##
##  parameters for the output.                                               ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################

# IMPORTANT: PRESETS SURROUNDED BY QUOTATION MARKS ARE ALWAYS IN ALL CAPS.


# CHOOSE YOUR INSTRUMENT HERE, OR SET TO THE EMPTY STRING TO USE SETTINGS
# UNDERNEATH.
# --------------------------------------------------------------------------- #
instrument_preset = "UKULELE"
# --------------------------------------------------------------------------- #

# If the preset is unrecognised, the following values are used.
# See find.py to see what they do.
tuning       = [7, 0, 4, 9]
nfrets       = 12
nmute        = 0
important    = 4
order        = [2, 0, 1, 3]
left         = False
stringstarts = [0, 0, 0, 0]


# CHOOSE YOUR RANKING COEFFICIENT PRESET HERE, OR SET TO EMPTY TO USE SETTINGS
# UNDERNEATH.
# --------------------------------------------------------------------------- #
ranking_preset = "UKULELE"
# --------------------------------------------------------------------------- #

# If the preset is unrecognised, the following coefficients are used.
ranks = [1, 2, 3, 1, 0, 0, 0, 0, 0]


# CHOOSE YOUR INPUT MODE HERE. OPTIONS: DIRECT/TERMINAL/CONSOLE.
# DIRECT takes the contents of the string in the main file.
# TERMINAL assumes you are running python3 from your terminal and have
# written the chord name after the filename.
# CONSOLE assumes you are using a Python console and will ask for input.
# --------------------------------------------------------------------------- #
input_type = "TERMINAL"
# --------------------------------------------------------------------------- #


# CHOOSE YOUR OUTPUT FORMAT HERE. OPTIONS: TEXT/PNG.
# --------------------------------------------------------------------------- #
output_format = "PNG"
# --------------------------------------------------------------------------- #


# CHOOSE YOUR OUTPUT METHOD HERE. OPTIONS:
# PRINT: only available with TEXT format. Prints to console.
# SPLASH: Opens a temp file with the image.
# NONE: do nothing with the output. The file will still be saved if you want.
# --------------------------------------------------------------------------- #
output_method  = "SPLASH"
# --------------------------------------------------------------------------- #


# CHOOSE YOUR SAVE METHOD HERE. OPTIONS:
# SINGLE: saves one file in specified location, overwriting any others
# LIBRARY: makes a (semi)unique filename to avoid overwriting.
# NONE: don't save any files.
# --------------------------------------------------------------------------- #
save_method = "SINGLE"
# --------------------------------------------------------------------------- #
# files are saved to the following directory. Don't forget to add a slash.
# recommended is to save in a dedicated "diagrams/" folder inside the ThatChord
# folder.
# DANGER: SAVING MAY OVERWRITE LOCAL FILES. FILENAMES CONTAIN "THATCHORD" TO
# AVOID CLASHES WITH UNRELATED FILES.
save_loc = "diagrams/"


# GRAPHICAL PARAMETERS HERE. A number of drawing options are available. See
# what they do in output.py.
height = 5
margin = 3
head   = "="
string = "|"
press  = "O"
muted  = "x"
top = True




















###############################################################################
###############################################################################
####          DO   NOT   CHANGE   ANYTHING   PAST   THIS   POINT           ####
###############################################################################
###############################################################################


















from errors import err

if instrument_preset[-2:] == "-L":
    left = True
    instrument_preset = instrument_preset[0:-2]


# DEFINE INSTRUMENT PRESETS HERE
if instrument_preset in ["UKULELE", "UKULELE-SOPRANO", "UKULELE-REENTRANT",   \
                         "UKULELE-SOPRANO-REENTRANT"]:
    tuning    = [7, 0, 4, 9]
    nfrets    = 12
    nmute     = 0
    important = 4
    order     = [2, 0, 1, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-D", "UKULELE-SOPRANO-D",                    \
                         "UKULELE-D-REENTRANT", "UKULELE-SOPRANO-D-REENTRANT"]:
    # Ukulele in D tuning: aDF#B
    tuning    = [9, 2, 6, 11]
    nfrets    = 12
    nmute     = 0
    important = 4
    order     = [2, 0, 1, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-CONCERT", "UKULELE-CONCERT-REENTRANT"]:
    tuning    = [7, 0, 4, 9]
    nfrets    = 15
    nmute     = 0
    important = 4
    order     = [2, 0, 1, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-CONCERT-LINEAR"]:
    tuning    = [7, 0, 4, 9]
    nfrets    = 15
    nmute     = 0
    important = 4
    order     = [0, 1, 2, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-TENOR", "UKULELE-TENOR-REENTRANT"]:
    tuning    = [7, 0, 4, 9]
    nfrets    = 15
    nmute     = 0
    important = 4
    order     = [2, 0, 1, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-TENOR-LINEAR"]:
    tuning    = [7, 0, 4, 9]
    nfrets    = 15
    nmute     = 0
    important = 4
    order     = [0, 1, 2, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-TENOR-CHICAGO",                             \
                         "UKULELE-TENOR-CHICAGO-REENTRANT"]:
    tuning    = [2, 7, 11, 4]
    nfrets    = 15
    nmute     = 0
    important = 4
    order     = [2, 0, 1, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-TENOR-CHICAGO-LINEAR"]:
    tuning    = [2, 7, 11, 4]
    nfrets    = 15
    nmute     = 0
    important = 4
    order     = [0, 1, 2, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-BARITONE", "UKULELE-BARITONE-REENTRANT"]:
    tuning    = [7, 0, 4, 9]
    nfrets    = 19
    nmute     = 0
    important = 4
    order     = [2, 0, 1, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-BARITONE-LINEAR"]:
    tuning    = [7, 0, 4, 9]
    nfrets    = 19
    nmute     = 0
    important = 4
    order     = [0, 1, 2, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-BARITONE-CHICAGO",                          \
                         "UKULELE-BARITONE-CHICAGO-REENTRANT"]:
    tuning    = [2, 7, 11, 4]
    nfrets    = 19
    nmute     = 0
    important = 4
    order     = [2, 0, 1, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["UKULELE-BARITONE-CHICAGO-LINEAR"]:
    tuning    = [2, 7, 11, 4]
    nfrets    = 19
    nmute     = 0
    important = 4
    order     = [0, 1, 2, 3]
    stringstarts = [0, 0, 0, 0]

if instrument_preset in ["GUITAR"]:
    tuning    = [4, 9, 2, 7, 11, 4]
    nfrets    = 19
    nmute     = 2
    important = 6
    order     = [0, 1, 2, 3, 4, 5]
    stringstarts = [0, 0, 0, 0, 0, 0]

if instrument_preset in ["BANJO"]:
    tuning       = [7, 2, 7, 11, 2]
    nfrets       = 15
    nmute        = 1
    important    = 3 # usually not playing complex chords
    order        = [4, 0, 1, 2, 3]
    stringstarts = [5, 0, 0, 0, 0]
    height       = 6 # so that there's space for the additional string
    
if instrument_preset in ["SAZ"]:
    tuning       = [2, 7, 9]
    nfrets       = 14
    nmute        = 0
    important    = 3
    order        = [2, 0, 1]
    stringstarts = [0, 0, 0]
    

# DEFINE RANKING PRESETS HERE
if ranking_preset in ["UKULELE"]:
    ranks = [1, 2, 3, 1, 0, 0, 0, 0, 0]

if ranking_preset in ["GUITAR"]:
    ranks = [3, 0, 3, 1, 0, 5, 2, 5, 8]

if ranking_preset in ["BANJO"]:
    ranks = [2, 1, 3, 0, 1, 0, 3, 2, 1]


# SENSE CHECKING FOR I/O FORMATS
if not input_type in ["DIRECT", "TERMINAL", "CONSOLE"]:
    err("input type")

if not output_format in ["TEXT", "PNG"]:
    err("output format")

if not output_method in ["PRINT", "SPLASH", "NONE"]:
    err("output method")

if not save_method in ["SINGLE", "LIBRARY", "NONE"]:
    err("save method")

if output_method == "PRINT" and not output_format == "TEXT":
    err("incompatible output")

# CHANGE TUNING TO IMAGINED NECK, FOR STRINGS STARTING HIGHER THAN 0TH FRET
for i in range(len(tuning)):
    tuning[i] = (tuning[i] - stringstarts[i]) % 12

# MAKE GRAPHICAL PARAMETERS DICTIONARY
kwgrargs = {
        "height"       : height,
        "margin"       : margin,
        "head"         : head,
        "string"       : string,
        "press"        : press,
        "muted"        : muted,
        "left"         : left,
        "top"          : top,
        "stringstarts" : stringstarts,
        }

# MAKE INPUT/OUTPUT PARAMETERS DICTIONARY
kwioargs = {
        "output_method" : output_method,
        "save_method"   : save_method,
        "save_loc"      : save_loc
        }