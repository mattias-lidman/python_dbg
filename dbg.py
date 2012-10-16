import ipdb
import inspect
import re
import sys
import traceback
import json
import pprint

def dbg(file=None, func=None, line=None):
    # Drop into debugger if the stack contains calls from a particular file,
    # function or line number. 
    # File- and function names are matched using a regex. Every specified
    # parameter must match.
    
    for frame in inspect.stack():
        if (
            (not file or re.search(file, frame[1])) and
            (not func or re.search(func, frame[3])) and
            (not line or line == frame[2])
        ):
            ipdb.set_trace(frame=sys._getframe(1))
            break

def stack():
    # TODO: Clear out last few frames, e.g dbg stuff.
    traceback.print_stack()

def file(ob):
    # Get path to the file where an object is defined.
    return inspect.getfile(f.__class__)

def pp(ob):
    # Pretty-print object. Useful in particular for nested dicts.
    if type(ob) is dict:
        print(json.dumps(ob, sort_keys=True, indent=2))
    else:
        pprint.pprint(ob)
