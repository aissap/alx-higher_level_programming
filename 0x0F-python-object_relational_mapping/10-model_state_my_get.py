#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    if len(argv) == 5:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        state_to_search = argv[4]
        result_state = session.query(State).filter(State.name == state_to_search).first()

        if result_state:
            print(result_state.id)
        else:
            print("Not found")

        session.close()
    else:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)
