from bs4 import BeautifulSoup
import urllib.request
import os
import re
import sys
import time
import csv
from collections import Counter

#PAX to look for
PAX=['warbucks']

#download July pages and look for FNGs

urls = []
counts=[]
#define AO to look for PAX at
categories=['nutcracker'] #'disney','purple-cobra','any-given-sunday', 'cletus', 'crazy-ivan','downtown-train', 'ground-pounder','kennys-grave','mutiny','nutcracker','paradise-city','possum-trot','running-4-the-john','sheepdog','tea-time','the-nest','thunder','tiger-blood','to-be-determined','u-turn']
for category in categories:
    counts.clear()
    urls.clear()
    for i in range(8):
        urls.append('https://f3southwake.com/category/'+category+'/page/'+str(i+1)+'/')
    #print(urls)

    #parse backblasts to pull out PAX at AO
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
                counter = 0
                time_=article.findAll('time')[0].contents[0]
                #print(time_)
                tags = article.findAll(rel="tag")
                #print(tags[0].contents[0],counter,time_)
                try:
                    title=article.findAll(rel='bookmark')[0].contents[0]
                except:
                    title= 'Q too lazy to put in a title'
                #print('Title: '+title)
                counter=counter+1
                for i in tags:
                    pax= i.contents[0].encode('utf-8')
                    pax = pax.decode('utf-8')        
                    PAX.append(pax)
                    #look for PAX matches
                    if pax in ['Warbucks']:
                        #ommitting tag matches agains AO names
                        if pax not in ['Fitness', 'Purple Cobra', 'Disney', 'Any Given Sunday', 'Cletus', 'Crazy Ivan', 'Downtown Train', 'Ground Pounder', 'Kennys Grave', 'Mutiny', 'Nutcracker', 'Paradise City', 'Possum Trot', 'Running 4 The John', 'Sheepdog', 'Tea Time', 'The Nest', 'Thunder', 'Tiger Blood', 'To Be Determined', 'U Turn']:
                            counter=counter+1
                            print(category+' '+time_+' '+ title+ ' '+ pax)
                counts.append(counter)
        except:
            print('page not found for: '+url)                
    
