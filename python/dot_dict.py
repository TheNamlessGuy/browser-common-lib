# https://stackoverflow.com/a/23689767
class DotDict(dict):
  __dir__ = dict.keys
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__
  def __getattr__(*args):
    val = dict.get(*args)
    return DotDict(val) if type(val) is dict else val