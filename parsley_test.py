from parsley import makeGrammar

returned_list = []
first_grammar = makeGrammar("""
grammar = hour:one colon:two hour:three -> (''.join(one), two, ''.join(three))
hour = digit{2}
colon = ':':s -> s
""", {})

example = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

print ''.join(list(first_grammar('09:14').grammar()))

for key, value in globals().items():
    print key, '=', value
