#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 03:30:51 2019

@author: Chanemougam
"""


## Librairies #
import matplotlib.pyplot as plt
import numpy as np
#from scipy.misc.doccer import (extend_notes_in_docstring,
 #                              replace_notes_in_docstring)
import librosa as lbr


## Loading and visualizing Data ##

##path to my audio file
path = "../DataTrain/CrowdsourcedR/wav"

file = lbr.util.example_audio_file()
y, sr = lbr.load(file)
#Audio(data='y', rate='sr')
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
