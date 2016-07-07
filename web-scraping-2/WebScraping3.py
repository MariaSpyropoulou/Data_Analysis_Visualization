import urllib
import xml.etree.ElementTree as ET


# The program will prompt for a URL, read the XML data from that URL
# using urllib and then parse and extract the comment counts from the
# XML data, compute the sum of the numbers in the file.
# web scraping

# We provide two files for this assignment. One is a sample file
# where we give you the sum for your testing and the other is the
# actual data you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_189528.xml (Sum ends with 89)

# You are to look through all the <comment> tags and find the <count> values sum the numbers.

while True:
    address = raw_input('Enter URL: ')
    if len(address) < 1:
        break

    print 'Retrieving', address
    url = urllib.urlopen(address)
    data = url.read()
    print 'Retrieved', len(data), 'characters'

    tree = ET.fromstring(data)
    results = tree.findall('.//count')
    lst = [i.text for i in results]
    lst = [int(i) for i in lst]
    print sum(lst)
