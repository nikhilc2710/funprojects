import collections
import json
import os
import sys
import uuid
from pathlib import Path
import multiprocessing
import time
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

COMMON_WORDS = set(stopwords.words("english"))
BASE_DIR = Path(__file__).resolve(strict=True).parent
DATA_DIR = Path(BASE_DIR).joinpath("data")
OUTPUT_DIR = Path(BASE_DIR).joinpath("output")

def save_file(filename, data):
    random_str = uuid.uuid4().hex
    outfile = f"{filename}_{random_str}.txt"
    with open(Path(OUTPUT_DIR).joinpath(outfile), "w") as outfile:
        outfile.write(data)


def get_word_counts(filename):
    wordcount = collections.Counter()
    # get counts
    with open(Path(DATA_DIR).joinpath(filename), "r") as f:
        for line in f:
            wordcount.update(line.split())
    for word in set(COMMON_WORDS):
        del wordcount[word]

    # save file
    save_file(filename, json.dumps(dict(wordcount.most_common(20))))

    proc = os.getpid()

    print(f"Processed {filename} with process id: {proc}")

PROCESSES = multiprocessing.cpu_count()
def run():
    print(f"Running with {PROCESSES} processes!")

    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(
            get_word_counts,
            [
                "pride-and-prejudice.txt",
                "heart-of-darkness.txt",
                "frankenstein.txt",
                "dracula.txt",
            ],
        )
        # clean up
        p.close()
        p.join()

    print(f"Time taken Async multiprocessing= {time.time() - start:.10f}")
def sequential():
    start = time.time()
    for i in ["pride-and-prejudice.txt", "heart-of-darkness.txt", "frankenstein.txt", "dracula.txt",]:
        get_word_counts(i)
    print(f"Time taken Sequential= {time.time() - start:.10f}")
run()
sequential()
