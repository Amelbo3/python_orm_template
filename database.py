from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base


# create session
engine = create_engine('sqlite:///sampleDB.db') # Use your database URL
Base.metadata.create_all(engine) # Creates tables if they don't exist
Session = sessionmaker(bind=engine)
session = Session()