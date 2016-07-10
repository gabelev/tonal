import unittest
from tonal import scale_octave


class TestTonal(unittest.TestCase):
    def test_scale_octave(self):
        self.assertEqual(12, scale_octave(0, 1))
