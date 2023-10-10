import re
from . import views

patterns = [
    (r"^bro\s", views.hi),
    (r"^sis\s", views.sis),
]
