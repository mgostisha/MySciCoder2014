#!/usr/bin/python

import sys
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *

filename = 'student_data.txt'

data = open(filename)

session = Session()

student = Student()
student.first_name = "Amelia"
student.last_name = "Pond"
session.add(student)

try:
	one_supervisor = session.query(Supervisor).filter(Supervisor.last_name=='Tennant') \
											  .filter(Supervisor.first_name=='David').one()
except sqlalchemy.orm.exc.NoResultFound:
	one_supervisor = Supervisor()
	one_supervisor.last_name = "Tennant"
	one_supervisor.first_name = "David"
	session.add(one_supervisor)
except sqlalchemy.orm.exc.MultipleResultsFound:
	print "There is more than one Doctor!"
	sys.exit(1)
	
student.supervisors.append(one_supervisor)

	

session.commit()

engine.dispose() # cleanly disconnect from the database
sys.exit(0)
