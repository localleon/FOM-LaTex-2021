from os import spawnle
import re

with open("./fuellwoerter.txt") as f: 
    counter = 0

    print(r"\b(", end='')
    for line in f.readlines():
        print(line.strip("\n") +"|", end='',sep='')
    print(r")\b")

