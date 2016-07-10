"""
Tell me what you are.
"""

notes = dict(C=0, D=2, E=4, F=5, G=7, A=9, B=11)


def scale_octave(note_int, scale):
    return note_int + scale * 12
