"""
Tell me what you are.
"""
import random

from scales import scale_names
import mingus.core.notes
import mingus.core.scales

notes = mingus.core.notes
scales = mingus.core.scales

notes_map = dict(C=0, D=2, E=4, F=5, G=7, A=9, B=11)

base_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# TODO: how to handle frequency? and Tempo?


class Tonal(object):
    def __init__(self, scale=None):
        self.scale = scale

    def note_to_int(self, note):
        if not isinstance(note, str) or len(note) != 1:
            raise TypeError
        else:
            return notes_map.get(note)

    def add_octave(self, note_int, scale):
        return note_int + scale * 12

    # This should either be random or determined. If random let's weight to the "normal" scales.
    # List of scales to be "seeds" to be used to generarate full note range.
    def pick_scale(self, scale=None):
        if not scale:
            return scale_names[random.randint(0, len(scale_names)-1)]
        else:
            return scale

    def pick_base_note(self):
        return notes.int_to_note(random.randint(0, 11))

    def create_scale_object(self):
        pass

    # takes a list of notes from scale and builds a [0-120] integer list that we can use to map to.
    def create_midi_note_range(self):
        pass
