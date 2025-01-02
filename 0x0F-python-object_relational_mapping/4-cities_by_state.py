#!/usr/bin/python3
"""
This script connects to a MySQL database and lists all cities from the database
'hbtn_0e_4_usa'. It retrieves and sorts cities by their ID in ascending order
using SQLAlchemy ORM, ensuring the cities are displayed with their respective
state names.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Define the Base class
Base = declarative_base()

# Define the State class
class State(Base):
    """
    Represents the 'states' table in the database.

    Attributes:
        id (int): The unique identifier of the state.
        name (str): The name of the state.
        cities (relationship): A relationship to the cities in this state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    cities = relationship('City', backref='state')

# Define the City class
class City(Base):
    """
    Represents the 'cities' table in the database.

    Attributes:
        id (int): The unique identifier of the city.
        name (str): The name of the city.
        state_id (int): The foreign key to the state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

def list_cities(username, password, db_name):
    """
    Connects to the MySQL database and lists cities from the 'cities' table,
    sorted by their id in ascending order.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): The name of the database.

    Returns:
        None
    """
    # Create a connection string
    connection_string = f"mysql+mysqldb://{username}:{password}@localhost/{db_name}"
    
    # Create the engine to interact with the MySQL database
    engine = create_engine(connection_string)

    # Create the session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get cities with their respective state names, ordered by city id
    cities = session.query(City.id, City.name, State.name).join(State).order_by(City.id).all()

    # Display the results
    for city in cities:
        print(city)

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        # Extract arguments from the command line
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        # Call the function to list cities
        list_cities(username, password, db_name)
    else:
        print("Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>")

