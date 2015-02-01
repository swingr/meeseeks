from pydub import AudioSegment
from pydub.playback import play

def start():
    song = AudioSegment.from_wav("audio/beginning.wav")
    play(song)

def shoulders():
    song = AudioSegment.from_wav("audio/shoulders.wav")
    play(song)

def choke():
    song = AudioSegment.from_wav("audio/choke.wav")
    play(song)

def existence():
    song = AudioSegment.from_wav("audio/existance.wav")
    play(song)

def frustrating():
    song = AudioSegment.from_wav("audio/frustrating.wav")
    play(song)

def head():
    song = AudioSegment.from_wav("audio/head.wav")
    play(song)
