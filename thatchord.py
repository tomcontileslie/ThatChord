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
































# DO NOT CHANGE THE FOLLOWING CODE. THIS IS WHERE THE MAGIC HAPPENS.

# change current directory
import os
import platform # To differentiate between platforms

# Load other files
import interpret
import find
import rank
import output
import custom
import settings
from errors import err

# Load settings from file. All defaults here so empty input.
tcsettings, kwgrargs, kwioargs = settings.get_settings()

# First, figure out what the request is.
if tcsettings["input_type"] == "CONSOLE":
    request = input("Enter request here: ")
elif tcsettings["input_type"] == "TERMINAL":
    import sys
    import argparse

    # Terminal input allows for command line options.
    parser = argparse.ArgumentParser(prog = "thatchord.py",
                                     usage = ("python3 thatchord.py <request> "+
                                              "[OPTIONS]"))

    parser.add_argument("request", nargs = 1, type = str,
            help = ("requested chord of form WX(Y)/Z:T, " +
                    "where W is the root note, "          +
                    "X is the chord quality, "            +
                    "Y is a list of alterations, "        +
                    "Z is the bass note, "                +
                    "and T is the desired index in the list"))

    parser.add_argument("-c", "--configuration", nargs = "?", type = str,
                        help = (".yml file to take settings from; its settings"+
                                " are overriden by the options below"))

    parser.add_argument("-i", "--instrument", nargs = "?", type = str,
                        help = "instrument preset")

    parser.add_argument("-r", "--ranking", nargs = "?", type = str,
                        help = "ranking preset")

    parser.add_argument("-f", "--format", nargs = "?", type = str,
                        help = "output format: text or png")

    parser.add_argument("-o", "--output", nargs = "?", type = str,
                        help = "output method: print, splash or none")

    parser.add_argument("-s", "--save", nargs = "?", type = str,
                        help = "save method: single, library or none")

    parser.add_argument("-d", "--directory", nargs = "?", type = str,
                        help = "directory to save diagrams")

    args = parser.parse_args()

    request = args.request[0]

    # populate dict with kwargs
    override = {"instrument_preset" : args.instrument,
                "ranking_preset"    : args.ranking,
                "output_format"     : args.format,
                "output_method"     : args.output,
                "save_method"       : args.save,
                "save_loc"          : args.directory}
    if args.configuration:
        override["settingsfile"] = args.configuration

    tcsettings, kwgrargs, kwioargs = settings.get_settings(**override)

# Special inputs here:
if request.upper() == "SETTINGS":
    # Typing SETTINGS opens the settings file.
    script_directory = os.path.dirname(os.path.realpath(__file__))
    settings_path = os.path.join(script_directory, "settings.yml")
    if platform.system() == "Linux":
        os.system("xdg-open " + settings_path)
    else:
        os.system("open " + settings_path)
    exit()

# Check whether a specific position in the list was requested. If not, 1 is
# default (best option).
listpos = 1

if ":" in request:
    colon_positions = [i for i, x in enumerate(request) if x == ":"]
    if len(colon_positions) > 1:
        err("colons")
    # if we made it here then there must be exactly one colon
    try:
        listpos = int(request[colon_positions[0] + 1:])
    except ValueError:
        err(15)
    # remove the colon bit from the request
    request = request[:colon_positions[0]]
    
# Check whether a minimum fret height was specified (fretspec).
at = 0

if "@" in request:
    at_positions = [i for i, x in enumerate(request) if x == "@"]
    if len(at_positions) > 1:
        err("ats")
    # if we made it here then there must be exactly one @
    try:
        at = int(request[at_positions[0] + 1:])
    except ValueError:
        err(22)
    # remove the colon bit from the request
    request = request[:at_positions[0]]
if at > tcsettings["nfrets"]:
    err(23)

if request[0:6].upper() == "CUSTOM":
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

# Find the chord at the requested listpos.
solution = find.find(chord,
                     nmute = tcsettings["nmute"],
                     important = tcsettings["important"],
                     index = listpos,
                     nfrets = tcsettings["nfrets"],
                     tuning = tcsettings["tuning"],
                     order = tcsettings["order"],
                     ranks = tcsettings["ranks"],
                     stringstarts = tcsettings["stringstarts"],
                     fretspec = at)


# figure out what the output format is
if tcsettings["output_format"] == "TEXT":
    output.text(
            solution,
            name = filename,
            title = title,
            **kwgrargs,
            **kwioargs
            )

# TODO no options for where to put title yet
elif tcsettings["output_format"] == "PNG":
    output.img(
            solution,
            name = filename,
            title = title,
            **kwgrargs,
            **kwioargs
            )
