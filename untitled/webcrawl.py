import re
import urllib.request
import time
arrayofStocks = ["FB", "GOOG", "DATA", "BABA"]
dictOfStocks={}
choice=1


while(choice==1):
    stock = input("Enter your stock: ").upper()
    url = "https://www.google.com/finance?q="
    url = url + stock
    stime=time.time()
    etime=time.time()
    if (dictOfStocks.get(stock)):
        print("FOUND LOCALLY")
        val=dictOfStocks.get(stock)
        print("THE VALUE OF "+stock + " IS :: "+val)
        etime=time.time()
        print("It took locally "+str(etime- stime)+" sec")
    else:
        print("SEARCHING WEB:")
        try:
            data = urllib.request.urlopen(url).read()
            data1 = data.decode("utf-8")
            '''file1 = open("stockdata.txt", "w")
            print(data1)
            file1.write(data1)
            print("WRITTEN")'''
            m = re.search('<meta itemprop="price"', data1)
            print(m)
            start = m.start()
            end = start + 50
            newstr1 = data1[start:end]
            # print(newstr1)
            m1 = re.search('[0-9]+.[0-9]+', newstr1)
            newstr2 = m1.group(0)
            print("THE VALUE OF " + stock + " IS:: " + str(newstr2))
            dictOfStocks[stock]=newstr2
            etime=time.time()


        except:
            print("couldn't find the requested stocks")
    if(stime!=etime):
        print("it took "+str(etime- stime)+ " seconds")
        print("STOCKS DATA::")
        dataFile = open("stockdatatable.txt", 'w')
        dataFile.write("TABLE OF STOCK VALUES\n")
        count=1
        for k,v in dictOfStocks.items():
            print(k,v)
            dataFile.write(str(count)+". "+k+" :: "+ v+"\n")
            count+=1


    choice=int(input("press 1 to continue.... "))

dataFile.close()



