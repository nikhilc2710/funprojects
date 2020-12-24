import collections
import json
import os
import sys
import uuid
from pathlib import Path
from colorama import Style ,Fore, init
init()

from nltk.corpus import stopwords
COMMON_WORDS = set(stopwords.words("english"))
BASE_DIR = Path(__file__).resolve(strict=True).parent
DATA_DIR = Path(BASE_DIR).joinpath("data")
OUTPUT_DIR = Path(BASE_DIR).joinpath("output")

def save_file(filename,data):
    uid=uuid.uuid4().hex
    outputfile=f'{filename}_{uid}.txt'
    with open(Path(OUTPUT_DIR).joinpath(outputfile),'w') as outfile:
        outfile.write(data)
with open('x.txt','r') as f:
    x=f.readlines()
print(x)


