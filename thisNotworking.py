from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbnb_dev_db')
meta = MetaData(bind=engine)
meta.reflect()
meta.drop_all()

