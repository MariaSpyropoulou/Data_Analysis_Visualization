import urllib
from bs4 import *

# Scraping Numbers from HTML using BeautifulSoup
# web scraping

# The program will use urllib to read the HTML from the
# data files below, and parse the data, extracting numbers
# and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample
# file where we give you the sum for your testing and the other
# is the actual data you need to process for the assignment.

# Sample data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html (Sum=2553)
# Actual data: http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_189531.html (Sum ends with 46)
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_189531.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


tags = soup('span')
ls = []
la = []

for tag in tags:
    ls.append(tag.contents)

for x in ls:
    for y in x:
        la.append(int(y))

sum(la)
