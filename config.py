from os import path

basedir = path.abspath(path.dirname(__file__))

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = path.join(basedir, "data", "external")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"