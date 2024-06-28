
import scales_chords as sc
from mingus.core import chords
from mingus.containers import Bar, Track
from mingus.midi import midi_file_out
from mingus.containers import NoteContainer
from midiutil import MIDIFile
import pprint
import re

t = Track()
t_chords = Track()
notes_t = []

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A#', 'C#', 'D#', 'F#', 'G#']  #sc.alphabet
nc = NoteContainer()
oct = 4
scale_oct =[]
chordList = []
chords = []
j = 0 

for key in alphabet:
    listNotes = sc.chromatic(key)
    chordRomans = ['', 'm', 'm', '', '', 'm', 'dim', '']
    formula = 'P1,M2,M3,P4,P5,M6,M7,P8' # Major Scale
    scale = sc.make_formula(formula, sc.make_intervals_standard(key))

    #print(scale)
    # for i in range(len(scale)):
    #     if i != 7:
    #         if scale[i] == ('A'):
    #             #print(scale[i])
    #             scale_oct.append(scale[i] + '-' + str(oct-1))
    #         elif scale[i] == ('B'):
    #             #print(scale[i])
    #             scale_oct.append(scale[i] + '-' + str(oct-1))
    #         else:
    #             #print('Should be 4', scale[i], oct)
    #             scale_oct.append(scale[i] + '-' + str(oct))
    #     else:
    #         #print('Should be 4', scale[i], oct)
    #         scale_oct.append(scale[i] + '-' + str(oct))
    
    
    for i, note in enumerate(scale):
        #t.add_notes(scale_oct[i])
        scale[i] = note + chordRomans[i]
    scale_oct = []
    t.from_chords(scale, 1)
    t_chords.from_chords(scale, 1)

    for i in range(j, j + 8):
        chordList += t_chords[i][0][2:4]

    prt = []
    print(key, 'Chord List')
    for i in range(8):
        prt = list(chordList[i][:])
        #for i in range(3):
        #    prt[1].replace('-4', '')
        print(*prt[:], '\n')   
    chordList = []
    #print(chordList)
    j += 8             
    

midi_file_out.write_Track("test.mid", t)

'''chordList = []
for i in range(8):
    chordList += t_chords[i][0][2:4]

prt = []
print(key, 'Chord List')
for i in range(8):
    #prt = str(chordList[i][:]).replace('-4', '')
    prt = chordList[i][:]

    print(*prt[:], '\n')
'''

def dump(scale, separator=' '):
    '''
    Pretty-print the notes of a scale. Replaces b and # characters
    for unicode flat and sharp symbols.
    '''
    return separator.join(['{:<3s}'.format(x) for x in scale]) \
                    .replace('b', '\u266d') \
                    .replace('#', '\u266f')

