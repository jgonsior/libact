"""
Concrete labeler classes.
"""
from .ideal_labeler import IdealLabeler

try:
    pass
except ImportError:
    raise ImportError("Error importing matplotlib." "InteractiveLabeler not supported.")
