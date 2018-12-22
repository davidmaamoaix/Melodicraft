'''The Note object.'''

__all__ = [
	'Note',
]
__author__ = 'DavidM'

class Note:
	'''Data structure for storing a note.'''

	def __init__(self, note):
		'''Initalize a Note

		note: int, a music21 instance of a note.
		'''
		self._note = 1
		self._startTick = 2

	@property
	def note(self):
		return self._note

	@note.setter
	def note(self, note):
		self._note = note

	@property
	def startTick(self):
		return self._startTick

	@startTick.setter
	def startTick(self, startTick):
		self._startTick = startTick