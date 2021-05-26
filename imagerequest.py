import os
import json
import sys
import requests

path = "" #modify path here
secretkey = ""
secretcx = ""
if len(sys.argv)<3:
	print("Usage : python "+sys.argv[0]+" <query> <number of results> >")
	exit()

searchQuery=sys.argv[1]

try:
	sys.argv[2]=int(sys.argv[2])
except:
	print("Number of results must be an integer")
	exit()

totalqueries=(sys.argv[2]//10) 
if totalqueries<1 or totalqueries>100:
	print("Total Queries must be more than 10 and less than 1000 due to API limits")
	exit()


if len(sys.argv)>=4:
	print("Need only 2 arguments")
	exit()

query=[]
searches={'key':secretkey,'searchType':'image','q':searchQuery,'cx':secretcx,'start':1} 
 
for i in range(totalqueries):
    search=searches.copy()
    search['start']=i*10+1   
    query.insert(i+1,search)

X=[]
for Q in query:
    X.append(requests.get("https://www.googleapis.com/customsearch/v1?",params=Q))
print(X)

response=[]
for result in X:
    response.append(result.json())

imagelist=[]
for x in response:
    for y in x["items"]:
        address=y["link"]
        imagelist.append(address.split("?",1)[0])
print("Total images : "+ str(len(imagelist)))

imagelist
i=0
for image in imagelist:
	print(image)
	filename=image.rsplit('/', 1)[-1]
	if(filename==""):
		filename=str(i)
	try:
		r=requests.get(image,allow_redirects=True)
	except:
		print("Connection Error : "+filename)
	try:
		os.mkdir(path+searchQuery)
	except:
		pass
	open(path+searchQuery+"\\"+filename,'wb').write(r.content)
	print("Downloaded : "+filename)
	i+=1
print("Downloaded : "+str(i) +" files.")
