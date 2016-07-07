import urllib
import json

# The program will prompt for a URL, read the JSON data from that URL
# using urllib and then parse and extract the comment counts from the
# JSON data, compute the sum of the numbers in the file and return the
# sum
# web scraping

# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing
# and the other is the actual data you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_189532.json (Sum ends with 72)

empty = []
jsn = raw_input('Enter JSON location: ')
url = urllib.urlopen(jsn)
data = url.read()
info = json.loads(str(data))
print 'User count:', len(info)

for key, value in info.iteritems():
    jsonlist = value

for item in jsonlist:
    empty.append(item['count'])

print sum(empty)
