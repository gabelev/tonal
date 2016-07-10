import unittest
import tonal

to = tonal.Tonal()

class TestTonal(unittest.TestCase):
    def test_scale_octave(self):
        self.assertEqual(12, to.scale(0, 1))
