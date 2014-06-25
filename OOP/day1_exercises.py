#!/usr/bin/env python

import numpy

def table2dict():
	''' Open data table and write to a dictionary, where the first
	line of the data file contains the keys to be used. '''

	filename = '/Users/Martin/Repos/SciCoder2014/Data/table.txt'
	datadict = {}

	datatable = open(filename, 'r')
	header = datatable.readline().split(',')

	for key in header:
		datadict[key] = []

	for line in datatable:
		vals = line.strip().split(',')
		print range(len(vals))

		for i in range(len(vals)):
			datadict[header[i]].append(vals[i])

	datatable.close()

	return datadict

class GettyAddy(object):

	def __init__(self):
		self.filename = '/Users/Martin/Repos/SciCoder2014/Data/gettysburg_address.txt'

	def readFile(self):
		''' Reads the above file, counts the number of line and the number
		of words in the file and prints these stats to the user. '''

		self.linecount = 0
		self.wordcount = 0
		self.wordarr = []

		with open(self.filename, 'r') as datafile:
			for line in datafile:

				linearr = line.strip().split()
				self.linecount += 1
				self.wordcount += len(linearr)

				for item in linearr:
					self.wordarr.append(item)

		print "Number of lines: {0}\nNumber of words: {1}".format(str(self.linecount), str(self.wordcount))

	def sortWords(self):
		''' Strips the word array of any duplicates and creates an array of
		alphabetically sorted unique words in the address. '''
		
		self.sorted_arr = []

		for word in self.wordarr:
			if word.lower() not in self.sorted_arr:
				self.sorted_arr.append(word.lower())

		self.sorted_arr.sort()

	def vowelCounts(self):
		''' Takes the word array without duplicates stripped and calculates the Number
		of each vowel is included in the address. '''

		vowel_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}

		for word in self.wordarr:
			for char in word.lower():
				if char in vowel_dict.keys():
					vowel_dict[char] += 1

		print 'Number of each vowel in the Gettysburg Address:\na: {0}\ne: {1}\ni: {2}\no: {3}\n\
u: {4}\ny: {5}'.format(str(vowel_dict['a']), str(vowel_dict['e']), str(vowel_dict['i']), \
		str(vowel_dict['o']), str(vowel_dict['u']), str(vowel_dict['y']))


