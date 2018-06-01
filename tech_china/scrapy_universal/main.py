__author__ = 'protectfish'

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
a = os.path.abspath(__file__)
b = os.path.dirname(a)
c = sys.path.append(b)

execute(["scrapy","crawl","china"])
