# -*- coding:UTF-8 -*-
from pyuts import ScrapyCommandU


class TestCrawl(ScrapyCommandU):
    
    def run(self, args, opts):
        print(args)
        self.runSpider("Test")
        