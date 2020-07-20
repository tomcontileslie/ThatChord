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

# define the pressed helper function since it is used in several ranking funcs
def helper_pressed(frets, stringstarts):
    """
    returns a list of the frets that are pressed down.
    """
    out = []
    for i in range(len(frets)):
        # a string is pressed if it is not muted or open
        if not frets[i] <= stringstarts[i]:
            out.append(frets[i])
    return out

def helper_played(frets, stringstarts):
    """
    returns a list of frets that are played (not muted).
    """
    out = []
    for i in range(len(frets)):
        if not frets[i] < stringstarts[i]:
            out.append(frets[i])
    return out

def rank_reach(frets, chord, tuning, order, stringstarts):
    """
    Returns the distance between the highest and lowest fret that needs
    to be pressed when playing the chord
    """
    pressed = helper_pressed(frets, stringstarts)
    if len(pressed) == 0:
        return 0
    else:
        return (max(pressed) - min(pressed))

def rank_spread(frets, chord, tuning, order, stringstarts):
    """
    Similar to reach, but includes empty strings as well, in order to measure
    how 'spread out' the chord sounds.
    """
    played = helper_played(frets, stringstarts)
    if len(played) == 0:
        return 0
    else:
        return max(played) - min(played)

def rank_fingers(frets, chord, tuning, order, stringstarts):
    """
    Returns the 'number of figners needed to play the chord', i.e. number
    of strings that are pressed.
    """
    return len(helper_played(frets, stringstarts))

def rank_pitch_hi(frets, chord, tuning, order, stringstarts):
    """
    This function prefers chords which are played lower on the fretboard.
    """
    return max(frets)

def rank_pitch_lo(frets, chord, tuning, order, stringstarts):
    """
    This function prefers chords which are played lower on the fretboard.
    """
    return min(helper_played(frets, stringstarts))

def rank_full(frets, chord, tuning, order, stringstarts):
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

def rank_mute(frets, chord, tuning, order, stringstarts):
    """
    Disadvantages chords with muted strings.
    """
    count = 1
    for i in range(len(frets)):
        if frets[i] < stringstarts[i]:
            count *= 2
    return count - 1

def rank_structure(frets, chord, tuning, order, stringstarts):
    """
    Assesses how well important notes in the chord have been placed on the
    low strings.
    """
    n = len(frets)
    
    # first make a list of notes played, with -1 still meaning mute.
    notes = []
    for i in range(n):
        if frets[i] < stringstarts[i]:
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

def rank_bass(frets, chord, tuning, order, stringstarts):
    """
    Penalises chords where the note played on the lowest string is not the bass
    """
    n         = len(frets)
    
    # ordernew changes order to remove muted strings
    bignum = max(order) + 1
    ordernew = []
    for i in range(n):
        if frets[i] < stringstarts[i]:
            ordernew.append(bignum)
        else:
            ordernew.append(order[i])
    
    # lowest played string has min value in ordernew.
    loword = min(ordernew)
    lowstr = ordernew.index(loword)
    
    # find note played on this string
    lownot = (frets[lowstr] + tuning[lowstr]) % 12
    
    # return 0 iff note is the lowest note in chord.
    if lownot == chord[0]:
        return 0
    else:
        return 1

# TODO safeguard against every string muted
    
rankfuncs = [rank_reach,       \
             rank_spread,      \
             rank_fingers,     \
             rank_pitch_hi,    \
             rank_pitch_lo,    \
             rank_full,        \
             rank_mute,        \
             rank_structure,   \
             rank_bass]

# define main rank function. "ranks" is list of coeffs.
def rank(frets, chord, tuning, order, ranks, stringstarts):
    return sum([ranks[i] * rankfuncs[i](frets, chord, tuning, order, stringstarts) \
                for i in range(len(rankfuncs))])
