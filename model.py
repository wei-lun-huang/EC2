import os
import sys
from sqlalchemy import create_engine

# db_user = os.environ.get("MYSQL_USER")
# print(db_user)
# db_password = os.environ.get("MYSQL_PWD")
# print(db_password)
# db_host = os.environ.get("MYSQL_HOST")
# print(db_host)
# db_port = os.environ.get("MYSQL_PORT")
# print(db_port)
# db_name = os.environ.get("MYSQL_DB")
# print(db_name)

db_user = sys.argv[1]
db_password = sys.argv[2]
db_host = sys.argv[3]
db_port = sys.argv[4]
db_name = sys.argv[5]


db_url = (
    f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4"
)
engine = create_engine(db_url)
connection = engine.connect()
print(connection)
