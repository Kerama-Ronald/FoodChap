from sqlalchemy import create_engine

DATABASE_NAME = 'sqlite:///foodstuff.db'
engine = create_engine(DATABASE_NAME, echo = True)