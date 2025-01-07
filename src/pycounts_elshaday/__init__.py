# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_elshaday")

# Import the functions from pycounts_elshaday.py
from .pycounts_elshaday import load_text, clean_text, count_words
