import re
from . import scripts

patterns = [
    (r"^bro\s", scripts.hi),
    (r"^sis\s", scripts.sis)
]