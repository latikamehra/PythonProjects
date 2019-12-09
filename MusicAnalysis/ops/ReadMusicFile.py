'''
Created on Aug 27, 2019

@author: latikamehra
'''

import matplotlib as mpl
import matplotlib.pyplot as plt
import librosa
import numpy
from librosa.display import waveplot



#plt.figure(figsize=(15,5))

songFile = "/Users/latikamehra/Music/Radiohead/STUDIO/FLACs/2003_Hail_To_The_Thief/09_There_There._The_Boney_King_Of_Nowhere..flac"

y, sr = librosa.load(songFile)#, duration=10)

#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

#beat_times = librosa.frames_to_time(beat_frames, sr=sr)

y_harmonic, y_percussive = librosa.effects.hpss(y)

print (y[50])

'''
mpl.rcParams['agg.path.chunksize'] = 100000
waveplot(y_harmonic,max_points=10000)

plt.show()
'''