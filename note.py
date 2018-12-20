'''The Note object.'''

__all__ = [
	'Note',
]
__author__ = 'DavidM'

class Note:

	self._note = None
	self._duration = None

	def __init__(self, note):
		'''Initalize a Note

		note: int, a music21 instance of a note.
		'''
		print(note.pitch)
		#self._note = note
		#self._duration = duration

	@property
	def note(self):
		return self._note

	@_note.setter
	def note(self, note):
		self._note = note

	@property
	def duration(self):
		return self._duration

	@_duration.setter
	def duration(self, duration):
		self._duration = duration