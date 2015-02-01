from pydub import AudioSegment
from pydub.playback import play
from os import path

_AUDIO_DIR = path.join(path.dirname(__file__), '')

def _format(sound_file):
    return "{0}{1}".format(_AUDIO_DIR, sound_file)

def start():
    song = AudioSegment.from_wav(_format("beginning.wav"))
    play(song)

def shoulders():
    song = AudioSegment.from_wav(_format("shoulders.wav"))
    play(song)

def choke():
    song = AudioSegment.from_wav(_format("choke.wav"))
    play(song)

def existence():
    song = AudioSegment.from_wav(_format("existence.wav"))
    play(song)

def frustrating():
    song = AudioSegment.from_wav(_format("frustrating.wav"))
    play(song)

def head():
    song = AudioSegment.from_wav(_format("head.wav"))
    play(song)
