#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from model_state import Base
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.orm import sessionmaker
    import sys

    user_name = sys.argv[1]
    user_password = sys.argv[2]
    db_name = sys.argv[3]

    url_object = URL.create(
        "mysql",
        username=user_name,
        password=user_password,
        host="localhost",
        port=3306,
        database=db_name
    )

    engine = create_engine(url_object)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a'))

    if states:
        for state in states:
            session.delete(state)

    session.commit()

    session.close()
