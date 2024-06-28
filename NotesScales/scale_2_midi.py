import scales_chords as sc
from mingus.core import chords
from midiutil import MIDIFile
import random

print(sc.alphabet)
print(sc.formulas.keys())
print(sc.formulas['scales']['minor'])
print(sc.make_formula(sc.formulas['scales']['major'], 
                      sc.make_intervals('C', 'major')))

#print(sc.make_intervals('C','major'))

array_of_notes = sc.make_formula(sc.formulas['scales']['major'], 
                                 sc.make_intervals('C', 'major'))

array_of_note_numbers = []

for note in array_of_notes:
    OCTAVE = 5
    array_of_note_numbers.append(sc.note_to_number(note, OCTAVE))

print(array_of_note_numbers)

# write out midi
track = 0
channel = 0
time = 0  # In beats
length = 4
duration = 1/length  # In beats
tempo = 120  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
# automatically)
MyMIDI.addTempo(track, time, tempo)

"""for i, pitch in enumerate(array_of_note_numbers):
    MyMIDI.addNote(track, channel, pitch, time + i/length, duration, volume)

with open("C_major_scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
"""

lengthList = [1, 2, 4, 8]

noteList = sc.alphabet

for note in noteList:
    OCTAVE = 5
    array_of_note_numbers.append(sc.note_to_number(note, OCTAVE))

lengthList = [0.5, 1, 2, 4, 8]


for i in range(501):
    randLength = random.choices(lengthList, weights=(30, 40, 50, 50, 5))
    noteLength = randLength[0]
    print('noteLemgth: ', noteLength)
    randPitch = random.choices(array_of_note_numbers)
    print('Pitch: ', randPitch[0])
    print('i: ', i)
    MyMIDI.addNote(track, channel, randPitch[0], 
                   time, 1/noteLength, volume)
    time = time + 1/noteLength
with open("C_30_notes.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

