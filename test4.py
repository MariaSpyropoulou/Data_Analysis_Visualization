import os

class ConfigDict(dict):

    def __init__(self, filename):

        # This is a private attribute
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as fn:
                for line in fn:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)
        print(self.items())

    # This method will override dict method
    # Called when user says thisdict[key]=value
    # which is the exact same thing as the magic method
    # __setitem__
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fn:
            for key, val in self.items():
                fn.write('{}={}\n'.format(key, val))



cc = ConfigDict('config.txt')

print(cc['2016-02-16'])
print(cc['2016-03-16'])
cc['database'] = 'mysql_managed'

print cc

