from dotenv import dotenv_values
import os

config = dotenv_values(".env")

user = config["MYSQL_USER"]
password = config["MYSQL_PASSWORD"]
host = config["MYSQL_HOST"]
database = config["MYSQL_DATABASE"]

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)
