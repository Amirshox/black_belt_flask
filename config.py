from dotenv import dotenv_values

config = dotenv_values(".env")

user = config["MYSQL_USER"]
password = config["MYSQL_PASSWORD"]
host = config["MYSQL_HOST"]
database = config["MYSQL_DATABASE"]

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
