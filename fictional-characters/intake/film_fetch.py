#!/usr/bin/env python3
"""Fetch the official CMU corpus archive into the local film cache."""
from pathlib import Path
from urllib.request import urlopen
import hashlib, json
HERE=Path(__file__).resolve().parent
OUT=HERE/'film-cache'/'MovieSummaries.tar.gz'
URL='https://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz'
OUT.parent.mkdir(parents=True,exist_ok=True)
if OUT.exists():
    raise SystemExit(f'Refusing to overwrite existing archive: {OUT}')
h=hashlib.sha256(); size=0
with urlopen(URL,timeout=60) as response, OUT.open('xb') as dest:
    while block:=response.read(1024*1024):
        dest.write(block); h.update(block); size+=len(block)
print(json.dumps({'url':URL,'path':str(OUT),'bytes':size,'sha256':h.hexdigest()},indent=2))
