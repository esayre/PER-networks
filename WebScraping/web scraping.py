import urllib2
import time
from bs4 import BeautifulSoup
import requests
import re
import csv
whitespaces = re.compile('\s+', flags=re.M)
def utf8_to_ascii(s, ws=whitespaces):
    s = s.encode("utf8")
    s = s.decode("ascii", errors="replace")
    s = s.replace(u"\ufffd", "")
    s = ws.sub(" ", s)
    return s.strip()


for L in range(10007, 100020+1):
    quote_page = "http://www.aapt.org/AbstractSearch/FullAbstract.cfm?KeyID={}".format(L)
    response = requests.get(quote_page)
    html = response.content
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, "html.parser")
    try:
        if "No files found for specified criteria" not in html:
            data=[]
            i=0
            while(i<19):
                name = soup.find_all("font", face="Arial", color="000000", size="2")
                data.append(name[i].contents[0])
                i = i + 1
            list=[]
            for k in data:
                k = utf8_to_ascii(k)
                k = k.encode("utf-8")
                list.append(k)

            'print (list)'
            'KEEP APPEHEND IN BINARY MODE! ("ab"), otherwise it will skip lines and wont be able to extract information'
            with open("C:\Users\Waika Wong\PycharmProjects\untitled11/testing.csv", "ab") as f:
                wr = csv.writer(f, delimiter=",")
                wr.writerow(list)
            f.close()

        time.sleep(5)
    except IndexError:
        continue

"10007 to 25435 range of abstracts"
'''last web scraping file was obtaining all the correct information from AAPT, but it was converting everything into txt lists, which
is not useful, I needed the csv format to extract information. The error that would run into was that since everything was filled up
with commas, instead of taking the whole abstract as a variable, it would cut it whenever it would encounter the closest comma
(i.e given the list A= ["hi", "my name", "is Waika, and", "my favourite fruit","is watermelon"]. If I wanted to extract the third
value, that is index = 2, it would give me only "is Waika") I need to run the correct version of code'''

