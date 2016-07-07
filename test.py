# Encapsulation


class MaxSizeList(object):

    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value
        self.list = []

    def push(self, string):
        try:
            string = str(string)
        except ValueError:
            string = ''
        while len(self.list) <= self.val:
            self.list.append(string)
        else:
            self.list.pop(0)

    def get_list(self):
        return self.list


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('hey')
a.push('hi')
a.push('what')
a.push('fuk')

b.push('hey')
b.push('hi')
b.push('what')
b.push('fuk')

print(a.get_list())
print(b.get_list())