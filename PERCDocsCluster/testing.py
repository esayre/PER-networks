import matplotlib.pyplot as plt

f = open('C:\Users\Waika Wong\PycharmProjects\untitled11\Results', 'r')

data = f.read()
array = []
splat = data.split("\n\n")
for paragraph in splat:
    array.append(paragraph)

print (array)

i = 0
for cluster in array:
    print(2008, cluster.count("(2008)"))
    print(2009, cluster.count("(2009)"))
    print(2010, cluster.count("(2010)"))
    print(2011, cluster.count("(2011)"))
    print(2012, cluster.count("(2012)"))
    print(2013, cluster.count("(2013)"))
    print(2014, cluster.count("(2014)"))
    print(2015, cluster.count("(2015)"))
    print(2016, cluster.count("(2016)"))
    print("There are {} documents in cluster number {}".format(cluster.count("(2008)") + cluster.count("(2009)") + cluster.count("(2010)") + cluster.count("(2011)") + cluster.count("(2012)") + cluster.count("(2013)") + cluster.count("(2014)") + cluster.count("(2015)") + cluster.count("(2016)"), i))
    plt.plot([2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],[cluster.count("(2008)"), cluster.count("(2009)"), cluster.count("(2010)"), cluster.count("(2011)"),cluster.count("(2012)"), cluster.count("(2013)"), cluster.count("(2014)"), cluster.count("(2015)"),cluster.count("(2016)")], linewidth=2.0)
    plt.axis([2007, 2018, 0, 10])
    plt.show()
    i=i+1