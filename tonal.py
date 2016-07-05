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
import random

output = mido.open_output()

for x in range(0, 1000):
    note=random.randint(0, 120)
    vel=random.randint(40,100)
    output.send(mido.Message('note_on', note=note, velocity=vel))
    print(note, vel)
    time.sleep(4)
    output.send(mido.Message('note_off', note=note, velocity=vel))
    time.sleep(1)
