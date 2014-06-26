import sys
import numpy
import fitsio

init_string = "DROP TABLE IF EXISTS 'star';\n"
init_string += "CREATE TABLE 'star' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE"
infilename = 'ssppOut-dr9.fits'

fits = fitsio.FITS(infilename)
colnames = fits[1].get_colnames()

data = fitsio.read(infilename, rows=1)
typearr = data.dtype

for idx, name in enumerate(colnames):

	datatype = typearr[idx].kind

	if datatype == 'S':
		data_string = 'TEXT'
	elif datatype == 'i':
		data_string = 'BIGINT'
	elif datatype == 'f':
		data_string = 'FLOAT'

	add_string = ", '{0}' {1}".format(name.lower(), data_string)

	init_string += add_string

init_string += ');'

outfilename = 'sspp_db.sql'
sqlfile = open(outfilename, 'w')

sqlfile.write(init_string)
sqlfile.close()
sys.exit(0)