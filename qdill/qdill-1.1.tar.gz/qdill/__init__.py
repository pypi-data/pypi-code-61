import dill
from os.path import exists

# convenient dill load function
def load(fname):
    with open(fname, 'rb') as f:
        return dill.load(f)
    return

# convenient dill save function
def save(thing, fname):
    with open(fname, 'wb') as f:
        return dill.dump(thing, f)
    return

# checks if file exists, if it doesn't
# it saves the default thing to the file
# AND returns the default thing
def defaultLoad(default_thing, fname):
    if exists(fname):
        return load(fname)
    else:
        save(default_thing, fname)
        return default_thing
    return

# if you need more fine-grained control of dill
# Don't use this 'library'