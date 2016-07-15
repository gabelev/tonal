"""Tell me what you are."""

import random

from scales import scale_names, TonalScales
import mingus.core.notes
import mingus.core.scales

notes = mingus.core.notes
scales = mingus.core.scales
ts = TonalScales()

notes_map = dict(C=0, D=2, E=4, F=5, G=7, A=9, B=11)

base_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# TODO: how to handle frequency? and Tempo?


class Tonal(object):

    """Let me tell you what I am."""

    def __init__(self, scale=None):
        """Let me tell you what I am."""
        self.scale = scale

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

    def create_scale_object(self, scale=None):
        """Let me tell you what I am."""
        if not scale:
            return ts.select_scale(self.pick_scale())
        else:
            pass

    # takes a list of notes from scale and builds a [0-120] integer
    # list that we can use to map to.
    def create_midi_note_range(self):
        """Let me tell you what I am."""
        pass
