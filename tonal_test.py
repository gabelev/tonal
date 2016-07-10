import unittest
import tonal
import mingus.core.notes

notes = mingus.core.notes
to = tonal.Tonal()

class TestTonal(unittest.TestCase):
    def test_scale_octave(self):
        self.assertEqual(12, to.scale(0, 1))
    def test_to_int(self):
        self.assertEqual(0, to.note_to_int("C"))
        self.assertEqual(11, notes.note_to_int("Cb"))
        with self.assertRaises(TypeError):
            to.note_to_int(0)
