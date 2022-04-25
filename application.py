from app import application
from utils.db import db

with application.app_context():
    db.create_all()

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0")
