'''The Note object.'''

__all__ = [
	'Note',
]
__author__ = 'DavidM'

class Note:

	def __init__(self, note):
		'''Initalize a Note

		note: int, a music21 instance of a note.
		'''
		self._note = 1
		self._duration = 2

	@property
	def note(self):
		return self._note

	@note.setter
	def note(self, note):
		self._note = note

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, duration):
		self._duration = duration