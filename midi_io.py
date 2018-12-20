'''Reads a midi file.'''

__all__ = [
	'read',
]
__author__ = 'DavidM'

from music21 import *

from .note import Note

def read(path):
	'''Reads a midi file.'''
	file = converter.parse(path)
	tracks = []

	'''Struggling to deal with the inconsistency of music21.'''
	for track in file:
		curr = []
		for note in track:
			Note(note)

read('/Users/davidm/Desktop/SchoolProjects/ICT/Python/Melodicraft/Canon.mid')