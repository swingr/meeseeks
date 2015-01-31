from pydub import AudioSegment
from pydub.playback import play

def start():
	song = AudioSegment.from_mp3("audio/beginning.mp3")
	play(song)

def shoulders():
	song = AudioSegment.from_mp3("audio/shoulders.mp3")
	play(song)

def choke():
	song = AudioSegment.from_mp3("audio/choke.mp3")
	play(song)

def existance():
	song = AudioSegment.from_mp3("audio/existance.mp3")
	play(song)

def frustrating():
	song = AudioSegment.from_mp3("audio/frustrating.mp3")
	play(song)

def head():
	song = AudioSegment.from_mp3("audio/head.mp3")
	play(song)
