from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from pgvector.sqlalchemy import Vector
from .utils import EnvVars



def get_connection_string():
  DB_USERNAME = EnvVars.get('DB_USERNAME')
  DB_PASSWORD = EnvVars.get('DB_PASSWORD')
  DB_HOST = EnvVars.get('DB_HOST')
  DB_PORT = EnvVars.get('DB_PORT')
  DB_NAME = EnvVars.get('DB_NAME')
  return f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    

class BasicDatabase:
  def __init__(self, reqd_tables):
    self.engine = create_engine(get_connection_string())
    self.Session = sessionmaker(bind=self.engine)
    self.get_existing_tables(reqd_tables)
  
  def get_existing_tables(self, reqd_tables):
    metadata = MetaData()
    metadata.reflect(bind=self.engine)
    AutomapBase = automap_base(metadata=metadata)
    AutomapBase.prepare()
    for tablename, classname in reqd_tables.items():
      self.__setattr__(classname, AutomapBase.classes[tablename])