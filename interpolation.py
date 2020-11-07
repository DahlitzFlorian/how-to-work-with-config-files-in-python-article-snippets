# interpolation.py
from configparser import ConfigParser
from configparser import ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read("interpolation_config.ini")

print(config.get("destinations", "app_dir"))
