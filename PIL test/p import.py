import os
import sys

DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(DIR, "PIL.egg"))

#You can now import from PIL normally:
from PIL import Image
