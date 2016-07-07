import urllib
from bs4 import *

# Following Links in Python
# web scraping

# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the
# first name in the list, follow that link and repeat the process a
# number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where
# we give you the name for your testing and the other is the actual data
# you need to process for the assignment

# Sample problem: Start at
# http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at:
# http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Megha.html
# Find the link at position 18 (the first name is 1).
# Follow that link.
# Repeat this process 7 times. The answer is the last name that you retrieve.


def extract_link(urls=str, position=17):
    htmls = urllib.urlopen(urls).read()
    soups = BeautifulSoup(htmls)
    tagss = soups('a')
    new_url = tagss[position].get('href', None)
    return new_url

page = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Megha.html'


def find_seventh_name(pages):
    reps = 6
    while reps >= 0:
        new = extract_link(pages)
        pages = new
        print pages
        reps -= 1
