#!/usr/bin/python

"""Tell me what I am."""

import mido
import time
import requests
import sys

from datadog import statsd

from tonal import Tonal, mapping

output = mido.open_output()
to = Tonal()


arg1 = sys.argv[1]
arg2 = sys.argv[2]
if arg1 is None:
    mid_range = to.create_sorted_midi("HarmonicMajor", "C")
else:
    mid_range = to.create_sorted_midi(str(arg1), str(arg2))


API_KEY = "3029dd3b274c8f534b16d89a14db6118"
GEO = "40.712784,-74.005941"
call = "https://api.forecast.io/forecast/{0}/{1}"

weather = call.format(API_KEY, GEO)

start = time.time()
max_time = 100

values = dict()
old_values = dict()

chans = dict(
    temp=1,
    app_temp=2,
    dew=3,
    humidity=4,
    visibility=5,
    ozone=6,
)


def get_info():
    """Get data."""
    hourly = []
    r = requests.get(weather)
    for i in range(len(r.json()["hourly"]["data"])):
        hourly.append(r.json()["hourly"]["data"][i])
    return hourly


def parse(record):
    """Get data."""
    values.update(temp=record["temperature"])
    values.update(
        app_temp=record["apparentTemperature"])
    values.update(dew=record["dewPoint"])
    values.update(humidity=record["humidity"] * 100)
    values.update(visibility=record["visibility"] * 10)
    values.update(ozone=record["ozone"])

keys = ["temperature", "apparentTemperature", "dewPoint", "humidity",
        "visibility", "ozone"]

if __name__ == "__main__":

    while True:
        data = get_info()
        for item in data:
            parse(item)
            for key, value in values.iteritems():
                chan = chans.get(key)
                try:
                    output.send(mido.Message(
                        'note_on',
                        note=mapping(value, mid_range),
                        velocity=50,
                        channel=chan))
                except:
                    print("error")
                    pass
                time.sleep(1)
                print(key, value, "channel:", chan)
                statsd.gauge(key, value)
        for item in data:
            parse(item)
            for key, value in values.iteritems():
                chan = chans.get(key)
                try:
                    output.send(mido.Message(
                        'note_off',
                        note=mapping(value, mid_range),
                        channel=chan))
                except:
                    print("error")
                    pass
                time.sleep(1)
                print(key, value, "channel:", chan)
