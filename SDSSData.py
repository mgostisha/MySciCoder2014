import numpy
import urllib2

def SpectrumSearch(**kwargs):

	base_string = "api.sdss3.org/spectrumQuery?"
	accepted_keys = ['class', 'redshift', 'limit']
	add_strings = []

	for key in kwargs.keys():
		if key in accepted_keys:
			if key == 'class':
				class_string = 'class={0}'.format(kwargs[key])
				add_strings.append(class_string)
			if key == 'redshift':
				redshift_string = 'redshift={0}[0]-{0}[1]'.format(kwargs[key])
				add_strings.append(redshift_string)
			if key == 'limit':
				limit_string = 'limit={0}'.format(kwargs[key])
				add_strings.append(limit_string)

	for string in add_strings:
		base_string += (string + '&')

	base_string = base_string[:-1]
	print base_string

#	results = urllib2.Requests(base_string)
#	return results
