#!/usr/bin/python3
"""
adds the State object "Louisiana" to database
"""
if __name__ == '__main__':
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    connection = engine.connect()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print('{}'.format(new.id))
    session.close()
