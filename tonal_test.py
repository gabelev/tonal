"""This is a Test."""

import unittest
import tonal
import mingus.core.notes
from scales import scale_names, TonalScale
import mingus.core.scales as scales

notes = mingus.core.notes
to = tonal.Tonal()
ts = TonalScale()


class TestTonal(unittest.TestCase):

    """Tell me something."""

    def test_scale_octave(self):
        """Test."""
        self.assertEqual(12, to.add_octave(0, 1))

    def test_to_int(self):
        """Test."""
        self.assertEqual(0, to.note_to_int("C"))
        self.assertEqual(11, notes.note_to_int("Cb"))
        with self.assertRaises(TypeError):
            to.note_to_int(0)

    def test_pick_scale(self):
        """Test."""
        self.assertIsNotNone(to.pick_scale())
        self.assertIn(to.pick_scale(), scale_names)

    def test_pick_base_note(self):
        """Test."""
        self.assertIn(notes.note_to_int(to.pick_base_note()), range(0, 13))


class TestScales(unittest.TestCase):

    """Test."""

    def test_select_scale(self):
        """Test."""
        self.assertIsInstance(
            ts.select_scale("HarmonicMajor", "C"),
            scales.HarmonicMajor
        )
