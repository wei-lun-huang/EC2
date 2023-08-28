import os
from sqlalchemy import create_engine

db_user = os.environ.get("MYSQL_USER")
db_password = os.environ.get("MYSQL_PWD")
db_host = os.environ.get("MYSQL_HOST")
db_port = os.environ.get("MYSQL_PORT")
db_name = os.environ.get("MYSQL_DB")


db_url = (
    f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4"
)
engine = create_engine(db_url)
connection = engine.connect()
print(connection)
