###############################################################################
###############################################################################
##                                                                           ##
##  THATCHORD BY TOM CONTI-LESLIE                                   rank.py  ##
##                                                                           ##
##  This file provides a number of functions which assess different          ##
##  characteristics of a list of frets. Combining them will then produce     ##
##  a key used to rank options when returning a diagram.                     ##
##  The convention is that larger numbers are worse.                         ##
##  More metrics for assessing "goodness" of a chord are welcome.            ##
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

def rank_reach(frets, chord, tuning, order):
    """
    Returns the distance between the highest and lowest fret that needs
    to be pressed when playing the chord
    """
    pressed = [i for i in frets if i != 0 and i != -1]
    if len(pressed) == 0:
        return 0
    else:
        return (max(pressed) - min(pressed))

def rank_spread(frets, chord, tuning, order):
    """
    Similar to reach, but includes empty strings as well, in order to measure
    how 'spread out' the chord sounds.
    """
    played = [i for i in frets if i != -1]
    if len(played) == 0:
        return 0
    else:
        return max(played) - min(played)

def rank_fingers(frets, chord, tuning, order):
    """
    Returns the 'number of figners needed to play the chord', i.e. number
    of strings that are pressed.
    """
    pressed = [i for i in frets if i != 0 and i != -1]
    return len(pressed)

def rank_pitch(frets, chord, tuning, order):
    """
    This function prefers chords which are played lower on the fretboard.
    """
    return max(frets)

def rank_full(frets, chord, tuning, order):
    """
    Assesses how many notes from the chord were hit.
    Only returns meaningful input if variable 'important' is set low.
    """
    
    # make list of all notes played in the configuration
    n = len(frets)
    notes = []
    for i in range(n):
        if frets[i] != -1:
            notes.append((tuning[i] + frets[i]) % 12)
    
    return len(set(chord) - set(notes))

def rank_mute(frets, chord, tuning, order):
    """
    Disadvantages chords with muted strings.
    """
    count = 1
    for i in frets:
        if i == -1:
            count *= 2
    return count - 1

def rank_bass(frets, chord, tuning, order):
    """
    Assesses how well important notes in the chord have been placed on the
    low strings.
    """
    n = len(frets)
    
    # first make a list of notes played, with -1 still meaning mute.
    notes = []
    for i in range(n):
        if frets[i] == -1:
            notes.append(-1)
        else:
            notes.append((tuning[i] + frets[i]) % 12)
    
    # calculate how many muted strings there are
    m = 0
    for i in range(n):
        if frets[i] == -1:
            m = i + 1
    
    # re-rank the order of strings to remove muted ones. simply subtract
    # m from each entry in order.
    order_norm = [i - m for i in order]
    
    
    # now check each note in chord. Most heavily weighted is the bass.
    out = 0
    for i in range(len(chord)):
        if chord[i] in notes:
            # in this case, find all places where played
            places = []
            for j in range(n):
                if chord[i] == notes[j]:
                    places.append(j)
            
            # find the lowest string where played
            lowest = order_norm[min(places, key = lambda x : order_norm[x])]
            
            # add the distance away from ideal rank to out
            out += abs(i - lowest) / (2 ** i)
    
    # normalise by the number of non-muted strings
    return out / (len(frets) - m)

#  TODO doesn't work well with muted strings
    
rankfuncs = [rank_reach, rank_spread, rank_fingers, rank_pitch, rank_full, rank_mute, rank_bass]
