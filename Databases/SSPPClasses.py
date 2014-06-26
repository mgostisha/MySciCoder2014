#!/usr/bin/python

from DatabaseConnection import DatabaseConnection

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relation, exc, column_property, validates
from sqlalchemy import orm
from sqlalchemy.orm.session import Session

dbc = DatabaseConnection()
Base = declarative_base(bind=dbc.engine)

class Star(Base):
	__tablename__ = 'star'
	__table_args__ = {'autoload': True}