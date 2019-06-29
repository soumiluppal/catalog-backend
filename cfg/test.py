import random
import string
class Dev_config():
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root@localhost/test_catalog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])
    JWT_SECRET_KEY = random

config = Dev_config