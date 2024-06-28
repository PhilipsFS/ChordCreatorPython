import music21 as ms
import librosa as lr



def cp(rn_in):  # cp = chord pitches
    # Get pitches
    return [str(p) for p in rn_in.pitches]

progression = ['I', 'IV', 'vi', 'V']

for prog in progression:
    chrd = ms.roman.RomanNumeral(prog, 'C')
    print(cp(chrd))



