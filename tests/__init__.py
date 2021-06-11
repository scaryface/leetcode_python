import sys
import os as _os

#sys.path.append(_os.path.dirname(__file__))
for _s in ('algorithms', 'data_strucures'):
    sys.path.append(_os.path.join(_os.path.dirname(__file__), _s))