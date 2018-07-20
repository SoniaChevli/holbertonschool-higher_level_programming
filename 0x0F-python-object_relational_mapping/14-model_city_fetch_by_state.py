#!/usr/bin/python3
"""
prints all City objects from database
"""
if __name__ == '__main__':
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    connection = engine.connect()
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    both = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in both:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
