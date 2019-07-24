from bs4 import BeautifulSoup
import urllib.request
import os
import re
import sys
import time
from collections import Counter

#array of FNGs
FNGs=['Angel', 'Pyle', 'Pile', 'Oboe', 'Snowden', 'Jeter', 'Boot Scoot', 'Pastel', 'Boots', 'Warhol', 'Tumbles', 'Dory', 'Tee Time', 'Posada', 'Vanellope', 'Tonka', 'Tony the Teacher', 'Pistorius', 'Tetanus', 'U-verse', 'Finkle', 'Heavy Flow', 'BB-8', 'Yellow Submarine', 'Sea Legs', 'Brownie', 'White Claw', 'Duck Hunt', 'Go-Gurt', 'Grasshopper', 'Big Green', 'Snip']
FNG_COUNTER=0
FNG_COST=57

TwelveOaks=['3rd Cousin','AAA','Angel','Blue Hen','Boot Scoot','Brony','Brownie','Buford','Cowboy','Da Business','Dawgpound','Flanigan','Forceps','Moby','Peak Week','Philly Special','Pigpen','Pyle','Slide Rule','Thigh Master']
TwelveOaksPaying=['3rd Cousin','Blue Hen','Boot Scoot','Brony','Da Business','Flanigan','Moby','Peak Week','Pigpen','Slide Rule']
TwelveOaks_COUNTER=0
TwelveOaks_match=[]

#download July pages and look for FNGs
urls= ['https://f3southwake.com/2019/07/', 'https://f3southwake.com/2019/07/page/2/','https://f3southwake.com/2019/07/page/3/', 'https://f3southwake.com/2019/07/page/4/','https://f3southwake.com/2019/07/page/5/', 'https://f3southwake.com/2019/07/page/6/', 'https://f3southwake.com/2019/07/page/7/', 'https://f3southwake.com/2019/07/page/8/', 'https://f3southwake.com/2019/07/page/9/', 'https://f3southwake.com/2019/07/page/10/', 'https://f3southwake.com/2019/07/page/11/', 'https://f3southwake.com/2019/07/page/12/', 'https://f3southwake.com/2019/07/page/13']

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
                for FNG in FNGs: 
                    match=''
                    match = re.search(FNG,pax,re.IGNORECASE)
                    if match and tags[0].contents[0] != i.contents[0]:
                        FNG_COUNTER=FNG_COUNTER+1
                        print(str(FNG_COUNTER)+') '+pax+' posted @ '+tags[0].contents[0]+' on '+time_+ ' for ' +title)
                for resident in TwelveOaks:
                    match=''
                    match = re.search(resident,pax,re.IGNORECASE)
                    if match and tags[0].contents[0] != i.contents[0]:
                        TwelveOaks_COUNTER=TwelveOaks_COUNTER+1
                        print(str(TwelveOaks_COUNTER)+') '+pax+' posted @ '+tags[0].contents[0]+' on '+time_+ ' for ' +title)
                        TwelveOaks_match.append(resident)
    except:
        print('page not found for: '+url)                

print('\n')

print('FNG Count: '+str(FNG_COUNTER))
cost = FNG_COST*FNG_COUNTER
print('Cost per FNG: '+str(FNG_COST))
print('FNG Total Cost: '+str(cost))

print('TwelveOaks PAX Count= '+str(TwelveOaks_COUNTER)+'\n')
TwelveOaks_counts = Counter(TwelveOaks_match)
TwelveOaks_Payout = 0
for dudes in TwelveOaks_counts:
    print (dudes+' owes '+ (str(TwelveOaks_COUNTER - TwelveOaks_counts[dudes]))+' (posted '+str(TwelveOaks_counts[dudes])+' times.)')
    TwelveOaks_Payout = TwelveOaks_Payout + (TwelveOaks_COUNTER - TwelveOaks_counts[dudes])

print('\nTotal TwelveOaks payout = $'+str(TwelveOaks_Payout))

print('\n FNG + TwelveOaks Payout =$'+str(cost+TwelveOaks_Payout))
