# Machine Music

Machine Music is a collection of scripts and Classes that transforms time-series data streams into compositional elements
and understandable sonic components. It was basis for a talk I gave at [PyGotham 2016](https://2016.pygotham.org/talks/311/the-sound-of-data-using-p/) at the UN in NYC.

In it's current state, Machine Music queries a weather api for the following points of data:

    - temp
    - apparent temperature
    - dew
    - humidity
    - visibility
    - ozone=
    - windBearing

And then translates that live streaming data into midi formatted notes which can be feed into your favorite music
software (I use [Ableton Live](https://help.ableton.com/hc/en-us/articles/209774225-Using-virtual-MIDI-buses-in-Live)).
I've included the Ableton live project as a starting point.

It can be pointed to any data source and any midi receptive output.

I also included datadog metrics as a rudimentary means of visualizing the data as we hear it.

## Motivation 

Machine Music aims at making complex time-series data more understandable by providing an alternate approach to
abstracting and representing numerical data via [audiation.](https://en.wikipedia.org/wiki/Gordon_music_learning_theory#Audiation)


