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


# SET YOUR WORKING DIRECTORY HERE (recommended: "~/Documents/ThatChord")
import os
os.chdir("/Users/tomcontileslie/Documents/ThatChord")


# TODO custom note-by-note input
# TODO way to print more chord options













# DO NOT CHANGE THE FOLLOWING CODE. THIS IS WHERE THE MAGIC HAPPENS.

# Load settings
exec(open("settings.py").read())

# Load other files
import interpret
import find
import rank
import output

# First, figure out what the request is.
if input_type == "CONSOLE":
    request = input("Enter request here: ")
if input_type == "TERMINAL":
    import sys
    request = sys.argv[1]

# Interpret the request.
chord = interpret.interpret(request)

# Find the list of chords.
options = find.find(chord, tuning, nfrets, nmute, important)

# Sort the options using rank
options.sort(key = lambda x : rank.rank(x, chord, tuning, order, ranks))

# figure out what the output format is
if output_format == "TEXT":
    output.text(options[0], height, margin, head, string, press, muted,       \
                output_method, save_method, save_loc, request, left)

# TODO no options for where to put title yet
if output_format == "PNG":
    output.img(options[0], request, True, height, output_method, save_method, \
               save_loc, request, left)
