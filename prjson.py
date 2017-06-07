#!/usr/bin/env python3

from codecs import open, getwriter
from io import TextIOWrapper
from json import loads as fromjson
import sys
from pprint import pprint

sys.stdout = getwriter('ascii')(sys.stdout.detach(), 'replace')

files = [open(f) for f in sys.argv[1:]]
if not files:
	files = [TextIOWrapper(sys.stdin.buffer, encoding='utf-8')]
for f in files:
	json = fromjson(f.read())
	pprint(json)
