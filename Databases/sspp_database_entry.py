import sys
import numpy
import fitsio
import sqlalchemy
from SSPP_SQLiteConnection import engine, Session
from SSPPClasses import Star


filename = 'ssppOut-dr9.fits'
fits = fitsio.FITS(filename)
colnames = fits[1].get_colnames()

data = fitsio.read(filename, rows=1)
typearr = data.dtype

session = Session()
session.begin() 

for count, row in enumerate(fits[1]):

	newStar = Star()

	for idx, col in enumerate(colnames):

		datatype = typearr[idx].kind
		value = row[idx]

		if datatype == 'i':
			value = long(value)
		
		setattr(newStar, col.lower(), value)

	session.add(newStar)

	if count % 10000 == 0:
		print 'Committing: {0}'.format(count)
		session.commit()
		session.begin()
		print 'Committed: {0}!'.format(count)

session.commit()

engine.dispose()
sys.exit(0)


