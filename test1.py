# Inheritance and Polymorphism
# Dog and Cat inherit from Animal but
# show_affection are different = polymorphism
# Changed in version 2.7: The positional argument
# specifiers can be omitted,
# so '{} {}' is equivalent to '{0} {1}' in string formatting
# check documentation, this %s or this %3.2f are old
# although still used
import random


class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print '{} eats {}'.format(self.name, food)


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle'])

    def fetch(self, thing):
        print '{} goes after the {}!'.format(self.name, thing)

    def show_affection(self):
        print '{} wags tail'.format(self.name)


class Cat(Animal):

    def swatstring(self):
        print '{} shreds the string!'.format(self.name)

    def show_affection(self):
        print '{} purrs'.format(self.name)


for a in (Dog('dolan'), Cat('floof'), Dog('gooby'), Cat('jinx')):
    a.show_affection()
