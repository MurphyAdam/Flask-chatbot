"""Flask config class."""
import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	"""Set Flask configuration vars."""

	# General Config
	TESTING = False
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
	SECRET_KEY = os.environ.get('SECRET_KEY') or b'some_badass_and_long_key_@_2020'


class Development(Config):

	TESTING = os.environ.get('TESTING') or False
	DEBUG = os.environ.get('DEBUG') or True
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
	SECRET_KEY = os.environ.get('SECRET_KEY') or b'DevelopmentKey468djkj475641;::454574551fdkJNdy'