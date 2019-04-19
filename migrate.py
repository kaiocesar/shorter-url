from sqlalchemy import create_engine, Column, Table, String, MetaData, Integer

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()

url = Table('urls', metadata,
    Column('id', Integer, primary_key=True),
    Column('hash', String)
)

metadata.create_all(engine)
