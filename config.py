from dotenv import dotenv_values

config = dotenv_values(".env")

user = config.get('MYSQL_USER', 'point')
password = config.get("MYSQL_PASSWORD", '12345678')
host = config.get("MYSQL_HOST", 'localhost')
database = config.get("MYSQL_DATABASE", 'point')

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
