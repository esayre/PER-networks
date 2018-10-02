import csv

years = ["2014","2015","2016","2017"]
for i in range(11,16+1):
    f = open("C:\Users\Waika Wong\PycharmProjects\untitled11\PER Abs\Abs{}.csv".format(i),"rU")

    csv_f = csv.reader(f)

    with open("C:/Users/Waika Wong/PycharmProjects/untitled11/text_samples", "a") as outfile, open("C:/Users/Waika Wong/PycharmProjects/untitled11/text_titles", "a") as titles:
        for row in csv_f:
            if "PER: " in row[1]:
                for i in years:
                    if i in row[6]:
                        outfile.write(row[17])
                        outfile.write("\n")
                        outfile.write("\n")
                        outfile.write("BREAKS HERE")
                        outfile.write("\n")
                        outfile.write("\n")
                        titles.write(row[4])
                        titles.write("\n")
        outfile.close()
        titles.close()

    f.close()