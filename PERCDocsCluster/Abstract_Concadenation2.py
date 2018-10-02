import csv
import glob

read_files = glob.glob("C:/Users/Waika Wong/PycharmProjects/untitled11/cvs documents/*.csv")

with open("C:/Users/Waika Wong/PycharmProjects/untitled11/Lists", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
