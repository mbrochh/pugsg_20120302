"""Another file in our package."""
from urlparse import urljoin


def print_twitter_url():
    """We can lookup the urljoin method via ``<Leader>g``."""
    print urljoin('http://www.twitter.com', 'mbrochh')


def try_to_import_from_demo_py():
    """Code completion makes importing easy!"""
    print 'Try to import that method which starts with ``open_``.'


def set_breakpoint(arg1, arg2, data=None):
    """We can set breakpoints via ``<Leader>b``."""
    foo = 'bar'
    result = arg1 + arg2
    print 'Try to set a breakpoint before this statement.'
    print 'Then run ``python demo.py``.'
    print 'Use s to step into the next method.'
    we_can_step_into_here()
    import ipdb; ipdb.set_trace() # BREAKPOINT
    print 'Good bye!'
    # ?
    # help a
    # a
    # l
    # next
    # inspect data
    # bt
    # u
    # s
    # c
    # exit


def we_can_step_into_here():
    print('It works!')
