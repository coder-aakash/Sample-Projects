import re
import urllib.request
city=input("Enter your city: ")
print(city)
file=open("weatherReport.txt","a+")
url="http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
#file.write(data1)#error in utf-8 conversion
#print(data1)
m= re.search('span class="phrase">',data1)
start=m.end()
end=start+300
newstr2=data1[start:end]
#print(data1[start:end])
m= re.search('</span>',newstr2)
end=m.start()-1
forecast=newstr2[:end]
forecast=city+" : \n"+forecast
print(forecast)
file.write(forecast+'\n')
input()
'''
#file.write("City::"+city)
'''
