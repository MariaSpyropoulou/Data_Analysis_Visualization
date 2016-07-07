import abc
from datetime import datetime

# This is typical inheritance hierarchy
# we want to add general functionality in the parent class
# and specific behaviour in the child classes


class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    # this is an abstract method
    # this means it NEEDS to be implemented
    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    # Duplicating any of this code in the child class
    # would be inefficient

    def write_line(self, text):
        ms = open(self.filename, 'a')
        ms.write(text + '\n')
        ms.close()


class DelimFile(WriteFile):

    # We could use self.filename = filename here
    # but we want to avoid duplication
    # thus we use the complex syntax of the super class constructor

    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    # The write function gets overriden in both child classes
    # and this is polymorphism

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)


# LogFile class doesn't need __init__ because
# it simply writes things to the filename, which it can get
# from parent class' __init__


class LogFile(WriteFile):

    def write(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{}     {}'.format(date_str, this_line))


log = LogFile('config.txt')
delimiter = DelimFile('delim.csv', ', ')

log.write('this is a log message')
log.write('this is another goofy message')

delimiter.write('1234567')

