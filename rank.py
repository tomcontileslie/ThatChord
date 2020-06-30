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

def rank_reach(frets):
    """
    Returns the distance between the highest and lowest fret that needs
    to be pressed when playing the chord
    """
    pressed = [i for i in frets if i != 0 and i != -1]
    if len(pressed) == 0:
        return 0
    else:
        return (max(pressed) - min(pressed)) ** 2

def rank_spread(frets):
    """
    Similar to reach, but includes empty strings as well, in order to measure
    how 'spread out' the chord sounds.
    """
    played = [i for i in frets if i != -1]
    if len(played) == 0:
        return 0
    else:
        return max(played) - min(played)

def rank_fingers(frets):
    """
    Returns the 'number of figners needed to play the chord', i.e. number
    of strings that are pressed.
    """
    pressed = [i for i in frets if i != 0 and i != 1]
    return len(pressed) ** 2

def rank_pitch(frets):
    """
    This function prefers chords which are played lower on the fretboard.
    """
    return max(frets)

def rank_full(frets, chord, tuning):
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
    
    return len(set(chord) - set(frets))

def rank_mute(frets):
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
    
    #print("notes = ", notes)
    
    # calculate how many muted strings there are
    m = 0
    for i in range(n):
        if frets[i] == -1:
            m = i + 1
    #print("m =", m)
    
    # re-rank the order of strings to remove muted ones. simply subtract
    # m from each entry in order.
    order_norm = [i - m for i in order]
    
    #print("order_norm = ", order_norm)
    
    
    # now check each note in chord. Most heavily weighted is the bass.
    out = 0
    for i in range(len(chord)):
        #print("")
        #print("checking note ", i, ": ", chord[i])
        if chord[i] in notes:
            #print("it is indeed played")
            # in this case, find all places where played
            places = []
            for j in range(n):
                if chord[i] == notes[j]:
                    places.append(j)
            #print("in these places: ", places)
            
            # find the lowest string where played
            lowest = order_norm[min(places, key = lambda x : order_norm[x])]
            #print("the lowest string of which has rank ", lowest)
            
            # add the distance away from ideal rank to out
            out += abs(i - lowest) / (2 ** i)
            #print("out is now ", out)
    
    # normalise by the number of non-muted strings
    return out / (len(frets) - m)

#  TODO doesn't work well with muted strings




















