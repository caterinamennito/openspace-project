from utils.openspace import Openspace
from utils.file_utils import file_utils

list = file_utils("./utils/colleagues.csv")
my_openspace = Openspace(list)
my_openspace.organize()
my_openspace.display()