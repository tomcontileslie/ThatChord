###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                              thatchord.py  ##
##                                                                           ##
##  THIS FILE COLLECTS ALL SUBPROCESSES FROM OTHER FILES AND RUNS THATCHORD  ##
##  You can change the "request" string in this file and that will have an   ##
##  effect, provided input_type is set to DIRECT in settings.py. The rest    ##
##  of this file should not be changed.                                      ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################








############             ENTER YOUR CHORD REQUEST HERE             ############

# --------------------------------------------------------------------------- #
request =                        "Gadd9"
# --------------------------------------------------------------------------- #


############            SET YOUR WORKING DIRECTORY HERE            ############
#####                 recommended: "~/Documents/ThatChord"                #####

# --------------------------------------------------------------------------- #
wdir =                     "~/Documents/ThatChord"
# --------------------------------------------------------------------------- #
































# DO NOT CHANGE THE FOLLOWING CODE. THIS IS WHERE THE MAGIC HAPPENS.

# change current directory
import os
os.chdir(os.path.expanduser(wdir))

# Load settings
exec(open("settings.py").read())

# Load other files
import interpret
import find
import rank
import output
import custom

# First, figure out what the request is.
if input_type == "CONSOLE":
    request = input("Enter request here: ")
if input_type == "TERMINAL":
    import sys
    request = sys.argv[1]

# Special inputs here:
if request == "SETTINGS":
    # Typing SETTINGS opens the settings file.
    os.system("open settings.py")
    exit()

# Check whether a specific position in the list was requested. If not, 0 is
# default.
listpos = 0

if ":" in request:
    colon_positions = [i for i, x in enumerate(request) if x == ":"]
    if len(colon_positions) > 1:
        err("colons")
    # if we made it here then there must be exactly one colon
    try:
        listpos = int(request[colon_positions[0] + 1:]) - 1
    except ValueError:
        err(15)
    # remove the colon bit from the request
    request = request[:colon_positions[0]]
    

if request[0:6] == "CUSTOM":
    # custom note by note input triggered. Code in "custom.py".
    chord = custom.interpret(request[6:])
    # title removes CUSTOM but adds exclamation mark to indicate custom.
    title = "!" + request[6:]
    filename = request
else:
    # Standard input. Use normal function.
    chord = interpret.interpret(request)
    # Title and filename of chord (for potential output) is the request string.
    title = request
    filename = request

# Find the list of chords.
options = find.find(chord, tuning, nfrets, nmute, important)

# Sort the options using rank
options.sort(key = lambda x : rank.rank(x, chord, tuning, order, ranks))

# Check the requested option is not too big
if listpos >= len(options):
    err(16)

# figure out what the output format is
if output_format == "TEXT":
    output.text(
            options[listpos],
            name = filename,
            title = title,
            **kwgrargs,
            **kwioargs
            )

# TODO no options for where to put title yet
if output_format == "PNG":
    output.img(
            options[listpos],
            name = filename,
            title = title,
            **kwgrargs,
            **kwioargs
            )
