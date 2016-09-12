"""Tell me what you are."""

import random

from scales import scale_names, TonalScale
import mingus.core.notes as notes

ts = TonalScale()

notes_map = dict(C=0, D=2, E=4, F=5, G=7, A=9, B=11)

base_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


class Tonal(object):

    """Let me tell you what I am."""

    def __init__(self):
        """Let me tell you what I am."""
        return

    def note_to_int(self, note):
        """Let me tell you what I am."""
        if not isinstance(note, str) or len(note) != 1:
            raise TypeError
        else:
            return notes_map.get(note)

    def add_octave(self, note_int, scale):
        """Let me tell you what I am."""
        return note_int + scale * 12

    # This should either be random or determined.
    # If random let's weight to the "normal" scales.
    # List of scales to be "seeds" to be used to generarate full note range.
    def pick_scale(self, scale=None):
        """Let me tell you what I am."""
        if not scale:
            return scale_names[random.randint(0, len(scale_names)-1)]
        else:
            return scale

    def pick_base_note(self):
        """Let me tell you what I am."""
        return notes.int_to_note(random.randint(0, 11))

    def create_scale_object(self, scale=None, base_note='C'):
        """Let me tell you what I am."""
        if not scale:
            return ts.select_scale(self.pick_scale())
        else:
            return ts.select_scale(scale, base_note)

    # takes a list of notes from scale and builds a [0-120] integer
    # list that we can use to map to.
    def create_midi_note_range(self, scale, base_note):
        """Let me tell you what I am."""
        beginning_scale = ts.select_scale(scale, base_note).ascending()
        begin_midi = [notes.note_to_int(note) for note in beginning_scale]
        midi_range = [note for note in begin_midi]
        for item in begin_midi:
            for x in range(16):
                new = self.add_octave(item, x)
                if new <= 120:
                    midi_range.append(new)
        return midi_range

    def create_sorted_midi(self, scale, base):
        """Let me tell you what I am."""
        midi = set(self.create_midi_note_range(scale, base))
        return sorted(midi)


def mapping(value, midi):
    """The object maps values to notes."""
    if value >= 120:
        return mapping(value % 10, midi)
    if value < 0:
        return mapping(int(value * 10), midi)
    for item in midi:
        if item == value:
            return value
        if item > value:
            return item
