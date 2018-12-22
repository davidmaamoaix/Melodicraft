'''Reads a midi file.'''

__all__ = [
	'read',
]
__author__ = 'DavidM'

from music21 import *

from note import Note

def read(path: str) -> list:
	'''Reads a midi file.
	Outputs a list of tracks, which contain sequences of notes.
	'''
	file = converter.parse(path)
	tracks = []

	'''Struggling to deal with the inconsistency of music21.'''
	for track in file:
		curr = []
		for element in track:

			'''A single note is treated as a chord with one element.'''
			if type(element) == note.Note:
				curr.append([Note(element)])

			if type(element) == chord.Chord:
				curr.append([Note(i) for i in element])

read('/Users/davidm/Desktop/SchoolProjects/ICT/Python/Melodicraft/Canon.mid')