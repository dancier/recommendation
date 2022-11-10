from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import Config

engine = create_engine(
    'postgresql://{user}:{passw}@{host}/{db_name}'.format(
        user = Config.DB_USER,
        passw = Config.DB_PASS,
        host = Config.DB_HOST,
        db_name = Config.DB_NAME
     ),
    echo=False,
    future=True
)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine,
                                         future=True))

Base = declarative_base()
Base.query = db_session.query_property()
