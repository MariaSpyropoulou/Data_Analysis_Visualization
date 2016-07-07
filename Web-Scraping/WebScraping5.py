import urllib
import json

# web scraping
# Uses google geolocation API to track the place id of a given location

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'characters'

    js = json.loads(str(data))

    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    place = js["results"][0]["place_id"]
    print place
