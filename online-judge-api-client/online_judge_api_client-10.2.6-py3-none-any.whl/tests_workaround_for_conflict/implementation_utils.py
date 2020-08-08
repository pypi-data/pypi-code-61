import bs4

import onlinejudge_workaround_for_conflict._implementation.logging as log
import onlinejudge_workaround_for_conflict._implementation.testcase_zipper
import onlinejudge_workaround_for_conflict._implementation.utils as utils
from onlinejudge_workaround_for_conflict.type import *


def get_handmade_sample_cases(self, *, html: str) -> List[TestCase]:
    # parse
    soup = bs4.BeautifulSoup(html, utils.html_parser)
    samples = onlinejudge_workaround_for_conflict._implementation.testcase_zipper.SampleZipper()
    for pre in soup.select('.sample pre'):
        log.debug('pre %s', str(pre))
        it = self._parse_sample_tag(pre)
        if it is not None:
            data, name = it
            samples.add(data.encode(), name)
    return samples.get()
