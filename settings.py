###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                               settings.py  ##
##                                                                           ##
##  This file defines a function which takes in a settings file location     ##
##  and potential manual settings assignments, then combines these settings  ##
##  and overwrites manual assignments with any presets that are defined.     ##
##  Note that manual assignments in the function's variables overwrite       ##
##  assignments in the settings file.                                        ##
##                                                                           ##
##                                                                           ##
##  License: CC BY-SA 4.0                                                    ##
##                                                                           ##
##  Contact: tom (dot) contileslie (at) gmail (dot) com                      ##
##                                                                           ##
###############################################################################
###############################################################################

def get_settings(settingsfile      = "settings.yml",
                 # NB.: settingsfile is relative to ThatChord directory.
                 instrument_preset = None,
                 ranking_preset    = None,
                 tuning            = None,
                 nfrets            = None,
                 nmute             = None,
                 important         = None,
                 order             = None,
                 left              = None,
                 stringstarts      = None,
                 ranks             = None,
                 input_type        = None,
                 output_format     = None,
                 output_method     = None,
                 save_method       = None,
                 save_loc          = None,
                 height            = None,
                 margin            = None,
                 head              = None,
                 string            = None,
                 press             = None,
                 muted             = None,
                 top               = None,
                 ):

    # firstly, put the manual assignments aside.

    xinstrument_preset = instrument_preset
    xranking_preset    = ranking_preset
    xtuning            = tuning
    xnfrets            = nfrets
    xnmute             = nmute
    ximportant         = important
    xorder             = order
    xleft              = left
    xstringstarts      = stringstarts
    xranks             = ranks
    xinput_type        = input_type
    xoutput_format     = output_format
    xoutput_method     = output_method
    xsave_method       = save_method
    xsave_loc          = save_loc
    xheight            = height
    xmargin            = margin
    xhead              = head
    xstring            = string
    xpress             = press
    xmuted             = muted
    xtop               = top


    # PRIORITY LEVEL 1: default values for all variables.
    
    instrument_preset = "UKULELE"
    
    tuning       = [7, 0, 4, 9]
    nfrets       = 12
    nmute        = 0
    important    = 4
    order        = [2, 0, 1, 3]
    left         = False
    stringstarts = [0, 0, 0, 0]
    
    ranking_preset = "UKULELE"
    
    ranks = [1, 2, 3, 1, 0, 0, 0, 0, 0]
    
    input_type = "TERMINAL"
    output_format = "PNG"
    output_method  = "SPLASH"
    save_method = "SINGLE"
    save_loc = "~/Documents/ThatChord/diagrams"
    
    height = 5
    margin = 3
    head   = "="
    string = "|"
    press  = "O"
    muted  = "x"
    top = True
    
    
    # PRIORITY LEVEL 2: overwrite default values with settings loaded from
    #                   settings.yml.
    
    import yaml
    import os
    from errors import err
    import custom
    
    script_directory = os.path.dirname(os.path.realpath(__file__))
    settings_path = os.path.join(script_directory, settingsfile)
    try:
        with open(settings_path, "r") as file:
            content = yaml.load(file, Loader=yaml.FullLoader)
            keys = content.keys()
            
            if "presets" in keys:
                for d in content["presets"]:
                    if "instrument" in d.keys():
                        instrument_preset = list(d.values())[0].upper()
                    if "ranking" in d.keys():
                        ranking_preset = list(d.values())[0].upper()
            else:
                err(20)
            
            if "input" in keys:
                for d in content["input"]:
                    if "how" in d.keys():
                        input_type = list(d.values())[0].upper()
            else:
                err(20)
            
            if "output" in keys:
                for d in content["output"]:
                    if "how" in d.keys():
                        output_method = list(d.values())[0].upper()
                    if "format" in d.keys():
                        output_format = list(d.values())[0].upper()
            else:
                err(20)
            
            if "saving" in keys:
                for d in content["saving"]:
                    if "method" in d.keys():
                        save_method = list(d.values())[0].upper()
                    if "location" in d.keys():
                        save_loc = list(d.values())[0]
            else:
                err(20)
            
            if "custom_instrument" in keys:
                for d in content["custom_instrument"]:
                    if "tuning" in d.keys():
                        tuning = custom.interpret(list(d.values())[0],
                                                  remove_duplicates = False)
                    if "nfrets" in d.keys():
                        nfrets = list(d.values())[0]
                    if "nmute" in d.keys():
                        nmute = list(d.values())[0]
                    if "important" in d.keys():
                        important = list(d.values())[0]
                    if "order" in d.keys():
                        order = list(d.values())[0].copy()
                    if "handedness" in d.keys():
                        handedness = list(d.values())[0].upper()
                        if handedness in ["LEFT", "RIGHT"]:
                            left = {"LEFT" : True, "RIGHT" : False}[handedness]
                    if "stringstarts" in d.keys():
                        stringstarts = list(d.values())[0].copy()
            else:
                err(20)
            
            if "custom_ranking" in keys:
                for d in content["custom_ranking"]:
                    if "ranks" in d.keys():
                        ranks = list(d.values())[0].copy()
            else:
                err(20)
                
            if "graphical_parameters" in keys:
                for d in content["graphical_parameters"]:
                    if "height" in d.keys():
                        height = list(d.values())[0]
                    if "margin" in d.keys():
                        margin = list(d.values())[0]
                    if "head" in d.keys():
                        head = list(d.values())[0]
                    if "string" in d.keys():
                        string = list(d.values())[0]
                    if "press" in d.keys():
                        press = list(d.values())[0]
                    if "muted" in d.keys():
                        muted = list(d.values())[0]
                    if "title_at_top" in d.keys():
                        top = list(d.values())[0]
            else:
                err(20)
    except FileNotFoundError:
        err(19)
   
    
    # PRIORITY LEVEL 3: MANUAL ASSIGNMENTS.
    
    if xinstrument_preset:
        instrument_preset = xinstrument_preset.upper()
    if xranking_preset:
        ranking_preset = xranking_preset.upper()
    if xtuning:
        tuning = xtuning
    if xnfrets:
        nfrets = xnfrets
    if xnmute:
        nmute = xnmute
    if ximportant:
        important = ximportant
    if xorder:
        order = xorder
    if xleft:
        left = xleft
    if xstringstarts:
        stringstarts = xstringstarts
    if xranks:
        ranks = xranks
    if xinput_type:
        input_type = xinput_type.upper()
    if xoutput_format:
        output_format = xoutput_format.upper()
    if xoutput_method:
        output_method = xoutput_method.upper()
    if xsave_method:
        save_method = xsave_method.upper()
    if xsave_loc:
        save_loc = xsave_loc
    if xheight:
        height = xheight
    if xmargin:
        margin = xmargin
    if xhead:
        head = xhead
    if xstring:
        string = xstring
    if xpress:
        press = xpress
    if xmuted:
        muted = xmuted
    if xtop:
        top = xtop
    
    # APPLY PRESETS: firstly remove -L tag
    if instrument_preset[-2:] == "-L":
        left = True
        instrument_preset = instrument_preset[0:-2]
        
    # APPLY PRESETS: check for a file in presets/instruments.
    script_directory = os.path.dirname(os.path.realpath(__file__))
    preset_path = os.path.join(script_directory,
                               "presets/instruments/" + instrument_preset + ".yml")
    ymldict = {}
    try:
        with open(preset_path, "r") as file:
            ymldict = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        # if there is no file with correct name, see if index can redirect
        index_path = os.path.join(script_directory,
                                  "presets/instruments/_index.yml")
        with open(index_path, "r") as file:
            index = yaml.load(file, Loader=yaml.FullLoader)
            if instrument_preset in index.keys():
                preset_path = os.path.join(script_directory,
                                           ("presets/instruments/" +
                                           index[instrument_preset] +
                                           ".yml"))
                try:
                    with open(preset_path, "r") as file:
                        ymldict = yaml.load(file, Loader=yaml.FullLoader)
                except FileNotFoundError:
                    pass

    # if a settings file was found, its contents are now in ymldict.
    keys = ymldict.keys()
    if "tuning" in keys:
        tuning = custom.interpret(ymldict["tuning"],
                                  remove_duplicates = False)
    if "nfrets" in keys:
        nfrets = ymldict["nfrets"]
    if "nmute" in keys:
        nmute = ymldict["nmute"]
    if "important" in keys:
        important = ymldict["important"]
    if "order" in keys:
        order = ymldict["order"]
    if "stringstarts" in keys:
        stringstarts = ymldict["stringstarts"]
    if "height" in keys:
        height = ymldict["height"]
    if "margin" in keys:
        margin = ymldict["margin"]
    if "head" in keys:
        head = ymldict["head"]
    if "string" in keys:
        string = ymldict["string"]
    if "press" in keys:
        press = ymldict["press"]
    if "muted" in keys:
        muted = ymldict["muted"]
    if "top" in keys:
        top = ymldict["top"]
        
    
    # DEFINE RANKING PRESETS HERE
    if ranking_preset in ["UKULELE"]:
        ranks = [1, 2, 3, 1, 0, 0, 0, 0, 0]
    
    if ranking_preset in ["GUITAR"]:
        ranks = [3, 0, 3, 1, 0, 5, 2, 5, 8]
    
    if ranking_preset in ["BANJO"]:
        ranks = [2, 1, 3, 0, 1, 0, 3, 2, 1]

    if ranking_preset in ["MANDOLIN"]:
        ranks = [1, 2, 3, 1, 0, 0, 0, 0, 0]
    
    
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
        
    if len(tuning) != len(order):
        err(17)
    
    if len(stringstarts) < len(tuning):
        err(18)
    
    # CHANGE TUNING TO IMAGINED NECK, FOR STRINGS STARTING HIGHER THAN 0TH FRET
    for i in range(len(tuning)):
        tuning[i] = (tuning[i] - stringstarts[i]) % 12
    
    # MAKE GRAPHICAL PARAMETERS DICTIONARY - for output functions
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
    
    # MAKE INPUT/OUTPUT PARAMETERS DICTIONARY - for output functions
    kwioargs = {
            "output_method" : output_method,
            "save_method"   : save_method,
            "save_loc"      : os.path.expanduser(save_loc)
            }
    
    # MAKE COMPLETE SETTINGS DICTIONARY - for use in main file
    settings = {
            "tuning"        : tuning,
            "nfrets"        : nfrets,
            "nmute"         : nmute,
            "important"     : important,
            "order"         : order,
            "left"          : left,
            "stringstarts"  : stringstarts,
            "ranks"         : ranks,
            "input_type"    : input_type,
            "output_format" : output_format,
            "output_method" : output_method,
            "save_method"   : save_method,
            "save_loc"      : save_loc}
    
    return settings, kwgrargs, kwioargs
