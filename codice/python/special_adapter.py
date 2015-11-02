#!/usr/bin/python3
__author__ = 'paranoia'


class Adapter(object):

	def __init__(self, obj, adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

	# def original_dict(self):
		# return self.obj.__dict__
