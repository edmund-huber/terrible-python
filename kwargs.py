# The following can make it hard to test things.

from collections import OrderedDict

def f(**kwargs):
    assert dict == type(kwargs)

d = OrderedDict([('z', 1), ('y', 2)])
f(**d)

# If you don't add new kwargs at the end of the list of kwargs, you
# might be changing how existing calls to the method are interpreted.

def f(actor=None, candy=None):
    return 'my favorite actor is %s and my favorite candy is %s' % (actor, candy)

def g(actor=None, fruit=None, candy=None):
    return 'my favorite actor is %s and my favorite candy is %s, and my favorite fruit is %s' % (actor, candy, fruit)

assert f('clint eastwood', 'twix') == 'my favorite actor is clint eastwood and my favorite candy is twix'
assert g('clint eastwood', 'twix') == 'my favorite actor is clint eastwood and my favorite candy is None, and my favorite fruit is twix'
