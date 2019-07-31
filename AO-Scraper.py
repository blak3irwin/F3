from bs4 import BeautifulSoup
import urllib.request
import os
import re
import sys
import time
import csv
from collections import Counter

PAX=[]

#download July pages and look for FNGs

urls = []
categories=['disney','purple-cobra','any-given-sunday', 'cletus', 'crazy-ivan','downtown-train', 'ground-pounder','kennys-grave','mutiny','nutcracker','paradise-city','possum-trot','running-4-the-john','sheepdog','tea-time','the-nest','thunder','tiger-blood','to-be-determined','u-turn']
for category in categories:
    for i in range(6):
        urls.append('https://f3southwake.com/category/'+category+'/page/'+str(i+1)+'/')
    #print(urls)

    
    for url in urls:
        req = urllib.request.Request(url)
        #print(req)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0')
        try:
            page = urllib.request.urlopen(req)
            #print(page)
            #page=urllib.request.urlopen(url)
            file=page.read()

            soup = BeautifulSoup(file, features="html.parser")
            
            articles = soup.findAll("article")
            for article in articles:
                time_=article.findAll('time')[0].contents[0]
                #print(time_)
                tags = article.findAll(rel="tag")
                #print(tags[0].contents[0])
                title=article.findAll(rel='bookmark')[0].contents[0]
                #print('Title: '+title)
                for i in tags:
                    pax= i.contents[0].encode('utf-8')
                    pax = pax.decode('utf-8')        
                    PAX.append(pax)

        except:
            print('page not found for: '+url)                
    matches=[]
    matches = Counter(PAX)
    pairs = []
    for i in matches:
        pairs.append([i,matches[i]])
    print('\n\n***'+category+'**')
    f = open(category+'.csv','w')
    f.write(category+'\n\n')
    f.write('PAX,Count\n')
    for i in sorted(pairs, key=lambda pax_:pax_[1],reverse=True):
        if i[0] not in ['Fitness', 'Purple Cobra', 'Disney', 'Any Given Sunday', 'Cletus', 'Crazy Ivan', 'Downtown Train', 'Ground Pounder', 'Kennys Grave', 'Mutiny', 'Nutcracker', 'Paradise City', 'Possum Trot', 'Running 4 The John', 'Sheepdog', 'Tea Time', 'The Nest', 'Thunder', 'Tiger Blood', 'To Be Determined', 'U Turn']:
            print(str(i[0])+','+str(i[1]))
            f.write(str(i[0])+','+str(i[1])+'\n')
    f.close()
    PAX=[]
    urls=[]