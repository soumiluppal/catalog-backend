import os
from importlib import import_module

env = os.getenv('ENV', 'dev')
config_file_name =  'cfg.' + env
config_file = import_module(config_file_name)
config = config_file.config