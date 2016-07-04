"""
import mido
import time

out = mido.open_output()
for x in range(0, 100):
    output.send(mido.Message('note_on', note=60, velocity=64))
    time.sleep(0)

"""

import mido
import time


