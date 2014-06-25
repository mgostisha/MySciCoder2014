import sys
import time
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *

#---------------------------------------------
# Define the file to be read and open the file
#---------------------------------------------
filename = 'student_data.txt'
student_data = open(filename, 'r')

#----------------------
# Start the SQL Session
#----------------------
session = Session()

#--------------------------------------
# Read the N header lines from the file
#--------------------------------------
n_header = 5
for i in range(n_header):
	student_data.readline()
#-------------------------------------------------------
# Read each line form the file and populate the database
#-------------------------------------------------------
for line in student_data:
	line = line.strip().split('|')
	print "---------------------------"

	#---------------------------------------------------------------
	# Start a new object for each student, add data fields to object
	#---------------------------------------------------------------
	newStudent = Student()
	newStudent.first_name = str(line[0])
	newStudent.last_name = str(line[1])
	session.add(newStudent)
	print "Name: {0}, {1}".format(line[1], line[0])

	#----------------------------------------------------------------------
	# Check to see if the city the student is from is already in the db
	# If it's not, create the new city object, point it towards the student
	# And add it to the db
	#----------------------------------------------------------------------
	try:
		one_city = session.query(City).filter(City.label==str(line[2])).one()
	except sqlalchemy.orm.exc.NoResultFound:
		one_city = City()
		one_city.label = str(line[2])
		session.add(one_city)

	newStudent.city = (one_city)

	#----------------------------------------------------
	# Split up the supervisors if there are more than one
	#----------------------------------------------------
	supline = line[3].split(', ')

	#----------------------------------------------------------------------
	# Check to see if the supervisor and their room number are in the db
	# If they aren't, create the new supervisor object, point it towards
	# The student object, and add it to the db
	#----------------------------------------------------------------------
	for sup in supline:
		if sup != '':
			sup = sup.split('/')
			try:
				one_supervisor = session.query(Supervisor).filter(Supervisor.last_name==str(sup[0]))\
														  .filter(Supervisor.room_number==str(sup[1])).one()
			except sqlalchemy.orm.exc.NoResultFound:
				one_supervisor = Supervisor()
				one_supervisor.last_name = str(sup[0])
				one_supervisor.room_number = str(sup[1])
				session.add(one_supervisor)
	
			newStudent.supervisors.append(one_supervisor)

	#----------------------------------------------------------------------
	# Check to see if the status is already in the DB. If it isn't, create
	# The new status object, point it towards the student, and add it to
	# The DB
	#----------------------------------------------------------------------
	try:
		one_status = session.query(Status).filter(Status.label==str(line[4])).one()
	except sqlalchemy.orm.exc.NoResultFound:
		one_status = Status()
		one_status.label = str(line[4])
		session.add(one_status)
	
	newStudent.status = (one_status)

	#-------------------------------------------
	# Split the clubs if there are more than one
	#-------------------------------------------
	clubline = line[5].strip().split(', ')

	#----------------------------------------------------------------------
	# Check to see if the club is already in the db. If it's not, create
	# The new club object, point it towards the student, and add it to the
	# DB
	#----------------------------------------------------------------------
	for club in clubline:
		if club != '':
			try:
				one_club = session.query(Club).filter(Club.label==str(club)).one()
			except sqlalchemy.orm.exc.NoResultFound:
				one_club = Club()
				one_club.label = str(club)
			session.add(one_club)

#--------------------------------------------------
# Commit the changes to the the database as a whole
#--------------------------------------------------
session.commit()

#-----------------------------------------
# Close the engine cleanly and exit python
#-----------------------------------------
engine.dispose()
sys.exit(0)

