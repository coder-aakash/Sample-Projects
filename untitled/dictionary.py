import re
import urllib.request
dict=[]
dic=open("wordList.txt","a+")
pos=dic.tell()
dic.seek(0)
for line in dic:
    end=len(line)
    dict.append(line[:end-1])
print("wordlist")
print(dict)
print("new words")

d = open("MyDictionary.txt", "a+")
if len(dict)==0:
    d.write("MY DICTIONARY:::\n")

#d.close()
#d = open("MyDictionary.txt", "a")
ch=1
while ch==1:
    word = input("Enter the word: ")
    url = "http://www.dictionary.com/browse/" + word

    try:
        if word!='':
            ch=1
        else:
            ch=0
            break
        data = urllib.request.urlopen(url).read()
        data1 = data.decode('utf-8')
        # print(data1)
        m = re.search('<meta name="description" content="', data1)
        start = m.end()
        end = start + 500
        newstr = data1[start:end]
        # print(newstr)
        m = re.search("See more.", newstr)
        end = m.start() - 1
        # print(newstr[:end])
        # count=file.read('\n')
        definition = word.upper() + "::\n" + newstr[:end]+'\n'
        print(definition)
        if (word not in dict):
            print("HOO")
            dic.write(word+'\n')
            dict.append(word)
            d.write("WORD:::")
            d.write(definition)
            #d.close()
           # d = open("MyDictionary.txt", "a")
            for i in dict:
                print(i)


    except:
        print("SORRY!!!WORD NOT FOUND")

print("close")
d.close()
dic.close()
