# coding=utf-8
import re

with open('C:/Users/Waika Wong/PycharmProjects/untitled11/testt') as infile, open('C:/Users/Waika Wong/PycharmProjects/untitled11/test', 'w') as outfile:
    copy = False
    for line in infile:
        if line.startswith('Speaker Order: ') or line.strip() == "michael.j.ross@colorado.edu":
            copy = True
            outfile.write("\n")
            outfile.write("BREAKS HERE")
            outfile.write("\n")
            outfile.write("\n")
        elif line.strip() == "":
            copy = False
        elif copy:
            outfile.write(line)

with open('C:/Users/Waika Wong/PycharmProjects/untitled11/testt') as infile, open('C:/Users/Waika Wong/PycharmProjects/untitled11/scores', 'w') as titles:
    copy = False
    for line in infile:
        if line.strip() == "":
            bucket = []
            copy = True
        elif line.startswith('Paper Type: '):
            for strings in bucket:
                titles.write(strings + '\n')
            copy = False
        elif copy:
            bucket.append(line.strip())


