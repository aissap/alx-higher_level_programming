#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    existing_state = session.query(State).filter(State.name == 'Louisiana').first()

    if existing_state:
        print(existing_state.id)
    else:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()

        print(new_state.id)

    session.close()
