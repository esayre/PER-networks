import csv

f = open("C:\Users\Waika Wong\PycharmProjects\untitled11\Lists")

csv_f = csv.reader(f)

with open("C:\Users\Waika Wong\PycharmProjects\untitled11\Listss", "wb") as outfile:
    for row in csv_f:
        outfile.write(row[3])
        outfile.write("\n")
        outfile.write("\n")
        outfile.write("BREAKS HERE")
        outfile.write("\n")
        outfile.write("\n")

f.close()

f = open("C:\Users\Waika Wong\PycharmProjects\untitled11\Lists")

csv_f = csv.reader(f)

with open("C:\Users\Waika Wong\PycharmProjects\untitled11\score", 'w') as titles:
    for row in csv_f:
        titles.write("{} ({})".format(row[2], row[8]))
        titles.write("\n")

f.close()