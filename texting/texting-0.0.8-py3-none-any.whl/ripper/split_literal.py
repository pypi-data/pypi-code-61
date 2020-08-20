import re
from functools import partial

from texting.enum.regexes import LITERAL
from texting.ripper.ripper import ripper

RE_LITERAL = re.compile(LITERAL)

split_literal = partial(ripper, RE_LITERAL)
