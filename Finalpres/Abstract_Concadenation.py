import glob

read_files = glob.glob("C:/Users/Waika Wong/PycharmProjects/untitled11/txt/*.txt")

with open("C:/Users/Waika Wong/PycharmProjects/untitled11/testt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())